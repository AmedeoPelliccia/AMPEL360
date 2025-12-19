# TALF Service Specification

**Tool Access & Licensing Fabric Service**

---

## Metadata

- **ATA:** 86 (Off-board Digital Services Platform)
- **Program:** SPACET Q10 BASELINE PLUS
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_DAB (Digital Applications & Blockchains)
- **Category:** DELIVERABLE
- **Type:** SPEC
- **Status:** DRAFT
- **Issue-Revision:** I01-R01

---

## 1. Purpose

The **TALF Service** (Tool Access & Licensing Fabric) is the backend service responsible for:

1. **Entitlement checking** — Verifying user permissions to access specific tools
2. **License pool management** — Managing concurrent license checkouts and returns
3. **Preflight validation** — Performing pre-launch checks (SSO, compute resources, licenses)
4. **Launch orchestration** — Coordinating tool launch across different channels (VDI, web, HPC)
5. **Audit logging** — Recording all tool access events for compliance

---

## 2. Service Architecture

### 2.1 Components

```
┌─────────────────────────────────────────────────────────────┐
│                      TALF Service                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────┐  │
│  │  Entitlement     │  │  License Pool    │  │  Preflight│  │
│  │  Engine          │  │  Manager         │  │  Checker  │  │
│  └──────────────────┘  └──────────────────┘  └──────────┘  │
│                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────┐  │
│  │  Launch          │  │  Workspace       │  │  Audit    │  │
│  │  Orchestrator    │  │  Provisioner     │  │  Logger   │  │
│  └──────────────────┘  └──────────────────┘  └──────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
         ↓                       ↓                      ↓
    ┌─────────┐           ┌──────────┐          ┌───────────┐
    │  Tool   │           │ License  │          │  Audit    │
    │ Catalog │           │  Pools   │          │   Log     │
    └─────────┘           └──────────┘          └───────────┘
```

### 2.2 Data Sources

**Note:** All data source files listed below exist and are validated by Gate E (TALF Validation) in the CI workflow.

- **Tool Catalog:** `CAXS/INFRASTRUCTURE/access/tool_catalog.yaml` ✓ (Verified by CI)
- **Entitlement Matrix:** `CAXS/INFRASTRUCTURE/access/entitlement_matrix.csv` ✓ (Verified by CI)
- **License Events Registry:** `CAXS/INFRASTRUCTURE/access/license_events_registry.md` ✓ (Verified by CI)
- **User Identity Service:** SSO/IAM integration (External)
- **Compute Resource Manager:** HPC/VDI infrastructure (External)

---

## 3. API Specification

### 3.1 Entitlement Check

**Endpoint:** `POST /api/talf/v1/entitlement/check`

**Request:**
```json
{
  "user_id": "user@ampel360.org",
  "tool_id": "ansys-fluent-2024",
  "aor": "STK_PHM"
}
```

**Response:**
```json
{
  "entitled": true,
  "groups": ["phm-engineers", "cfd-users"],
  "reason": null
}
```

**Error Response:**
```json
{
  "entitled": false,
  "groups": [],
  "reason": "User not in required entitlement groups: phm-engineers"
}
```

---

### 3.2 License Check

**Endpoint:** `POST /api/talf/v1/license/check`

**Request:**
```json
{
  "tool_id": "ansys-fluent-2024",
  "pool_id": "ansys-pool-01",
  "user_id": "user@ampel360.org"
}
```

**Response:**
```json
{
  "available": true,
  "pool_status": {
    "total": 10,
    "in_use": 7,
    "available": 3
  },
  "checkout_token": "tok_abc123xyz",
  "expires_at": "2025-12-20T06:31:00Z"
}
```

**Error Response (No License Available):**
```json
{
  "available": false,
  "pool_status": {
    "total": 10,
    "in_use": 10,
    "available": 0
  },
  "queue_position": 3,
  "estimated_wait": "PT15M"
}
```

---

### 3.3 Preflight Check

**Endpoint:** `POST /api/talf/v1/preflight`

**Request:**
```json
{
  "user_id": "user@ampel360.org",
  "tool_id": "ansys-fluent-2024",
  "aor": "STK_PHM",
  "checks": ["sso_session", "entitlement", "license", "compute_profile"]
}
```

**Response:**
```json
{
  "status": "PASS",
  "checks": {
    "sso_session": {
      "status": "PASS",
      "message": "Valid SSO session"
    },
    "entitlement": {
      "status": "PASS",
      "message": "User entitled"
    },
    "license": {
      "status": "PASS",
      "message": "License available",
      "checkout_token": "tok_abc123xyz"
    },
    "compute_profile": {
      "status": "PASS",
      "message": "Compute resources available"
    }
  }
}
```

**Error Response (Failed Check):**
```json
{
  "status": "FAIL",
  "checks": {
    "sso_session": {
      "status": "PASS",
      "message": "Valid SSO session"
    },
    "entitlement": {
      "status": "FAIL",
      "message": "User not in required groups: phm-engineers"
    },
    "license": {
      "status": "SKIP",
      "message": "Skipped due to entitlement failure"
    },
    "compute_profile": {
      "status": "SKIP",
      "message": "Skipped due to entitlement failure"
    }
  }
}
```

