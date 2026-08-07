# PRD Template

Adapt depth to product complexity. Do not fill sections with generic prose; write `Not applicable` with a reason when necessary.

At the top of every PRD, state:

- **Artifact maturity**: `Snapshot`, `Draft`, or `Implementation-ready`
- **Coverage**: which discussion, evidence, repository state, and product planes are included
- **Known gaps**: missing decisions or evidence that prevent the next maturity level
- **Collaboration model**: `Dynamic council` or `Lead-PM collaboration`, including the Lead PM lens when selected
- **Lens naming**: use aliases only in user-facing text

When the user requests a PRD before discovery is complete, produce it immediately. Write `Pending` with a reason for unavailable sections instead of delaying output or inventing content.

## 1. Product Decision Summary

- One-sentence product definition
- Primary user and situation
- Current alternative
- Product promise
- Primary success metric
- Recommended decision
- Lead PM lens and integration responsibility when selected

## 2. Negative Boundary

### Must not

### Not now

### Hard constraints

### Protected qualities

For each item, state which downstream decisions and acceptance checks it constrains.

## 3. Background And Evidence

- Problem evidence
- User evidence
- Business or organizational context
- Repository and existing-product constraints

| Statement | Type: fact, user statement, assumption, inference, or recommendation | Source | Confidence | Validation status |
|---|---|---|---|---|

For high-impact assumptions, include the cheapest validation plan and whether the user authorized external research, competitor inspection, or prototype execution.

## 4. Strategy Plane

- Primary and excluded users
- User need and desired progress
- Product objective
- Value creation and exchange
- Success and guardrail metrics
- Strategic risks and validation plan
- Selected lens proposals, conflicts, and decision

## 5. Scope Plane

### Must ship

For each requirement: user need, behavior, business rule, acceptance boundary, and metric contribution.

### Later

### Not doing

### Content and data requirements

Include selected lens proposals, conflicts, and the reason each accepted or rejected recommendation changed scope.

## 6. Structure Plane

- Product objects and relationships
- Primary user flow
- Secondary flows
- States and transitions
- Empty, error, permission, interruption, and recovery paths
- Information architecture
- Selected lens proposals, conflicts, and decision

## 7. Framework Plane (Skeleton)

- Screen or surface inventory
- Navigation model
- Per-screen purpose, information priority, controls, and next action
- Interaction annotations
- Positive references, negative references, and rejected generic patterns when relevant
- Selected lens proposals, conflicts, and decision

## 8. Surface Plane

- Product character
- Visual and content hierarchy
- Voice and terminology
- Feedback behavior
- Accessibility and sensory constraints
- Positive references, negative references, and forbidden expressions of the product character
- Selected lens proposals, conflicts, and decision

## 9. Decision Constraint Chain

| Upstream decision or boundary | Scope rule | Structure behavior | Framework or surface constraint | Implementation acceptance check |
|---|---|---|---|---|

Mark unresolved product questions explicitly. An AI coding agent must not silently choose an answer.

## 10. Measurement And Learning

- Primary metric
- Leading indicators
- Guardrail metrics
- Events or data required
- Experiment or rollout plan
- Review date and decision threshold

## 11. Delivery

- Dependencies
- Technical or policy constraints
- Milestones
- Release and rollback approach
- Owners when known
- AI coding agent handoff instructions and stop conditions

## 12. Product-Lens Deliberation And Decision Log

For every major decision, preserve the independent advice before synthesis:

| Decision question | Collaboration role | Lens and principle IDs | Reframe | Concrete proposal | Challenge or refusal | Evidence needed | Downstream change |
|---|---|---|---|---|---|---|---|

Then record:

- agreements and disagreements;
- accepted recommendation and reason;
- rejected recommendation and reason;
- final decision and revisit trigger.

## 13. Risks And Open Questions

Separate unresolved questions, assumptions requiring validation, and accepted risks.
