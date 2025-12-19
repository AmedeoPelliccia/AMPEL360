# Tool Launchpad Specification

**AMPEL360 CA360º — Tool Access & Licensing Fabric (TALF) Integration**

---

## Metadata

- **ATA:** 00 (GENERAL)
- **Program:** SPACET Q10 BASELINE PLUS
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_DAB (Digital Applications & Blockchains)
- **Category:** DELIVERABLE
- **Type:** SPEC (Specification)
- **Status:** ACTIVE
- **Issue-Revision:** I01-R01

---

## Purpose

This specification defines the **Tool Launchpad** (Feature F09) as a UI + policy surface that provides fluent, integrated access to engineering tools with preflight validation, license management, and audit logging.

The Tool Launchpad is the orchestrator for tool access—transforming the portal from a "link farm" into an intelligent execution environment.

---

## Scope

This specification covers:

1. Tool tile structure and metadata
2. Launch channel definitions
3. Workspace binding mechanisms
4. Licensing models and preflight checks
5. Audit event requirements
6. Failure mode handling
7. UI/UX requirements
8. Backend service contracts

---

## 1. Tool Tile Structure

Each tool tile is a **governed object** with the following mandatory elements:

### 1.1 Tool Identity

```yaml
tool_id: string (required, unique)
  # Unique identifier for the tool
  # Format: lowercase-kebab-case
  # Example: "ansys-fluent-2024", "matlab-r2024a"

tool_name: string (required)
  # Human-readable tool name
  # Example: "ANSYS Fluent", "MATLAB R2024a"

version: string (optional)
  # Tool version or class
  # Example: "2024.1", "R2024a", "latest"

tool_class: string (optional)
  # Functional classification
  # Example: "cfd", "fem", "model-based-design", "data-analysis"

owner_aor: string (required)
  # AoR responsible for this tool
  # Must be a valid STK identifier
  # Example: "STK_PHM", "STK_DAB"

vendor: string (optional)
  # Tool vendor/provider
  # Example: "ANSYS", "MathWorks", "internal"

documentation_url: string (optional)
  # Link to tool documentation
```

### 1.2 Launch Configuration

```yaml
launch:
  channel: enum (required)
    # One of: VDI | HPC_job | container | web | api
    # Defines how the tool is accessed

  deep_link: string (required)
    # Launch URL or command
    # Channel-specific format:
    #   VDI: "vdi://tool-identifier"
    #   HPC_job: "hpc://job-template-id"
    #   container: "docker://image:tag" or "k8s://deployment"
    #   web: "https://tool.domain.com/launch"
    #   api: "api://service-name/endpoint"

  parameters: object (optional)
    # Launch parameters (channel-specific)
    # Example for HPC: {cores: 16, memory: "64GB", walltime: "4h"}

  requires_interaction: boolean (default: true)
    # Whether launch requires user interaction
    # False for API-only tools
```

### 1.3 Workspace Bindings

```yaml
workspace_bindings:
  repo_nodes: array of strings (optional)
    # Repository paths to mount in the tool workspace
    # Example: ["CAXS/AoR/STK_PHM", "data/thermal-models"]

  exports: array of strings (optional)
    # Export directories (outputs from tool)
    # Example: ["exports/simulation-results", "exports/reports"]

  datasets: array of strings (optional)
    # Dataset identifiers to make available
    # Example: ["flight-test-data-2024", "material-properties-db"]

  templates: array of strings (optional)
    # Template identifiers for artifact generation
    # Example: ["phm-analysis-report", "evidence-pack-thermal"]

  environment_variables: object (optional)
    # Environment variables to set
    # Example: {AMPEL360_CONTEXT: "${current_context}"}
```

### 1.4 Licensing

```yaml
licensing:
  model: enum (required)
    # One of: concurrent | named | pool | unlimited | none

  pool_id: string (conditional)
    # Required if model is "concurrent" or "pool"
    # Identifies the license pool to check

  checkout_mode: enum (default: automatic)
    # One of: automatic | manual | pre_reserved
    # automatic: checkout when tool launches
    # manual: user initiates checkout explicitly
    # pre_reserved: license already reserved for this user

  max_duration: string (optional)
    # Maximum license checkout duration
    # Format: ISO 8601 duration (e.g., "PT4H" = 4 hours)

  grace_period: string (optional)
    # Grace period before forced license return
    # Format: ISO 8601 duration

  constraints: object (optional)
    # Additional license constraints
    # Example: {max_concurrent_per_user: 1, restricted_hours: "09:00-17:00"}
```

### 1.5 Preflight Checks

