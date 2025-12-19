# License & Audit Events Registry

**Purpose:** Capture tool access lifecycle events for audit trails, LC gate evidence, and operational analytics.

**Retention:** Events retained for 7 years per compliance requirements.

**Schema Version:** 1.0

---

## Event Types

| Event Type | Description | Triggers Evidence Recording |
|-----------|-------------|----------------------------|
| `login` | User SSO login to portal | No |
| `launch` | Tool launch initiated successfully | Yes |
| `checkout` | License checkout successful | Yes |
| `checkout_fail` | License checkout failed (pool exhausted, entitlement missing) | Yes (blocking event) |
| `usage` | Periodic tool usage heartbeat (every 15 min) | No |
| `export` | File/data export from tool workspace | Yes (export control) |
| `close` | Tool session closed normally | Yes |
| `timeout` | Tool session timed out | Yes |
| `killed` | Tool session forcibly terminated | Yes |

---

## Event Schema

```json
{
  "event_id": "unique-uuid",
  "timestamp": "ISO8601 datetime",
  "event_type": "login|launch|checkout|checkout_fail|usage|export|close|timeout|killed",
  "user_id": "SSO user identifier",
  "tool_id": "tool_catalog tool_id",
  "session_id": "unique session identifier",
  "aor": "STK_* owning area of responsibility",
  "project": "project identifier",
  "task_id": "task identifier (if applicable)",
  "license_info": {
    "pool_id": "license pool identifier",
    "checkout_mode": "interactive|batch",
    "tokens_used": 1,
    "server": "license server address"
  },
  "outcome": "success|blocked|failed|timeout",
  "blocking_reason": "entitlement_missing|license_unavailable|capacity_exceeded|...",
  "evidence_ref": "link to evidence artifact (if applicable)",
  "metadata": {
    "ip_address": "client IP",
    "vdi_host": "VDI host (if applicable)",
    "hpc_job_id": "HPC job ID (if applicable)",
    "export_path": "export file path (if event_type=export)"
  }
}
```

---

## Sample Events

### Example 1: Successful Launch

```json
{
  "event_id": "evt-2025-12-19-001",
  "timestamp": "2025-12-19T14:32:01Z",
  "event_type": "launch",
  "user_id": "john.doe@ampel360.com",
  "tool_id": "catia-v5-vdi",
  "session_id": "sess-catia-20251219-143201",
  "aor": "STK_PHM",
  "project": "SPACET-Q10",
  "task_id": "K04-T011",
  "license_info": {
    "pool_id": "catia_v5_design",
    "checkout_mode": "interactive",
    "tokens_used": 1,
    "server": "license-server-01.ampel360.internal"
  },
  "outcome": "success",
  "blocking_reason": null,
  "evidence_ref": "EV-PHM-TALF-LAUNCH-001",
  "metadata": {
    "ip_address": "10.0.1.45",
    "vdi_host": "vdi-worker-03.ampel360.internal",
    "hpc_job_id": null,
    "export_path": null
  }
}
```

### Example 2: Checkout Failure (License Exhausted)

```json
{
  "event_id": "evt-2025-12-19-002",
  "timestamp": "2025-12-19T15:47:12Z",
  "event_type": "checkout_fail",
  "user_id": "jane.smith@ampel360.com",
  "tool_id": "ansys-hpc-solver",
  "session_id": null,
  "aor": "STK_PHM",
  "project": "SPACET-Q10",
  "task_id": "K04-T015",
  "license_info": {
    "pool_id": "ansys_hpc_structural",
    "checkout_mode": "batch",
    "tokens_used": 0,
    "server": "license-server-02.ampel360.internal"
  },
  "outcome": "blocked",
  "blocking_reason": "license_unavailable",
  "evidence_ref": "EV-PHM-TALF-BLOCK-001",
  "metadata": {
    "ip_address": "10.0.2.78",
    "vdi_host": null,
    "hpc_job_id": null,
    "export_path": null
  }
}
```

### Example 3: Checkout Failure (Entitlement Missing)

```json
{
  "event_id": "evt-2025-12-19-003",
  "timestamp": "2025-12-19T16:22:34Z",
  "event_type": "checkout_fail",
  "user_id": "bob.jones@ampel360.com",
  "tool_id": "matlab-vdi-analysis",
  "session_id": null,
  "aor": "STK_PHM",
  "project": "SPACET-Q10",
  "task_id": "K05-T008",
  "license_info": {
    "pool_id": "matlab_engineering",
    "checkout_mode": "interactive",
    "tokens_used": 0,
    "server": "license-server-01.ampel360.internal"
  },
  "outcome": "blocked",
  "blocking_reason": "entitlement_missing",
  "evidence_ref": "EV-PHM-TALF-BLOCK-002",
  "metadata": {
    "ip_address": "10.0.1.89",
    "vdi_host": null,
    "hpc_job_id": null,
    "export_path": null
  }
}
```

### Example 4: Successful Export

```json
{
  "event_id": "evt-2025-12-19-004",
  "timestamp": "2025-12-19T17:05:22Z",
  "event_type": "export",
  "user_id": "john.doe@ampel360.com",
  "tool_id": "catia-v5-vdi",
  "session_id": "sess-catia-20251219-143201",
  "aor": "STK_PHM",
  "project": "SPACET-Q10",
  "task_id": "K04-T011",
  "license_info": {
    "pool_id": "catia_v5_design",
    "checkout_mode": "interactive",
    "tokens_used": 1,
    "server": "license-server-01.ampel360.internal"
  },
  "outcome": "success",
  "blocking_reason": null,
  "evidence_ref": "EV-PHM-TALF-EXPORT-001",
  "metadata": {
    "ip_address": "10.0.1.45",
    "vdi_host": "vdi-worker-03.ampel360.internal",
    "hpc_job_id": null,
    "export_path": "/workspace/exports/SPACET-Q10/thermal_analysis_results.catpart"
  }
}
```

---

## Event Collection

Events are collected via:
- Portal backend API (login, launch, checkout attempts)
- License server integrations (checkout success/fail, token usage)
- VDI/HPC platform webhooks (session lifecycle, exports)
- Periodic heartbeat (usage tracking)

---

## Evidence Linkage

Events with `evidence_ref` are indexed in:
- `CAXS/AoR/STK_PHM/PORTAL/REGISTRIES/evidence_index.md`
- Release Evidence Packs (for LC gates requiring tool access proof)

Blocking events (checkout_fail with outcome=blocked) are **mandatory evidence** for PMO escalation and capacity planning.

---

## Queries & Analytics

Common queries:
- License pool utilization by tool_id and time range
- Blocking events by user, project, task
- Export events for export control compliance
- Tool usage by AoR for capacity forecasting

---

## Retention & Compliance

- **Retention period:** 7 years
- **Storage:** Append-only event store (JSONL format)
- **Backup:** Daily snapshots to secure archive
- **Access control:** Read access limited to STK_CM, STK_PMO, STK_CERT, audit roles

---

## Version Control

**Registry Version:** 1.0  
**Schema Version:** 1.0  
**Last Updated:** 2025-12-19  
**Owner:** STK_DAB (schema), STK_CM (governance)
