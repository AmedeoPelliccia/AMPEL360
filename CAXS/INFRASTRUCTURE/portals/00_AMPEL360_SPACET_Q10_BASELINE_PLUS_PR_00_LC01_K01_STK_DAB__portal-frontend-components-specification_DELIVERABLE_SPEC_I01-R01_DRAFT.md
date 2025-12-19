# Portal Frontend Components Specification

**CA360º Portal — MUST Features Implementation Guide**

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

This document specifies the implementation requirements for the **MUST features (F01-F09)** of the CA360º Portal. These features are non-negotiable for a release-grade AoR portal.

---

## 2. Component Catalog

### F01 — Context Bar (Slice Selector)

**Component Type:** UI Widget (Persistent Header)

**Description:**  
A persistent UI component that displays and allows selection of the current operational context.

**Required Elements:**
- Program/Family/Variant/Version selector dropdown
- OPT-INS node selector (Axis/ATA/Block)
- LC phase selector
- Active KNOT selector
- Current context display badge

**State Management:**
- Context stored in session state
- Context changes broadcast to all components
- Context persisted across page navigation

**API Integration:**
- `GET /api/portal/context` — Get current context
- `POST /api/portal/context` — Update context
- `GET /api/portal/context/options` — Get available options

**UI Requirements:**
- Fixed position (top of page)
- Always visible
- Context changes reflected within 500ms
- Dropdown autocomplete/search for quick navigation

**Example Structure:**
```jsx
<ContextBar>
  <SliceSelector>
    <ProgramSelector value="SPACET" />
    <FamilySelector value="Q10" />
    <VariantSelector value="BASELINE" />
    <VersionSelector value="PLUS" />
  </SliceSelector>
  <NodeSelector value="ATA-53" />
  <PhaseSelector value="LC03" />
  <KnotSelector value="K03" />
  <ContextBadge compact />
</ContextBar>
```

---

### F02 — AoR Dashboard (Default Filters + KPIs)

**Component Type:** Dashboard View

**Description:**  
A landing screen showing "what I must do now" with role-specific KPIs.

**Required Elements:**
- KPI cards (4-6 cards per AoR)
- Default filters applied automatically
- Quick navigation to critical items
- Refresh indicator

**State Management:**
- Dashboard state synced with context
- Auto-refresh every 5 minutes (configurable)
- Manual refresh button

**API Integration:**
- `GET /api/portal/dashboard?aor={aor}` — Get dashboard data
- `GET /api/portal/kpis?aor={aor}` — Get KPI values

**KPI Card Format:**
```jsx
<KPICard
  id="open_tasks"
  label="Open Tasks"
  value={42}
  trend="+5"
  onClick={() => navigate('/work-queue?status=open')}
/>
```

**Performance Requirements:**
- Dashboard loads within 2 seconds
- KPIs update with <5 minute lag
- Clicking KPI navigates to detailed view

---

### F03 — Registry-Driven Work Queue

**Component Type:** List View

**Description:**  
Work items automatically derived from SSOT registries (gaps, pending signoffs, missing evidence).

**Required Elements:**
- Filterable/sortable work item list
- Link to source registry entry
- Priority indicator
- Status badge
- Assignee avatar
- Due date indicator

**State Management:**
- Work queue synced with registries
- Real-time updates when registries change

**API Integration:**
- `GET /api/portal/work-queue?aor={aor}&filters=...` — Get work items
- `POST /api/portal/work-queue/item/{id}/resolve` — Mark item resolved

**Work Item Format:**
```jsx
<WorkItem
  id="WI-12345"
  title="Complete thermal analysis for ATA-53"
  priority="HIGH"
  status="OPEN"
  assignee="user@ampel360.org"
  dueDate="2025-12-25"
  sourceRegistry="task_registry.md#L123"
  onClick={() => navigate('/task/12345')}
/>
```

---

### F04 — Kanban / Backlog Mapped to KNOTs

**Component Type:** Kanban Board

**Description:**  
Visual task management board with columns mapped to KNOT stages.

**Required Elements:**
- Columns (5-7 columns per AoR)
- Cards (tasks with metadata)
- Drag-and-drop support
- Filters (by AoR, KNOT, assignee, due date)
- Board state persistence

**State Management:**
- Board state synchronized across users
- Drag events update underlying registry
- Optimistic UI updates

**API Integration:**
- `GET /api/portal/kanban?aor={aor}` — Get board state
- `POST /api/portal/kanban/move` — Move card
- `POST /api/portal/kanban/create` — Create card