```yaml
preflight:
  checks: array of enums (required)
    # Checks to run before allowing launch
    # Possible values:
    #   - sso_session: Verify SSO session is valid
    #   - entitlement: Verify user has required entitlement group
    #   - license: Verify license is available
    #   - compute_profile: Verify compute resources are ready
    #   - network: Verify network connectivity
    #   - storage: Verify storage quota/availability

  requirements: object (optional)
    # Specific requirements per check
    # Example:
    #   entitlement: {groups: ["phm-engineers", "cfd-users"]}
    #   compute_profile: {min_cores: 8, min_memory: "32GB"}
    #   storage: {min_free_space: "10GB"}

  timeout: string (default: "PT30S")
    # Maximum time for all preflight checks
    # Format: ISO 8601 duration

  allow_override: boolean (default: false)
    # Whether user can override failed preflight checks
    # Requires audit log entry if true
```

### 1.6 Audit Events

```yaml
audit:
  events: array of enums (required)
    # Events to log for audit trail
    # Possible values:
    #   - launch: Tool launch initiated
    #   - checkout: License checked out
    #   - export: Artifacts exported
    #   - close: Tool session closed
    #   - failure: Launch or operation failed

  log_level: enum (default: INFO)
    # One of: DEBUG | INFO | WARNING | ERROR

  retention: string (optional)
    # Audit log retention period
    # Format: ISO 8601 duration or "indefinite"

  fields: object (optional)
    # Additional fields to log with each event
    # Example: {project_id: true, task_id: true, context: true}
```

### 1.7 Failure Modes

```yaml
failure_modes:
  license_unavailable:
    action: enum (required)
      # One of: block | retry | queue | log
      # block: Prevent launch with error message
      # retry: Auto-retry after delay
      # queue: Add to wait queue and notify when available
      # log: Log and proceed (for "nice-to-have" tools)

    message: string (optional)
      # User-facing error message

    retry_config: object (conditional)
      # Required if action is "retry"
      # Example: {max_attempts: 3, delay: "PT1M"}

    queue_config: object (conditional)
      # Required if action is "queue"
      # Example: {max_wait: "PT30M", notify_channels: ["portal", "email"]}

  entitlement_denied:
    action: enum (required)
      # One of: block | notify
      # block: Prevent launch with error message
      # notify: Notify admin and log incident

    message: string (optional)
      # User-facing error message

  compute_unavailable:
    action: enum (required)
      # One of: block | queue | scale
      # scale: Attempt to provision additional compute resources

  network_failure:
    action: enum (required)
      # One of: block | offline_mode
      # offline_mode: Launch tool in limited offline mode (if supported)
```

---

## 2. Launch Channels

### 2.1 VDI (Virtual Desktop Infrastructure)

**Description:** Tool runs in a remote virtual desktop session.

**Deep Link Format:**  
`vdi://tool-identifier[?param=value]`

**Preflight Checks:**
- SSO session validity
- Entitlement (VDI access group)
- VDI session availability
- License availability

**Launch Flow:**
1. Preflight checks pass
2. Request VDI session from broker
3. Mount workspace bindings
4. Inject environment variables
5. Launch tool in VDI session
6. Log launch event

**Example:**
```yaml
launch:
  channel: VDI
  deep_link: "vdi://ansys-fluent-2024?profile=high-performance"
```

---

### 2.2 HPC_job (High-Performance Computing)

**Description:** Tool runs as a batch job on HPC cluster.

**Deep Link Format:**  
`hpc://job-template-id[?param=value]`

**Preflight Checks:**
- SSO session validity
- Entitlement (HPC access group)
- HPC queue availability
- Compute resource availability
- License availability

**Launch Flow:**
1. Preflight checks pass
2. Generate job script from template
3. Inject workspace bindings and parameters
4. Submit job to HPC scheduler
5. Return job ID and monitoring link
6. Log launch event

**Example:**
```yaml
launch:
  channel: HPC_job
  deep_link: "hpc://cfd-simulation-template"
  parameters:
    cores: 128
    memory: "512GB"
    walltime: "8h"
    partition: "high-mem"
```

---

### 2.3 Container (Docker/Kubernetes)

**Description:** Tool runs in a containerized environment.

**Deep Link Format:**  
`docker://image:tag` or `k8s://deployment-name`

**Preflight Checks:**
- SSO session validity
- Entitlement (container access group)
- Container runtime availability
- Image availability
- Compute resource availability

**Launch Flow:**
1. Preflight checks pass
2. Pull container image (if not cached)
3. Mount workspace bindings as volumes
4. Inject environment variables
5. Start container
6. Provide access link (if web interface)
7. Log launch event

**Example:**
```yaml
launch:
  channel: container
  deep_link: "docker://ampel360/thermal-analysis:2024.1"
  parameters:
    ports: ["8080:8080"]
    volumes: ["${workspace}:/workspace"]
```

---

### 2.4 Web (Web Application)

