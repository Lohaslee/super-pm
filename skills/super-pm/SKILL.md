---
name: super-pm
description: Use six distilled product lenses (Steve Jobs, Zhang Xiaolong, Liang Ning, Yu Jun, Wang Shimu, and Li Xiang) to clarify negative requirements, define product strategy, work through the five planes of user experience, resolve tradeoffs, and produce evidence-aware product decisions or PRDs. Trigger for product discovery, 0-to-1 concepts, feature definition, product diagnosis, scope reduction, UX structure, interaction framing, or formal PRD work.
---

# Super PM

Turn an unclear product idea into a defensible product decision and an executable PRD. Start from what the user refuses to build, proceed through the five planes in dependency order, and call only the product lenses that help with the current decision.

## Operating Rules

1. Preserve the user's wording for goals, constraints, metrics, and non-goals. Mark interpretations as interpretations.
2. Start discovery by asking what must not happen, what must not be built, and which outcomes are unacceptable.
3. Ask at most three high-information questions per round. Do not repeat a question already answered.
4. Separate facts, user statements, assumptions, inferences, and recommendations.
5. Treat the six thinkers as distilled decision lenses, not simulated people. Never claim that a person endorses the result or fabricate a quotation.
6. Use upstream planes to constrain downstream planes. Do not solve visual presentation before strategy, scope, and structure are coherent.
7. Prefer the smallest product that proves the strategic hypothesis. Do not add speculative features.
8. Keep disagreements visible. Apply the conflict rules rather than blending incompatible advice into vague consensus.
9. In Chinese output, use the exact plane names `战略层、范围层、结构层、框架层、表现层`. The first mention may say `框架层（Skeleton Plane）`; never rename it `骨架层`.

## Choose A Mode

- **Full product definition**: Run negative discovery, all five planes, decision review, and PRD output.
- **Product diagnosis**: Map the existing product onto the five planes, identify the earliest broken plane, and repair from there.
- **Single-plane work**: Work only on the requested plane, but state any missing upstream assumptions.
- **Decision review**: Compare options with relevant lenses and return a decision record without generating a full PRD.

## Run The Workflow

### 1. Establish The Negative Boundary

Ask for the easiest exclusions first:

- Which users or scenarios are explicitly out of scope?
- Which experiences, business outcomes, or implementation costs are unacceptable?
- Which tempting features must this release avoid?
- What may be valuable later but is not part of the current bet?

Return a short **Negative Boundary** with `must not`, `not now`, and `hard constraints`. If the user cannot answer, offer concrete alternatives to reject rather than asking for an abstract vision.

### 2. Build The Decision Brief

Capture the user, situation, unmet need, current alternative, product promise, success signal, constraints, assumptions, and non-goals. Do not draft the full PRD until this brief is coherent, unless the user explicitly requests a one-pass draft.

### 3. Traverse The Five Planes

Read [five-planes.md](references/five-planes.md) and process in order:

1. Strategy: user needs and product objectives.
2. Scope: functional and content requirements, including exclusions.
3. Structure: interaction flows and information architecture.
4. Framework (Skeleton): interface, navigation, and information arrangement.
5. Surface: sensory design, language, feedback, and product character.

At every plane, state the decision, evidence, selected lenses, rejected alternative, remaining assumption, and exit check. Move backward when a downstream problem exposes an upstream contradiction.

### 4. Route Product Lenses

Read [lens-router.md](references/lens-router.md). Select two to four lenses based on the current decision; do not invoke all six by default. Then read only the selected thinker files:

- [jobs.md](references/jobs.md)
- [zhang-xiaolong.md](references/zhang-xiaolong.md)
- [liang-ning.md](references/liang-ning.md)
- [yu-jun.md](references/yu-jun.md)
- [wang-shimu.md](references/wang-shimu.md)
- [li-xiang.md](references/li-xiang.md)

Apply their diagnostic questions and decision rules. Cite the principle IDs in internal decision records, for example `YX-P03`; include public source links when the user requests evidence or when the conclusion depends materially on attribution.

### 5. Resolve Conflicts

Read [conflict-resolution.md](references/conflict-resolution.md). Rank decisions by:

1. User-declared unacceptable outcomes and hard constraints.
2. Safety, legality, and irreversible harm.
3. Observed user problem and credible evidence.
4. Product objective and agreed success metric.
5. Delivery constraints and reversibility.
6. Thinker preference.

Do not use a famous person's reputation as evidence.

### 6. Produce The Requested Artifact

For a full definition, use [prd-template.md](references/prd-template.md). Keep unresolved items explicit. Include the Negative Boundary and a short Product-Lens Decision Log so future changes can be checked against the original reasoning.

## Quality Gate

Before delivery, verify:

- Every feature traces to a user need and product objective.
- Every non-goal remains excluded from scope and downstream designs.
- Scope separates `must`, `later`, and `not doing`.
- The primary user flow has entry, success, failure, empty, permission, and recovery states where relevant.
- Framework-plane decisions do not compensate for an unresolved structure problem.
- Surface choices reinforce the intended product character rather than decorate it.
- Metrics distinguish leading behavior from lagging business outcomes.
- Attributions use declared source IDs; no invented quotations or impersonation appear.
- Assumptions and evidence gaps are visible.

## Maintain The Knowledge Base

Read [source-policy.md](references/source-policy.md) before adding or changing a thinker principle. Run:

```bash
python3 scripts/validate_sources.py
```

Keep detailed evidence in the thinker references and keep this file focused on execution.
