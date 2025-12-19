# Portal Feature Catalog (SSOT)

**AMPEL360 CA360º Portal — Canonical Feature Registry**

---

## Metadata

- **ATA:** 00 (GENERAL)
- **Program:** SPACET Q10 BASELINE PLUS
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_DAB (Digital Applications & Blockchains)
- **Category:** REGISTRY
- **Type:** CAT (Catalog)
- **Status:** ACTIVE
- **Issue-Revision:** I01-R01

---

## Purpose

This document is the **Single Source of Truth (SSOT)** for all AoR portal features in the AMPEL360 CA360º ecosystem. Each feature is assigned a unique identifier (F-01 through F-20) and classified according to MoSCoW prioritization (MUST, SHOULD, COULD, WON'T).

Every AoR portal contract must reference this catalog when declaring enabled features.

---

## Feature Catalog

### MUST Features (Non-negotiable for release-grade AoR portal)

#### F01 — Context Bar (Slice Selector)

**Description:**  
A persistent UI component that displays and allows selection of the current operational context.

**Capabilities:**
- Select PROGRAM / FAMILY / VARIANT / VERSION
- Select OPT-INS node (AXIS / ATA / BLOCK)
- Select LC phase
- Select active KNOT

**Acceptance Criteria:**
- Every view shows current context
- Every artifact and action binds to the selected context
- Context changes are reflected across all portal surfaces within 500ms

**Dependencies:**
- Backend: Context resolution service
- Frontend: Context bar component

---

#### F02 — AoR Dashboard (Default Filters + KPIs)

**Description:**  
A single landing screen showing "what I must do now" with role-specific KPIs.

**Capabilities:**
- Display open tasks count
- Display pending signoffs count
- Display evidence gaps count
- Display gate blockers count
- Apply default filters per AoR contract
- Quick navigation to critical items

**Acceptance Criteria:**
- Dashboard loads within 2 seconds
- KPIs are updated in real-time (or with <5 minute lag)
- Clicking a KPI navigates to the corresponding detailed view

**Dependencies:**
- Backend: Registry aggregation service, KPI computation engine
- Frontend: Dashboard component, KPI widgets

---

#### F03 — Registry-Driven Work Queue

**Description:**  
Work items are automatically derived from SSOT registries (gaps, pending signoffs, missing evidence), not manually curated.

**Capabilities:**
- Auto-generate work items from registry analysis
- Link each work item to the source registry entry
- Prioritize items by urgency and dependencies
- Filter and sort by multiple dimensions

**Acceptance Criteria:**
- Queue items link to SSOT registry line that produced them
- Adding/removing registry entries automatically updates queue
- Work item resolution updates the underlying registry

**Dependencies:**
- Backend: Registry scanner, work item generator
- Frontend: Work queue component

---

#### F04 — Kanban / Backlog Mapped to KNOTs

**Description:**  
Visual task management board with columns mapped to KNOT stages.

**Capabilities:**
- Columns = KNOT stages (or KNOT groups)
- Cards = tasks (Kxx-T###) with STATUS
- Drag-and-drop to update task status
- Filter by AoR, KNOT, assignee, due date

**Acceptance Criteria:**
- Moving a card updates the underlying registry entry (or creates a delta PR)
- Board state is persisted and synchronized across users
- Board loads within 3 seconds

**Dependencies:**
- Backend: Task registry, state update service
- Frontend: Kanban board component

---

#### F05 — Artifact Generator (Template Wizard)

**Description:**  
Create governed artifacts from approved templates with guided workflows.

**Capabilities:**
- Generate ONUP packs from templates
- Generate evidence packs from templates
- Create signoff index entries
- Auto-populate metadata from context
- Validate outputs against v6.0 nomenclature

**Acceptance Criteria:**
- Outputs are v6.0 compliant
- Artifacts automatically backlink to requirements and context
- Templates are versioned and approved

**Dependencies:**
- Backend: Template registry, artifact generation service, validator
- Frontend: Wizard UI component

---

#### F06 — Gates & Validator Console

**Description:**  
Run and view CI gates relevant to the AoR; show failing checks, required evidence, and responsible parties.

**Capabilities:**
- Display gate status per node and per KNOT
- Show failing checks with detailed error messages
- Link to required evidence
- Identify who must sign off
- Trigger gate re-runs

**Acceptance Criteria:**
- Gate status is visible per node and per KNOT
- Status updates within 1 minute of gate completion
- Failed gates block progression with clear messaging

**Dependencies:**
- Backend: CI/CD bridge, gate execution service, validator service
- Frontend: Gate console component

---

#### F07 — Evidence Console (Index + Attach + Hash)

**Description:**  
Browse, attach, export, and verify integrity of evidence artifacts.

**Capabilities:**
- Browse evidence index by AoR, KNOT, LC phase
- Attach new evidence with metadata
- Export evidence packages
- Compute and record integrity hashes (sha256)
- Create snapshots for audit

**Acceptance Criteria:**
- Evidence artifacts are linkable into LC06 packs
- All evidence has computed sha256 hash
- Evidence can be filtered and searched efficiently

**Dependencies:**
- Backend: Evidence index service, hash computation service, storage
- Frontend: Evidence console component

---

#### F08 — Signoff Console

**Description:**  
View signoff requests, route to appropriate AoRs, capture decisions and minutes.

**Capabilities:**
- Display pending signoff requests
- Route signoffs to correct AoR roles
- Capture decision records (DEC)
- Capture minutes (MIN)
- Link signoffs to gates and evidence

**Acceptance Criteria:**
- No gate closes without required signoffs present in index
- Signoff records are immutable and auditable
- Signoff status is visible in gate console

**Dependencies:**
- Backend: Signoff index, routing service, decision capture service
- Frontend: Signoff console component

---

#### F09 — Tool Launchpad (TALF-aware)

**Description:**  
Tool tiles with preflight checks for SSO, entitlements, licenses, and compute profiles.

**Capabilities:**
- Display available tools per AoR
- Perform preflight checks before launch
- Check SSO session validity
- Check entitlement groups
- Check license availability
- Check compute profile readiness
- Block task start if tooling not available
- Record audit events (launch, checkout, export)

**Acceptance Criteria:**
- "Start Task" can be blocked with auditable reason if tooling is not available
- Tool launch is logged for audit
- License checkout/return is tracked

**Dependencies:**
- Backend: TALF service (Tool Access & Licensing Fabric), entitlement service, audit log
- Frontend: Tool launchpad component

---

### SHOULD Features (Strongly recommended for scale and audit defensibility)

#### F10 — Portal-aware AI Assistant (Governance-bounded)

**Description:**  
AI assistant constrained by governance rules to help with artifact drafting and task decomposition.

**Capabilities (Allowed):**
- Draft artifacts using templates and current context (slice + AoR + node)
- Propose task breakdown (URB)
- Propose impact matrix rows
- Propose RACI assignments
- Suggest evidence required for gates
- Identify missing links in traceability

**Constraints (Mandatory):**
- Cannot bypass gates
- Cannot invent AoRs or tools
- Every generated item cites its source context
- All suggestions link to SSOT registries

**Acceptance Criteria:**
- Assistant responses include citations to SSOT
- Assistant cannot create or modify released artifacts
- All actions are logged for audit

**Dependencies:**
- Backend: AI service with governance constraints, SSOT access, audit log
- Frontend: Assistant panel component

---

#### F11 — Integrated Communication Threads

**Description:**  
Discussion threads bound to nodes, tasks, and signoffs with decision extraction.

**Capabilities:**
- Create threads bound to: node, task, signoff, decision
- Extract decisions into DEC records
- Extract minutes into MIN records
- Link threads to artifacts
- Notify participants of updates

**Acceptance Criteria:**
- Every decision affecting baselines becomes a governed decision record
- Threads are searchable and auditable
- Thread history is immutable

**Dependencies:**
- Backend: Thread service, decision extraction service, notification service
- Frontend: Communication panel component

---

#### F12 — Cross-AoR Handshake Panel

**Description:**  
Display interfaces owed to and by this AoR with status and triggers.

**Capabilities:**
- Show "interfaces I owe" with deadlines
- Show "interfaces owed to me" with status
- Display REQ ↔ ICD ↔ Evidence chains
- Trigger notifications on interface updates
- Track validation status by owning and validating AoR

**Acceptance Criteria:**
- Interface objects have an owner AoR and a validation AoR
- Status updates are reflected within 5 minutes
- Overdue interfaces are highlighted

**Dependencies:**
- Backend: Interface registry, cross-AoR notification service
- Frontend: Handshake panel component

---

#### F13 — Trace & Impact Viewer

**Description:**  
Visualize requirements trace, ATA impact matrix, and evidence-to-objective mapping.

**Capabilities:**
- Display requirements trace graph
- Display ATA impact matrix coupling
- Display evidence-to-objective mapping
- Interactive graph navigation
- Export trace reports

**Acceptance Criteria:**
- Click-through from any requirement/objective → evidence → signoff
- Graph renders within 5 seconds for up to 10,000 nodes
- Trace completeness metrics are displayed

**Dependencies:**
- Backend: Traceability graph service (ATA 93)
- Frontend: Trace viewer component (graph visualization)

---

#### F14 — Notification Engine

**Description:**  
Notify users of gate failures, signoff requests, license issues, and blockers.

**Capabilities:**
- Notify on gate failures
- Notify on signoff requests
- Notify on license checkout failures (TALF)
- Notify on new blockers
- Configurable notification channels (email, portal, webhook)
- Subscription management

**Acceptance Criteria:**
- Critical notifications delivered within 1 minute
- Users can configure notification preferences
- Notifications are logged for audit

**Dependencies:**
- Backend: Notification service, event bus, subscription manager
- Frontend: Notification settings UI

---

### COULD Features (Valuable, but not required for first production release)

#### F15 — "Start Task" Execution Runner

**Description:**  
Guided flow for task execution from preflight through delivery.

**Capabilities:**
- Run preflight checks
- Open required tools
- Mount workspace (repo node, datasets, templates)
- Generate outputs
- Update registries
- Close task with evidence

**Acceptance Criteria:**
- Task execution is logged end-to-end
- Failed preflight blocks execution
- Outputs are automatically validated

**Dependencies:**
- Backend: Task runner service, workspace provisioning service
- Frontend: Execution runner UI

---

#### F16 — Integrated Meeting Capture

**Description:**  
Convert recorded reviews into structured artifacts.

**Capabilities:**
- Record review sessions
- Extract minutes automatically
- Extract decisions automatically
- Extract action items automatically
- Link action items to tasks

**Acceptance Criteria:**
- Extracted decisions are valid DEC records
- Extracted action items create tasks in registry
- Recordings are stored securely

**Dependencies:**
- Backend: Meeting capture service, NLP extraction service
- Frontend: Meeting capture UI

---

#### F17 — Comparative Dashboards

**Description:**  
Compare variants/versions across KPIs.

**Capabilities:**
- Compare variants across KPIs
- Compare versions across KPIs
- Domain-specific comparisons (e.g., PHM: thermal margins, CERT: closure rate, AI: regression rate)
- Export comparison reports

**Acceptance Criteria:**
- Comparisons update when underlying data changes
- Reports are exportable in multiple formats

**Dependencies:**
- Backend: KPI aggregation service, comparison engine
- Frontend: Comparative dashboard component

---

#### F18 — Offline/Edge Mode

**Description:**  
Limited capability when disconnected with deferred synchronization.

**Capabilities:**
- Cache current context and recent artifacts
- Allow read-only access offline
- Allow evidence export with deferred upload
- Strict audit trail for offline actions
- Auto-sync when reconnected

**Acceptance Criteria:**
- All offline actions are logged with timestamps
- Sync conflicts are detected and resolved
- Offline mode is explicitly indicated in UI

**Dependencies:**
- Backend: Sync service, conflict resolution service
- Frontend: Offline cache, sync UI

---

### WON'T Features (Explicitly excluded to protect scope and certification posture)

#### F19 — Auto-merge / Auto-signoff

**Description:**  
Portal must NOT autonomously close gates or sign decisions.

**Rationale:**  
Autonomous approval would bypass human-in-the-loop governance required for certification and audit defensibility.

**Policy:**  
All gate closures and signoffs must be explicitly authorized by qualified personnel.

---

#### F20 — Unbounded external chatbots / uncontrolled tool plugins

**Description:**  
All assistants and tools must be cataloged, permissioned, and auditable.

**Rationale:**  
Uncontrolled external integrations introduce security, compliance, and traceability risks.

**Policy:**  
- All tools must be registered in the tool access registry
- All assistants must operate within governance constraints (see F10)
- No direct access to external AI services without approval

---

## Governance

### Feature Addition Process

1. Propose new feature with ID (F-21+)
2. Define capabilities, acceptance criteria, dependencies
3. Classify as MUST / SHOULD / COULD / WON'T
4. Submit for review by STK_DAB and STK_CM
5. Upon approval, add to this catalog
6. Update all affected AoR contracts

### Feature Modification Process

1. Propose change to existing feature
2. Impact analysis on all AoR contracts referencing the feature
3. Submit for review by STK_DAB and STK_CM
4. Upon approval, update catalog with new revision
5. Notify all affected AoRs

### Version Control

- Major version increment: Adding/removing MUST features
- Minor version increment: Adding/removing SHOULD/COULD features
- Patch version increment: Clarifications, acceptance criteria updates

---

## Change Log

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| I01-R01 | 2025-12-19 | STK_DAB | Initial catalog with F01-F20 |

---

## References

- **AoR Portal Contract Schema:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__aor-portal-contract-schema_DELIVERABLE_SCHEMA_I01-R01_ACTIVE.md`
- **Tool Launchpad Specification:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__tool-launchpad-specification_DELIVERABLE_SPEC_I01-R01_ACTIVE.md`
- **CA360º Portal RC Protocol:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal-rc-protocol_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

---

**END OF DOCUMENT**
