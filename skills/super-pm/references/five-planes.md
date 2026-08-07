# Five-Plane Product Workflow

Use Jesse James Garrett's five planes as a dependency model, not five parallel brainstorming buckets. The Negative Boundary precedes the planes and constrains all of them.

Framework basis: Jesse James Garrett, *The Elements of User Experience*, Chapter 2 - http://www.jjg.net/elements/pdf/elements_ch02.pdf

## Dependency Model

`Negative Boundary -> Strategy -> Scope -> Structure -> Framework (Skeleton) -> Surface`

When writing in Chinese, use `战略层、范围层、结构层、框架层、表现层`. Use `框架层（Skeleton Plane）` only on first mention when clarification helps; do not translate it as `骨架层`.

A lower-plane decision may reveal a higher-plane defect. When that happens, return to the earliest inconsistent plane, revise it, and propagate the change downward.

## Decision Constraint Chain

Carry each accepted user boundary and product decision downstream rather than restating it as a vague design adjective:

`User statement or evidence -> Negative Boundary -> strategy decision -> scope rule -> structure behavior -> framework constraint -> surface behavior -> acceptance check`

Assign stable decision IDs when the chain is long enough to lose traceability. Do not let a downstream implementation invent a missing upstream rule; record it as an unresolved decision.

## Preflight: Negative Boundary

Clarify:

- `must not`: unacceptable users, outcomes, behaviors, risks, or product qualities.
- `not now`: useful ideas intentionally deferred.
- `hard constraints`: time, cost, technology, channel, policy, and organizational limits.
- `protected qualities`: what the solution must preserve even under pressure.

Exit when the user can reject a polished but wrong solution using these boundaries.

## 1. Strategy Plane

Answer:

- Who is the primary user in a specific situation?
- What progress are they trying to make?
- What do they use or do today?
- Why is the problem worth solving now?
- What value will the product create for the user and the organization?
- Which observable result would prove the bet?

Produce:

- Primary user and excluded users.
- Core situation, problem, current alternative, and switching barrier.
- Product promise and product objective.
- One primary success metric plus guardrail metrics.
- Strategic assumptions and cheapest validation.

Exit when the proposed product can be described without naming features.

## 2. Scope Plane

Answer:

- Which capabilities are necessary to deliver the product promise?
- Which content or data is required?
- Which requirement is merely a familiar implementation pattern?
- What is the smallest coherent release that tests the strategy?

Produce:

- Functional requirements and content requirements.
- `must`, `later`, and `not doing` lists.
- Acceptance boundaries and major business rules.
- Traceability from each `must` item to strategy.

Exit when removing any remaining `must` item breaks the strategic promise, and adding a `later` item is unnecessary to test it.

## 3. Structure Plane

Answer:

- What is the user's mental model and task sequence?
- How does the system respond to each meaningful action?
- How is information grouped, labeled, and connected?
- Where can the user fail, abandon, recover, or change direction?

Produce:

- Primary and secondary user flows.
- State model and decision points.
- Information architecture and object relationships.
- Error, empty, permission, interruption, and recovery paths where relevant.

Exit when every scoped requirement has a place in a flow or information structure and no interface layout is needed to explain the logic.

## 4. Framework Plane (Skeleton)

Answer:

- Which information and controls belong on each screen or surface?
- What must be visible, nearby, persistent, or progressive?
- How does the user know where they are and what happens next?
- Which control is the primary action and which options should remain hidden?

Produce:

- Screen inventory and page purpose.
- Interface layout hierarchy.
- Navigation model.
- Control choices and information priority.
- Interaction annotations, not visual decoration.

Exit when a low-fidelity wireframe can be built without inventing product rules.

## 5. Surface Plane

Answer:

- What should the product feel like in the target situation?
- Which visual, verbal, motion, audio, or haptic signals clarify state and action?
- Does the presentation reduce cognitive work and support trust?
- Is the product character consistent across success, waiting, failure, and recovery?

Produce:

- Product character and tone principles.
- Visual hierarchy and component-state direction.
- Content design and feedback language.
- Accessibility and sensory constraints.
- High-fidelity examples only when requested.

Exit when presentation reinforces comprehension and intent without hiding structural weakness.

## Plane Review Record

For every plane, record:

```text
Decision:
Evidence:
Lens proposals and principle IDs:
Conflict and resolution:
Rejected alternative and reason:
Assumptions:
Upstream constraints:
Downstream implications:
Exit check:
```