**Description:** Tool is accessed via web browser.

**Deep Link Format:**  
`https://tool.domain.com/launch[?param=value]`

**Preflight Checks:**
- SSO session validity (may use SAML/OIDC)
- Entitlement (web tool access group)
- Service availability

**Launch Flow:**
1. Preflight checks pass
2. Generate SSO token
3. Construct launch URL with token and parameters
4. Open in browser (new tab/window)
5. Log launch event

**Example:**
```yaml
launch:
  channel: web
  deep_link: "https://jupyter.ampel360.org/launch?context=${current_context}"
```

---

### 2.5 API (Programmatic Access)

**Description:** Tool is accessed programmatically (no UI).

**Deep Link Format:**  
`api://service-name/endpoint`

**Preflight Checks:**
- SSO session validity (API token)
- Entitlement (API access group)
- Service availability
- Rate limit check

**Launch Flow:**
1. Preflight checks pass
2. Generate API token
3. Return API endpoint and token to caller
4. Log launch event

**Example:**
```yaml
launch:
  channel: api
  deep_link: "api://ml-training-service/train"
  parameters:
    model_type: "cnn"
    dataset: "flight-test-2024"
```

---

## 3. Preflight Check Specifications

### 3.1 SSO Session Check

**Purpose:** Verify user has a valid SSO session.

**Implementation:**
- Check session cookie or token validity
- Refresh token if expired but refresh token is valid
- Redirect to SSO login if no valid session

**Pass Criteria:**
- Valid session token with expiry > 5 minutes

**Failure Action:**
- Redirect to SSO login
- Log failure event

---

### 3.2 Entitlement Check

**Purpose:** Verify user has required entitlement groups.

**Implementation:**
- Query identity provider for user groups
- Check if user is member of required groups
- Cache result for 5 minutes

**Pass Criteria:**
- User is member of all required entitlement groups

**Failure Action:**
- Block launch with error message
- Notify admin if repeated failures
- Log failure event

---

### 3.3 License Check

**Purpose:** Verify license is available.

**Implementation:**
- Query TALF service for license pool status
- Check if license can be checked out
- Optionally reserve license

**Pass Criteria:**
- License is available in pool
- User has quota for checkout

**Failure Action:**
- Execute failure_modes.license_unavailable action
- Log failure event

---

### 3.4 Compute Profile Check

**Purpose:** Verify compute resources meet requirements.

**Implementation:**
- Check CPU, memory, GPU availability
- Check storage quota
- Check network bandwidth

**Pass Criteria:**
- All resource requirements met

**Failure Action:**
- Block launch or queue (depending on configuration)
- Suggest alternative compute profiles
- Log failure event

---

### 3.5 Network Check

**Purpose:** Verify network connectivity to tool service.

**Implementation:**
- Ping tool service endpoint
- Check latency and bandwidth

**Pass Criteria:**
- Service reachable within timeout
- Latency < 500ms

**Failure Action:**
- Block launch or enable offline mode
- Log failure event

---

### 3.6 Storage Check

**Purpose:** Verify storage quota and availability.

**Implementation:**
- Check user storage quota
- Check workspace storage availability

**Pass Criteria:**
- Free space meets minimum requirement
- User has not exceeded quota

**Failure Action:**
- Block launch with quota error
- Suggest cleanup actions
- Log failure event

---

## 4. Audit Event Schema

Every audit event must include:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO 8601 datetime",
  "event_type": "launch | checkout | export | close | failure",
  "tool_id": "string",
  "tool_name": "string",
  "user_id": "string",
  "user_name": "string",
  "aor_id": "string",
  "context": {
    "program": "string",
    "family": "string",
    "variant": "string",
    "version": "string",
    "node": "string",
    "task_id": "string (optional)"
  },
  "launch_channel": "VDI | HPC_job | container | web | api",
  "license_info": {
    "pool_id": "string (optional)",
    "checkout_id": "string (optional)",
    "duration": "string (optional)"
  },
  "result": "success | failure",
  "failure_reason": "string (if result is failure)",
  "metadata": {
    "additional_fields": "object"
  }
}
```

**Retention:**
- Minimum 7 years for certification compliance
- Stored in immutable audit log (append-only)

---

## 5. UI/UX Requirements

### 5.1 Tool Launchpad View

**Layout:**
- Grid of tool tiles
- Each tile shows: icon, tool name, status, quick actions

**Tile States:**
- Available (green indicator)
- License unavailable (yellow indicator)
- Entitlement denied (red indicator)
- Offline (gray indicator)

**Actions:**
- Click to launch (with preflight)
- Context menu: View details, Documentation, Report issue

**Filters:**
- By tool class
- By owner AoR
- By availability status

---

### 5.2 Launch Dialog

When user clicks a tool tile:

1. **Preflight Progress Indicator**
   - Show checks being performed
   - Real-time status updates
   - Estimated time remaining

2. **Preflight Success**
   - Display launch confirmation
   - Show expected launch time
   - Option to cancel

3. **Preflight Failure**
   - Display failure reason
   - Suggest remediation actions
   - Options: Retry, Queue, Report issue

---

### 5.3 Active Sessions Panel

**Display:**
- List of active tool sessions
- For each session: tool name, launch time, status, resource usage

**Actions:**
- View session details
- Export artifacts
- Close session (with confirmation)
- Extend license (if applicable)

---

## 6. Backend Service Contracts

### 6.1 TALF Service

**Endpoints:**

```
GET /licenses/pools/{pool_id}/status
  → Returns: {available: int, total: int, queue_length: int}

