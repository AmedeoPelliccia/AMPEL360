"""
DVC (Data Version Control) integration for large dataset management.

Provides versioned, reproducible data pipelines with remote storage support.
"""

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional


class DVCManager:
    """Manage DVC operations for dataset versioning."""
    
    def __init__(self, repo_root: Optional[Path] = None):
        """
        Initialize DVC manager.
        
        Args:
            repo_root: Root directory of the repository. Defaults to current directory.
        """
        self.repo_root = repo_root or Path.cwd()
        
    def is_initialized(self) -> bool:
        """Check if DVC is initialized in the repository."""
        dvc_dir = self.repo_root / ".dvc"
        return dvc_dir.exists()
    
    def init(self) -> bool:
        """
        Initialize DVC in the repository.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            subprocess.run(
                ["dvc", "init"],
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            print("✓ DVC initialized")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ DVC init failed: {e.stderr.decode()}")
            return False
        except FileNotFoundError:
            print("✗ DVC not installed. Install with: pip install dvc[s3]")
            return False
    
    def add_dataset(self, data_path: Path) -> bool:
        """
        Add dataset to DVC tracking.
        
        Args:
            data_path: Path to dataset file or directory
        
        Returns:
            True if successful, False otherwise
        """
        try:
            subprocess.run(
                ["dvc", "add", str(data_path)],
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            print(f"✓ Added {data_path} to DVC tracking")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to add {data_path}: {e.stderr.decode()}")
            return False
    
    def configure_remote(
        self,
        remote_name: str,
        remote_url: str,
        default: bool = True
    ) -> bool:
        """
        Configure remote storage for DVC.
        
        Args:
            remote_name: Name of the remote
            remote_url: URL of the remote storage (e.g., s3://bucket/path)
            default: Set as default remote
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Add remote
            subprocess.run(
                ["dvc", "remote", "add", remote_name, remote_url],
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            
            # Set as default if requested
            if default:
                subprocess.run(
                    ["dvc", "remote", "default", remote_name],
                    cwd=self.repo_root,
                    check=True,
                    capture_output=True
                )
            
            print(f"✓ Configured remote: {remote_name} -> {remote_url}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to configure remote: {e.stderr.decode()}")
            return False
    
    def push(self, remote: Optional[str] = None) -> bool:
        """
        Push data to remote storage.
        
        Args:
            remote: Name of remote to push to. Uses default if None.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            cmd = ["dvc", "push"]
            if remote:
                cmd.extend(["-r", remote])
            
            subprocess.run(
                cmd,
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            print("✓ Pushed data to remote")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to push: {e.stderr.decode()}")
            return False
    
    def pull(self, remote: Optional[str] = None) -> bool:
        """
        Pull data from remote storage.
        
        Args:
            remote: Name of remote to pull from. Uses default if None.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            cmd = ["dvc", "pull"]
            if remote:
                cmd.extend(["-r", remote])
            
            subprocess.run(
                cmd,
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            print(f"✓ Pulled data from remote")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to pull: {e.stderr.decode()}")
            return False
    
    def get_dataset_info(self, data_path: Path) -> Optional[Dict[str, Any]]:
        """
        Get DVC metadata for a dataset.
        
        Args:
            data_path: Path to dataset file
        
        Returns:
            Dictionary with DVC metadata or None if not tracked
        """
        dvc_file = Path(str(data_path) + ".dvc")
        if not dvc_file.exists():
            return None
        
        try:
            with open(dvc_file) as f:
                import yaml
                return yaml.safe_load(f)
        except Exception as e:
            print(f"✗ Failed to read DVC file: {e}")
            return None
    
    def checkout(self, revision: Optional[str] = None) -> bool:
        """
        Checkout data for a specific git revision.
        
        Args:
            revision: Git revision (commit, tag, branch). Uses current if None.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            cmd = ["dvc", "checkout"]
            if revision:
                # First checkout git revision, then DVC
                subprocess.run(
                    ["git", "checkout", revision],
                    cwd=self.repo_root,
                    check=True,
                    capture_output=True
                )
            
            subprocess.run(
                cmd,
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )
            print(f"✓ Checked out DVC data")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to checkout: {e.stderr.decode()}")
            return False


def create_dvc_pipeline(
    name: str,
    stages: Dict[str, Dict[str, Any]],
    output_file: Path = Path("dvc.yaml")
) -> bool:
    """
    Create a DVC pipeline configuration.
    
    Args:
        name: Pipeline name
        stages: Dictionary of stage definitions
        output_file: Path to output dvc.yaml file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        import yaml
        
        pipeline = {
            "stages": stages
        }
        
        with open(output_file, "w") as f:
            yaml.dump(pipeline, f, default_flow_style=False)
        
        print(f"✓ Created DVC pipeline: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to create pipeline: {e}")
        return False


def get_dataset_version_info(manifest_path: Path) -> Dict[str, Any]:
    """
    Get DVC version info for a dataset manifest.
    
    Args:
        manifest_path: Path to dataset manifest
    
    Returns:
        Dictionary with version information
    """
    dvc_manager = DVCManager()
    dvc_info = dvc_manager.get_dataset_info(manifest_path)
    
    info = {
        "manifest_path": str(manifest_path),
        "dvc_tracked": dvc_info is not None,
    }
    
    if dvc_info:
        info["dvc_md5"] = dvc_info.get("outs", [{}])[0].get("md5")
        info["dvc_size"] = dvc_info.get("outs", [{}])[0].get("size")
    
    return info
