"""
ONNX model export for cross-platform deployment.

Provides conversion of trained models to ONNX format for deployment
on various platforms and runtimes.
"""

from pathlib import Path
from typing import Any, Optional

try:
    import onnx
    import onnxruntime as ort
    from skl2onnx import convert_sklearn
    from skl2onnx.common.data_types import FloatTensorType
    ONNX_AVAILABLE = True
except ImportError:
    ONNX_AVAILABLE = False


def export_sklearn_to_onnx(
    model: Any,
    initial_types: Optional[list] = None,
    output_path: Optional[Path] = None,
    n_features: Optional[int] = None
) -> Optional[Path]:
    """
    Export scikit-learn model to ONNX format.
    
    Args:
        model: Trained scikit-learn model
        initial_types: Input type specification. Auto-detected if None.
        output_path: Path to save ONNX model. Uses default if None.
        n_features: Number of input features. Required if initial_types is None.
    
    Returns:
        Path to exported ONNX model, or None if export fails
    """
    if not ONNX_AVAILABLE:
        print("✗ ONNX not available. Install with: pip install onnx onnxruntime skl2onnx")
        return None
    
    try:
        # Set initial types if not provided
        if initial_types is None:
            if n_features is None:
                raise ValueError("Either initial_types or n_features must be provided")
            initial_types = [("float_input", FloatTensorType([None, n_features]))]
        
        # Convert to ONNX
        onnx_model = convert_sklearn(
            model,
            initial_types=initial_types,
            target_opset=12
        )
        
        # Set default output path if not provided
        if output_path is None:
            output_path = Path("model.onnx")
        
        # Save ONNX model
        with open(output_path, "wb") as f:
            f.write(onnx_model.SerializeToString())
        
        print(f"✓ Exported model to ONNX: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Failed to export to ONNX: {e}")
        return None


def validate_onnx_model(onnx_path: Path) -> bool:
    """
    Validate an ONNX model.
    
    Args:
        onnx_path: Path to ONNX model file
    
    Returns:
        True if valid, False otherwise
    """
    if not ONNX_AVAILABLE:
        print("✗ ONNX not available.")
        return False
    
    try:
        # Load and check model
        onnx_model = onnx.load(str(onnx_path))
        onnx.checker.check_model(onnx_model)
        
        print(f"✓ ONNX model is valid: {onnx_path}")
        return True
        
    except Exception as e:
        print(f"✗ ONNX model validation failed: {e}")
        return False


def get_onnx_model_info(onnx_path: Path) -> dict:
    """
    Get information about an ONNX model.
    
    Args:
        onnx_path: Path to ONNX model file
    
    Returns:
        Dictionary with model information
    """
    if not ONNX_AVAILABLE:
        print("✗ ONNX not available.")
        return {}
    
    try:
        onnx_model = onnx.load(str(onnx_path))
        
        info = {
            "ir_version": onnx_model.ir_version,
            "opset_version": onnx_model.opset_import[0].version if onnx_model.opset_import else None,
            "producer_name": onnx_model.producer_name,
            "producer_version": onnx_model.producer_version,
            "inputs": [],
            "outputs": [],
        }
        
        # Get input info
        for inp in onnx_model.graph.input:
            input_info = {
                "name": inp.name,
                "type": inp.type.WhichOneof("value"),
            }
            if inp.type.HasField("tensor_type"):
                tensor_type = inp.type.tensor_type
                input_info["shape"] = [
                    dim.dim_value if dim.HasField("dim_value") else -1
                    for dim in tensor_type.shape.dim
                ]
                input_info["dtype"] = tensor_type.elem_type
            info["inputs"].append(input_info)
        
        # Get output info
        for out in onnx_model.graph.output:
            output_info = {
                "name": out.name,
                "type": out.type.WhichOneof("value"),
            }
            if out.type.HasField("tensor_type"):
                tensor_type = out.type.tensor_type
                output_info["shape"] = [
                    dim.dim_value if dim.HasField("dim_value") else -1
                    for dim in tensor_type.shape.dim
                ]
                output_info["dtype"] = tensor_type.elem_type
            info["outputs"].append(output_info)
        
        return info
        
    except Exception as e:
        print(f"✗ Failed to get model info: {e}")
        return {}


def infer_onnx_model(
    onnx_path: Path,
    input_data: Any,
    input_name: str = "float_input"
) -> Optional[Any]:
    """
    Run inference with an ONNX model.
    
    Args:
        onnx_path: Path to ONNX model file
        input_data: Input data (numpy array)
        input_name: Name of the input node
    
    Returns:
        Model predictions, or None if inference fails
    """
    if not ONNX_AVAILABLE:
        print("✗ ONNX not available.")
        return None
    
    try:
        # Create inference session
        session = ort.InferenceSession(str(onnx_path))
        
        # Run inference
        input_feed = {input_name: input_data}
        outputs = session.run(None, input_feed)
        
        return outputs[0]
        
    except Exception as e:
        print(f"✗ Inference failed: {e}")
        return None


def compare_sklearn_onnx_predictions(
    sklearn_model: Any,
    onnx_path: Path,
    test_data: Any,
    tolerance: float = 1e-5
) -> bool:
    """
    Compare predictions from sklearn and ONNX models.
    
    Args:
        sklearn_model: Original scikit-learn model
        onnx_path: Path to ONNX model
        test_data: Test data for comparison
        tolerance: Tolerance for numerical differences
    
    Returns:
        True if predictions match within tolerance, False otherwise
    """
    if not ONNX_AVAILABLE:
        print("✗ ONNX not available.")
        return False
    
    try:
        import numpy as np
        
        # Get sklearn predictions
        sklearn_pred = sklearn_model.predict(test_data)
        
        # Get ONNX predictions
        onnx_pred = infer_onnx_model(
            onnx_path,
            test_data.astype(np.float32)
        )
        
        if onnx_pred is None:
            return False
        
        # Compare predictions
        max_diff = np.max(np.abs(sklearn_pred - onnx_pred.flatten()))
        
        if max_diff < tolerance:
            print(f"✓ Predictions match (max diff: {max_diff:.2e})")
            return True
        else:
            print(f"✗ Predictions differ (max diff: {max_diff:.2e})")
            return False
        
    except Exception as e:
        print(f"✗ Comparison failed: {e}")
        return False


def export_model_with_metadata(
    model: Any,
    output_path: Path,
    n_features: int,
    metadata: dict
) -> bool:
    """
    Export model to ONNX with metadata.
    
    Args:
        model: Trained model
        output_path: Path to save ONNX model
        n_features: Number of input features
        metadata: Metadata to embed in model
    
    Returns:
        True if successful, False otherwise
    """
    onnx_path = export_sklearn_to_onnx(
        model,
        n_features=n_features,
        output_path=output_path
    )
    
    if onnx_path is None:
        return False
    
    # Add metadata
    try:
        onnx_model = onnx.load(str(onnx_path))
        
        for key, value in metadata.items():
            meta = onnx_model.metadata_props.add()
            meta.key = key
            meta.value = str(value)
        
        onnx.save(onnx_model, str(onnx_path))
        print("✓ Added metadata to ONNX model")
        return True
        
    except Exception as e:
        print(f"✗ Failed to add metadata: {e}")
        return False