POST /licenses/checkout
  Body: {pool_id, user_id, duration}
  → Returns: {checkout_id, expires_at}

POST /licenses/return
  Body: {checkout_id}
  → Returns: {status: "returned"}

GET /licenses/user/{user_id}/active
  → Returns: [{checkout_id, pool_id, tool_id, expires_at}]
```

---

### 6.2 Entitlement Service

**Endpoints:**

```
GET /entitlements/user/{user_id}/groups
  → Returns: [group1, group2, ...]

POST /entitlements/check
  Body: {user_id, required_groups}
  → Returns: {authorized: boolean, missing_groups: [...]}
```

---

### 6.3 Launch Service

**Endpoints:**

```
POST /launch/vdi
  Body: {tool_id, user_id, workspace_bindings, parameters}
  → Returns: {session_id, connection_url}

POST /launch/hpc
  Body: {tool_id, user_id, job_template, parameters}
  → Returns: {job_id, status_url}

POST /launch/container
  Body: {tool_id, user_id, image, volumes, parameters}
  → Returns: {container_id, access_url}

POST /launch/web
  Body: {tool_id, user_id, parameters}
  → Returns: {launch_url, sso_token}
```

---

### 6.4 Audit Service

**Endpoints:**

```
POST /audit/log
  Body: {event_type, tool_id, user_id, context, metadata}
  → Returns: {event_id, timestamp}

GET /audit/events
  Query: {user_id, tool_id, start_date, end_date, event_type}
  → Returns: [{event}, ...]
```

---

## 7. Integration with Portal Features

### 7.1 Context Bar (F01)

Tool Launchpad uses current context to:
- Filter available tools
- Pre-populate workspace bindings
- Set environment variables

### 7.2 Task Wizard (F05)

When starting a task:
- Task wizard can auto-launch required tools
- Tool outputs are linked to task artifacts

### 7.3 Evidence Console (F07)

Tool exports are automatically registered in evidence console with:
- Tool provenance metadata
- Execution parameters
- Integrity hash

### 7.4 Notification Engine (F14)

Tool Launchpad triggers notifications for:
- License checkout failures
- Tool session expirations
- Queue position updates

---

## 8. Security Considerations

### 8.1 Authentication

- All tool access requires valid SSO session
- API tokens are short-lived (max 1 hour)
- Tokens are scoped to specific tool/resource

### 8.2 Authorization

- Entitlement checks are non-bypassable
- All authorization decisions are logged
- Failed authorization attempts trigger alerts after threshold

### 8.3 Audit

- All tool launches are logged (even failures)
- Audit logs are immutable
- Audit log access is restricted and logged

### 8.4 Data Protection

- Workspace bindings do not expose sensitive paths
- Tool exports are scanned for sensitive data
- License information is not exposed to end users

---

## 9. Performance Requirements

| Metric | Requirement |
|--------|-------------|
| Preflight check total time | < 5 seconds (typical), < 10 seconds (max) |
| Tool launch time (VDI) | < 30 seconds |
| Tool launch time (HPC) | Job submitted within 5 seconds |
| Tool launch time (container) | < 15 seconds |
| Tool launch time (web) | < 2 seconds |
| License check response time | < 500ms |
| Entitlement check response time | < 500ms |
| Tile status update frequency | Every 30 seconds |

---

## 10. References

- **Portal Feature Catalog (SSOT):** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__portal-feature-catalog_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **AoR Portal Contract Schema:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__aor-portal-contract-schema_DELIVERABLE_SCHEMA_I01-R01_ACTIVE.md`
- **TALF Specification (STK_PHM):** `CAXS/AoR/STK_PHM/PORTAL/DELIVERABLES/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_00_LC01_K01_STK_PHM__talf-tool-access-licensing-fabric_DELIVERABLE_PROC_I01-R01_DRAFT.md`

---

## Change Log

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| I01-R01 | 2025-12-19 | STK_DAB | Initial specification |

---

**END OF DOCUMENT**