**Board Structure:**
```jsx
<KanbanBoard>
  <Column label="Backlog" knotStages={["K01"]} />
  <Column label="Requirements" knotStages={["K02"]} />
  <Column label="Design" knotStages={["K03"]} />
  <Column label="Analysis" knotStages={["K04"]} />
  <Column label="Integration" knotStages={["K05"]} />
  <Column label="Verification" knotStages={["K06"]} />
  <Column label="Complete" knotStages={["K07"]} />
</KanbanBoard>
```

**Performance Requirements:**
- Board loads within 3 seconds
- Drag-and-drop feels responsive (<100ms latency)

---

### F05 — Artifact Generator (Template Wizard)

**Component Type:** Multi-Step Form Wizard

**Description:**  
Create governed artifacts from approved templates with guided workflows.

**Required Elements:**
- Template selector
- Step-by-step wizard
- Auto-populated metadata fields
- Validation feedback
- Preview before creation
- v6.0 nomenclature enforcement

**State Management:**
- Wizard state saved (can resume later)
- Draft artifacts stored temporarily

**API Integration:**
- `GET /api/portal/templates?aor={aor}` — Get templates
- `POST /api/portal/artifacts/generate` — Generate artifact
- `POST /api/portal/artifacts/validate` — Validate artifact

**Wizard Flow:**
```jsx
<ArtifactWizard>
  <Step1_SelectTemplate />
  <Step2_FillMetadata />
  <Step3_AddContent />
  <Step4_Validate />
  <Step5_Preview />
  <Step6_Create />
</ArtifactWizard>
```

---

### F06 — Gates & Validator Console

**Component Type:** Status Dashboard

**Description:**  
Run and view CI gates relevant to the AoR; show failing checks, required evidence, responsible parties.

**Required Elements:**
- Gate status per node/KNOT
- Failing checks with error details
- Link to required evidence
- Responsible party indicators
- Re-run button
- Gate history/timeline

**API Integration:**
- `GET /api/portal/gates?aor={aor}&node={node}` — Get gate status
- `POST /api/portal/gates/rerun` — Trigger gate re-run
- `GET /api/portal/gates/{gateId}/logs` — Get gate logs

**Gate Status Display:**
```jsx
<GateConsole>
  <GateStatus
    gate="nomenclature-validator"
    status="PASS"
    lastRun="2025-12-19T22:00:00Z"
  />
  <GateStatus
    gate="evidence-link-validator"
    status="FAIL"
    lastRun="2025-12-19T22:05:00Z"
    errors={[
      "Evidence file not found: exports/test-report-001.pdf",
      "Broken link: CAXS/missing-file.md"
    ]}
    requiredEvidence={["exports/test-report-001.pdf"]}
    responsibleParty="STK_TEST"
  />
</GateConsole>
```

---

### F07 — Evidence Console (Index + Attach + Hash)

**Component Type:** File Manager / Index Browser

**Description:**  
Browse, attach, export, and verify integrity of evidence artifacts.

**Required Elements:**
- Evidence index browser (tree view)
- File upload/attach interface
- Hash computation display (sha256)
- Export package creator
- Search/filter capabilities

**API Integration:**
- `GET /api/portal/evidence?aor={aor}` — Get evidence index
- `POST /api/portal/evidence/attach` — Attach evidence
- `POST /api/portal/evidence/export` — Export evidence package
- `GET /api/portal/evidence/{id}/hash` — Get file hash

**Evidence Item Display:**
```jsx
<EvidenceItem
  id="EVD-12345"
  filename="thermal-analysis-report.pdf"
  hash="sha256:abc123...xyz789"
  uploadedBy="user@ampel360.org"
  uploadedAt="2025-12-19T22:00:00Z"
  linkedTo={["TASK-001", "REQ-042"]}
/>
```

---

### F08 — Signoff Console

**Component Type:** Approval Dashboard

**Description:**  
View signoff requests, route to appropriate AoRs, capture decisions and minutes.

**Required Elements:**
- Pending signoff list
- Signoff routing rules
- Decision capture form
- Minutes capture form
- Signoff history
- Immutable signoff records

**API Integration:**
- `GET /api/portal/signoffs?aor={aor}` — Get signoffs
- `POST /api/portal/signoffs/create` — Create signoff request
- `POST /api/portal/signoffs/{id}/approve` — Approve signoff
- `POST /api/portal/signoffs/{id}/reject` — Reject signoff