---

### 3.4 Launch Tool

**Endpoint:** `POST /api/talf/v1/launch`

**Request:**
```json
{
  "user_id": "user@ampel360.org",
  "tool_id": "ansys-fluent-2024",
  "aor": "STK_PHM",
  "checkout_token": "tok_abc123xyz",
  "workspace_context": {
    "repo_nodes": ["CAXS/AoR/STK_PHM", "data/cfd-models"],
    "exports": ["exports/simulation-results/cfd"],
    "datasets": ["flight-test-data-2024"]
  }
}
```

**Response:**
```json
{
  "status": "LAUNCHED",
  "session_id": "sess_xyz789abc",
  "launch_url": "vdi://ansys-fluent-2024?session=sess_xyz789abc",
  "expires_at": "2025-12-20T06:31:00Z",
  "workspace": {
    "mount_points": [
      "/workspace/CAXS/AoR/STK_PHM",
      "/workspace/data/cfd-models"
    ],
    "export_path": "/workspace/exports/simulation-results/cfd"
  }
}
```

---

### 3.5 Return License

**Endpoint:** `POST /api/talf/v1/license/return`

**Request:**
```json
{
  "checkout_token": "tok_abc123xyz",
  "session_id": "sess_xyz789abc",
  "user_id": "user@ampel360.org"
}
```

**Response:**
```json
{
  "status": "RETURNED",
  "duration": "PT2H15M",
  "audit_event_id": "evt_license_return_123456"
}
```

---

### 3.6 Audit Event

**Endpoint:** `POST /api/talf/v1/audit`

**Request:**
```json
{
  "event_type": "launch",
  "user_id": "user@ampel360.org",
  "tool_id": "ansys-fluent-2024",
  "aor": "STK_PHM",
  "session_id": "sess_xyz789abc",
  "checkout_token": "tok_abc123xyz",
  "timestamp": "2025-12-19T22:31:00Z",
  "metadata": {
    "launch_channel": "VDI",
    "compute_profile": "high-performance"
  }
}
```

**Response:**
```json
{
  "audit_event_id": "evt_launch_123456",
  "stored": true
}
```

---

## 4. Failure Modes

### 4.1 License Unavailable

**Action:** `queue`

**Workflow:**
1. User requests tool launch
2. TALF checks license pool → all licenses in use
3. TALF adds user to queue
4. TALF returns queue position and estimated wait
5. When license becomes available, TALF notifies user via portal/email

### 4.2 Entitlement Denied

**Action:** `block`

**Workflow:**
1. User requests tool launch
2. TALF checks entitlement → user not in required groups
3. TALF blocks request
4. TALF returns error message with instructions to contact AoR lead

### 4.3 Compute Unavailable

**Action:** `queue` or `retry`

**Workflow:**
1. User requests tool launch
2. TALF checks compute resources → insufficient resources
3. TALF queues request or suggests retry

---

## 5. Audit Requirements

All TALF events must be logged with:

- **Event ID:** Unique identifier
- **Event Type:** `launch`, `checkout`, `return`, `export`, `failure`
- **Timestamp:** ISO 8601 format
- **User ID:** User performing the action
- **Tool ID:** Tool being accessed
- **AoR:** Area of Responsibility context
- **Session ID:** Unique session identifier
- **Checkout Token:** License checkout token (if applicable)
- **Metadata:** Additional context (launch channel, compute profile, etc.)

**Retention:** 7 years (P7Y)

---

## 6. Integration Points

### 6.1 Portal Frontend

- Portal calls TALF preflight API before showing "Launch" button
- Portal displays preflight results (pass/fail with reasons)
- Portal handles launch orchestration via TALF launch API

### 6.2 IAM/SSO

- TALF integrates with SSO for session validation
- TALF queries IAM for user group membership

### 6.3 License Servers

- TALF integrates with vendor license servers (FlexLM, RLM, etc.)
- TALF manages license checkout/return lifecycle

### 6.4 Compute Infrastructure

- TALF integrates with VDI for desktop provisioning
- TALF integrates with HPC for job submission
- TALF provisions workspace mounts

---

## 7. Implementation Status

- [x] Specification drafted
- [ ] API implementation
- [ ] License pool manager
- [ ] Entitlement engine
- [ ] Launch orchestrator
- [ ] Audit logger
- [ ] Integration with portal
- [ ] Integration with IAM/SSO
- [ ] Integration with license servers
- [ ] Integration with compute infrastructure

---

## 8. References

- **Tool Catalog:** `CAXS/INFRASTRUCTURE/access/tool_catalog.yaml`
- **Entitlement Matrix:** `CAXS/INFRASTRUCTURE/access/entitlement_matrix.csv`
- **License Events Registry:** `CAXS/INFRASTRUCTURE/access/license_events_registry.md`
- **Portal Feature Catalog:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__portal-feature-catalog_REGISTRY_CAT_I01-R01_ACTIVE.md`

---

**END OF DOCUMENT**
