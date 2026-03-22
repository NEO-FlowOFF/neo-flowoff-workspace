# NEO-FlowOFF Unified Roadmap 2026

Project URL: https://github.com/orgs/NEO-FlowOFF/projects/1

## Scope

- Organization: `NEO-FlowOFF`
- Workspace root: `/Users/nettomello/neomello/NEO-FlowOFF`
- Date format: `YYYY-MM-DD`
- Structure: repository, milestone, dependencies, execution order, proposed start date, proposed target date

## Milestones

### 1. NEO-FlowOFF/org

- Milestone: `M0 Board Bootstrap`
- Dependencies: `None`
- Proposed Start Date: `2026-03-16`
- Proposed Target Date: `2026-03-17`
- Tasks:
  - Create organization GitHub Project
  - Create custom roadmap fields
  - Import roadmap items as draft issues

### 2. neoflw-token

- Milestone: `M1 Canonical Token Path`
- Dependencies: `M0 Board Bootstrap`
- Proposed Start Date: `2026-03-16`
- Proposed Target Date: `2026-03-20`
- Tasks:
  - Choose canonical token network
  - Retire non-canonical documentation branches
  - Generate single deployment manifest
  - Normalize addresses consumed by PWA and miniapp

### 3. neoflw-token

- Milestone: `M2 On-chain Readiness`
- Dependencies: `M1 Canonical Token Path`
- Proposed Start Date: `2026-03-23`
- Proposed Target Date: `2026-03-31`
- Tasks:
  - Verify contracts in canonical explorer
  - Fund `StakingVault`
  - Decide `GamificationController` go-live
  - Consolidate liquidity and token distribution operations

### 4. neo-flowoff-pwa

- Milestone: `M3 Real Integrations Core`
- Dependencies: `M1 Canonical Token Path`
- Proposed Start Date: `2026-03-23`
- Proposed Target Date: `2026-04-03`
- Tasks:
  - Replace MCP router mocks with real integrations
  - Implement real EIP-712 verification
  - Integrate real FlowPay client
  - Persist fallback and logs to decentralized stack

### 5. neo-flowoff-pwa

- Milestone: `M4 UI Hardening`
- Dependencies: `M3 Real Integrations Core`
- Proposed Start Date: `2026-03-30`
- Proposed Target Date: `2026-04-10`
- Tasks:
  - Complete Fase 5 tests
  - Complete Fase 6 documentation
  - Validate compatibility with legacy loaders
  - Confirm build and test stability

### 6. neo-flowoff-pwa

- Milestone: `M5 Product Modules Wave 1`
- Dependencies: `M3 Real Integrations Core`
- Proposed Start Date: `2026-04-06`
- Proposed Target Date: `2026-04-17`
- Tasks:
  - Implement `WOD[X]PRO` real module
  - Implement `FLUXX` real module
  - Add MCP intents
  - Connect frontend cards to real backends
  - Publish minimal module docs

### 7. neo-flowoff-pwa

- Milestone: `M6 Product Modules Wave 2`
- Dependencies: `M5 Product Modules Wave 1`
- Proposed Start Date: `2026-04-20`
- Proposed Target Date: `2026-05-01`
- Tasks:
  - Implement `RUN NEØ` module
  - Implement `NEØ SMART FACTORY` module
  - Add navigation and dedicated pages
  - Connect both modules to backend capabilities

### 8. ceo-escalavel-miniapp

- Milestone: `M7 Wallet Referral and Metrics`
- Dependencies: `M1 Canonical Token Path`
- Proposed Start Date: `2026-03-30`
- Proposed Target Date: `2026-04-10`
- Tasks:
  - Set production `VITE_REOWN_PROJECT_ID`
  - Implement `start_param` tracking
  - Create trackable referral rewards
  - Fix premium store copy
  - Add conversion metrics dashboard

### 9. ceo-escalavel-miniapp

- Milestone: `M8 Token Utility and Retention`
- Dependencies: `M2 On-chain Readiness`, `M7 Wallet Referral and Metrics`
- Proposed Start Date: `2026-04-13`
- Proposed Target Date: `2026-04-24`
- Tasks:
  - Enable real wallet connect
  - Implement mint or airdrop flow aligned to canonical token
  - Add bot notifications
  - Add leaderboard and daily tasks
  - Test maturity-based paywalls

### 10. neo-flw-landing

- Milestone: `M9 Conversion Infrastructure`
- Dependencies: `M0 Board Bootstrap`
- Proposed Start Date: `2026-04-06`
- Proposed Target Date: `2026-04-17`
- Tasks:
  - Implement public `/api/health` endpoint
  - Add Meta Pixel client-side base events
  - Add Meta CAPI server-side high-value events
  - Add low-latency operations callback
  - Decide stealth middleware now or later

### 11. neoflow-content-machine

- Milestone: `M10 Reliability Hardening`
- Dependencies: `M0 Board Bootstrap`
- Proposed Start Date: `2026-03-23`
- Proposed Target Date: `2026-04-10`
- Tasks:
  - Migrate `console.log` to logger
  - Expand critical test coverage
  - Complete Instagram, LinkedIn, Farcaster and Blog distributors
  - Publish API documentation

### 12. neoflow-content-machine

- Milestone: `M11 Launch Content Execution`
- Dependencies: `M9 Conversion Infrastructure`, `M10 Reliability Hardening`
- Proposed Start Date: `2026-04-13`
- Proposed Target Date: `2026-04-24`
- Tasks:
  - Promote FlowOFF launch assets from planned to approved pipeline
  - Produce launch sequence
  - Validate distribution by channel
  - Prepare scheduled posting

### 13. pro-ia

- Milestone: `M12 Funnel Automation`
- Dependencies: `M0 Board Bootstrap`
- Proposed Start Date: `2026-04-20`
- Proposed Target Date: `2026-05-08`
- Tasks:
  - Choose CRM and marketing automation stack
  - Automate form to payment to portal access flow
  - Create non-conversion follow-up
  - Centralize lead scoring and dashboards

### 14. pro-ia

- Milestone: `M13 Content and Analytics Closure`
- Dependencies: `M12 Funnel Automation`
- Proposed Start Date: `2026-05-11`
- Proposed Target Date: `2026-05-22`
- Tasks:
  - Finish pending blog CTA and checklist blocks
  - Complete Post 3 draft
  - Instrument weekly conversion, retention and productivity metrics