**Signoff Request Display:**
```jsx
<SignoffRequest
  id="SIGN-12345"
  type="thermal-approval"
  artifact="thermal-analysis-report.pdf"
  requestedBy="user1@ampel360.org"
  requestedAt="2025-12-19T20:00:00Z"
  targetAor="STK_PHM"
  status="PENDING"
  onApprove={() => handleApprove()}
  onReject={() => handleReject()}
/>
```

---

### F09 — Tool Launchpad (TALF-aware)

**Component Type:** Tool Grid / Tile View

**Description:**  
Tool tiles with preflight checks for SSO, entitlements, licenses, and compute profiles.

**Required Elements:**
- Tool tiles (grid layout)
- Preflight status indicators
- Launch button (enabled/disabled)
- License availability indicator
- Entitlement status badge
- Failure mode messaging

**State Management:**
- Tool status polled periodically
- Preflight checks run on-demand

**API Integration:**
- `GET /api/portal/tools?aor={aor}` — Get tool tiles
- `POST /api/talf/v1/preflight` — Run preflight checks
- `POST /api/talf/v1/launch` — Launch tool

**Tool Tile Display:**
```jsx
<ToolTile
  toolId="ansys-fluent-2024"
  displayName="ANSYS Fluent"
  toolClass="cfd"
  ownerAor="STK_PHM"
  preflightStatus={{
    sso_session: "PASS",
    entitlement: "PASS",
    license: "PASS",
    compute_profile: "PASS"
  }}
  launchEnabled={true}
  onLaunch={() => handleLaunch()}
/>
```

**Failure Mode Display:**
```jsx
<ToolTile
  toolId="ansys-fluent-2024"
  displayName="ANSYS Fluent"
  preflightStatus={{
    license: "FAIL"
  }}
  launchEnabled={false}
  failureMessage="All licenses in use. You are #3 in queue."
  queueEstimate="PT15M"
/>
```

---

## 3. Technology Stack

### 3.1 Frontend Framework

**Recommended:** React 18+ or Vue 3+

**Rationale:**
- Component-based architecture
- Strong ecosystem
- Good performance
- Wide adoption

### 3.2 State Management

**Recommended:** React Context + Zustand or Vuex

**Rationale:**
- Lightweight
- Easy to learn
- Good for medium-complexity apps

### 3.3 UI Component Library

**Recommended:** Material-UI, Ant Design, or Chakra UI

**Rationale:**
- Pre-built components
- Accessibility built-in
- Customizable theming

### 3.4 Data Fetching

**Recommended:** React Query or SWR

**Rationale:**
- Caching
- Auto-refresh
- Optimistic updates
- Error handling

---

## 4. Implementation Checklist

- [ ] **F01 — Context Bar**
  - [ ] Component implementation
  - [ ] State management
  - [ ] API integration
  - [ ] Unit tests
  - [ ] Integration tests
  
- [ ] **F02 — AoR Dashboard**
  - [ ] Component implementation
  - [ ] KPI cards
  - [ ] Auto-refresh
  - [ ] Unit tests
  
- [ ] **F03 — Registry-Driven Work Queue**
  - [ ] Component implementation
  - [ ] Filter/sort logic
  - [ ] Registry sync
  - [ ] Unit tests
  
- [ ] **F04 — Kanban / Backlog**
  - [ ] Component implementation
  - [ ] Drag-and-drop
  - [ ] State sync
  - [ ] Unit tests
  
- [ ] **F05 — Artifact Generator**
  - [ ] Wizard implementation
  - [ ] Template engine
  - [ ] Validation
  - [ ] Unit tests
  
- [ ] **F06 — Gates & Validator Console**
  - [ ] Component implementation
  - [ ] Gate status polling
  - [ ] Error display
  - [ ] Unit tests
  
- [ ] **F07 — Evidence Console**
  - [ ] Component implementation
  - [ ] File upload
  - [ ] Hash computation
  - [ ] Unit tests
  
- [ ] **F08 — Signoff Console**
  - [ ] Component implementation
  - [ ] Decision capture
  - [ ] Routing logic
  - [ ] Unit tests
  
- [ ] **F09 — Tool Launchpad**
  - [ ] Component implementation
  - [ ] Preflight integration
  - [ ] Launch orchestration
  - [ ] Unit tests

---

## 5. References

- **Portal Feature Catalog:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__portal-feature-catalog_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **TALF Service Specification:** `CAXS/INFRASTRUCTURE/portals/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__talf-service-specification_DELIVERABLE_SPEC_I01-R01_DRAFT.md`

---

**END OF DOCUMENT**
