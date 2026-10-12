# Expanded Product Workflow

Use this workflow only when the Default Decision Loop reaches an expansion condition. Do not treat the numbered sections as mandatory gates for a focused question.

### 0. Inspect Existing Context

When files or a live product are available, inspect the relevant repository, product documents, implementation, and constraints. Record conflicts between the user's request and the existing state. Reuse known boundaries. Ask only about missing exclusions that could change the direction; do not restart discovery when context is sufficient.

### 1. Establish The Negative Boundary

Reuse confirmed exclusions first. When critical exclusions are missing, offer the easiest concrete choices:

- Which users or scenarios are explicitly out of scope?
- Which experiences, business outcomes, or implementation costs are unacceptable?
- Which tempting features must this release avoid?
- What may be valuable later but is not part of the current bet?

Return a short **Negative Boundary** with `must not`, `not now`, and `hard constraints`. If the user cannot answer, offer concrete alternatives to reject rather than asking for an abstract vision.

Also record `protected qualities`: what the product must preserve even under time, growth, or implementation pressure. Carry every accepted boundary into later product decisions and acceptance criteria.

### 2. Build The Decision Brief

Capture the user, situation, unmet need, current alternative, product promise, success signal, constraints, assumptions, evidence gaps, and non-goals. Do not draft the full PRD until this brief is coherent, unless the user explicitly requests a one-pass draft.

For every high-impact assumption, state what evidence would confirm or reverse it and propose the cheapest validation. Use authorization already present in the request or conversation. Ask only before additional work outside that scope; do not ask again for research the user already requested.

### 3. Select The Relevant Product Dimensions

In Chinese mode read [中文产品维度](zh-CN/product-dimensions.md); in English mode read [product-dimensions.md](product-dimensions.md). Always resolve demand, value, and the Negative Boundary. Then select only the dimensions and cross-cutting constraints that can change the product decision.

Do not force every product through an interface-centric sequence. Software may require detailed state and interaction work; hardware may require physical form, manufacturing, maintenance, and safety; a service may require people, service recovery, and operating scripts; an AI product may require model behavior, data, uncertainty, oversight, and trust. State what is in scope and what is intentionally skipped.

### 4. Convene The Relevant Product Lenses

In Chinese mode read [中文视角路由](zh-CN/lens-router.md) and [中文表达指引](zh-CN/voice-guidance.md). In English mode read [lens-router.md](lens-router.md) and [voice-guidance.md](voice-guidance.md). Determine whether the user selected a Lead PM. Assign one Primary Owner for each decision and add a challenger only when its named test can change the answer. Honor a user's explicit request for a lens. Across a full project, different lenses may enter for different dimensions; do not force all seven into every decision.

Then read only the selected thinker files in the working language.

Chinese mode:

- [乔帮主.md](zh-CN/乔帮主.md)
- [龙哥.md](zh-CN/龙哥.md)
- [梁老师.md](zh-CN/梁老师.md)
- [俞老师.md](zh-CN/俞老师.md)
- [师母.md](zh-CN/师母.md)
- [想哥.md](zh-CN/想哥.md)
- [军哥.md](zh-CN/军哥.md)

English mode:

- [乔帮主.md](乔帮主.md)
- [龙哥.md](龙哥.md)
- [梁老师.md](梁老师.md)
- [俞老师.md](俞老师.md)
- [师母.md](师母.md)
- [想哥.md](想哥.md)
- [军哥.md](军哥.md)

Apply their diagnostic questions and decision rules. Principle IDs are maintenance metadata. Do not show IDs such as `YJ-P03` in user-facing dialogue, reports, PRDs, decision briefs, or `.super-pm/decisions.md` unless the user explicitly requests traceability. When attribution helps, use an alias plus a plain-language principle title; otherwise state the recommendation without a lens label. Do not require principle-to-source traceability in product work. When the user requests research or evidence, perform the authorized work and report evidence separately from the lens recommendation.

When a lens contribution is material, capture:

- the problem it sees and how it reframes the question;
- a concrete product or design proposal;
- what it challenges or would refuse in the current direction;
- the tradeoff, evidence need, and downstream decision it would change;
- its principle IDs in internal working notes only.

In Lead-PM collaboration, have the Lead PM state the primary direction and integration logic first. Have supporting lenses identify blind spots, propose specialist alternatives, and pressure-test the direction independently before synthesis. Do not produce seven generic monologues. Do not show separate lens sections when a concise integrated answer preserves the only material disagreement.

### 5. Deliberate And Resolve Conflicts

In Chinese mode read [中文冲突处理](zh-CN/conflict-resolution.md); in English mode read [conflict-resolution.md](conflict-resolution.md). Show agreements and disagreements before synthesis. Resolve them using the user's Negative Boundary, credible evidence, primary-user value, product objective, delivery constraints, and reversibility. The Lead PM does not win by status alone. Record the accepted advice, rejected advice, reason, owner of the integrated decision, and revisit trigger.

### 6. Close The Evidence-To-Decision Loop

For every high-impact assumption, keep a compact Validation Record:

```text
Hypothesis:
Predicted behavior or outcome:
Method and sample:
Decision threshold:
Observed result:
Interpretation:
Decision changed or retained:
Next action:
```

Before execution, fill the hypothesis through decision threshold. Explain each threshold using a baseline, cost, error consequence, or explicitly provisional working target. Small qualitative samples can reveal mechanisms and failures; do not treat them as market-wide proof. Reuse existing authorization for research, competitor inspection, or prototype execution; ask only when the next action exceeds it. After evidence arrives, fill the result through next action, revise affected decisions and downstream constraints, and preserve what changed. Validation is incomplete if the evidence does not update a decision.

For multi-turn work, keep the compact state in [Decision State And Controls](decision-state.md) or [中文决策状态与控制](zh-CN/decision-state.md). Treat `只给结论`, `只做探索`, and `别玩了` as presentation or session controls; they do not become product requirements. When two directions remain plausible, use [Evidence Ledger And Decision Branches](evidence-ledger.md) to label the source and write observable reversal branches.

### 7. Preserve Confirmed Decisions

During context inspection, read `.super-pm/decisions.md` when it exists. Treat it as prior project context rather than unquestionable truth; surface conflicts, stale assumptions, and revisit triggers.

When a confirmed decision is likely to matter beyond the current conversation, offer once at a natural stopping point to save it. Do not offer for tentative, trivial, or already-persisted decisions. An offer is not write authorization.

Create or update `.super-pm/decisions.md` only when the user has asked to modify project files or explicitly asked to save the product decision. Never write it merely because the skill ran. When persistence is relevant, read [decision-memory.md](decision-memory.md) in English mode or [中文决策记忆](zh-CN/decision-memory.md) in Chinese mode and use its compact schema.

When a confirmed decision reverses an earlier one, never silently overwrite history. Mark the earlier record `superseded`, link both records, and capture the evidence or constraint that caused the change. Update a current record in place only when new information does not change the decision itself.

Do not store hidden reasoning, full council dialogue, or unconfirmed inference. When no writable project exists, offer the same fields as a portable Markdown decision snapshot.

### 8. Build The Decision Constraint Chain

Translate accepted upstream decisions into explicit downstream constraints:

- user need, value exchange, and Negative Boundary;
- product mechanism, system boundary, and scope rule;
- use, operation, delivery, and recovery lifecycle;
- relevant form, touchpoint, channel, or interaction constraint;
- experience, trust, product-character, and safety constraint;
- delivery or implementation acceptance check.

Every important implementation requirement must trace to an upstream decision. Do not let an AI coding agent fill unresolved product questions silently; mark them for user decision.

### 9. Produce The Requested Artifact

For solo work, early alignment, or a compact decision handoff, use the one-page brief in [中文 PRD 模板](zh-CN/prd-template.md) in Chinese mode or [prd-template.md](prd-template.md) in English mode. Do not label this brief implementation-ready.

For a full definition or implementation handoff, use the full PRD in the same language-specific template. Adapt it to the product type rather than filling irrelevant sections. Keep unresolved items explicit. Make it usable by an AI coding agent or delivery team while remaining readable by a person.

When the user asks for an artifact before the workflow is complete, do not continue questioning first. Generate it from all confirmed information available and label its maturity:

- **Snapshot**: current discussion state; major upstream decisions may still be open.
- **Draft**: the product direction is coherent, but evidence, scope, or delivery details remain unresolved.
- **Implementation-ready**: the relevant quality gates and acceptance boundaries are satisfied.

For an on-demand report, include the current objective, Negative Boundary, collaboration model and Lead PM when selected, confirmed decisions by relevant dimension, material lens advice and conflicts, evidence and assumptions, unresolved decisions, and recommended next step. For an on-demand PRD, use the PRD template for the working language, write `待确认` in Chinese or `Pending` in English with a reason for unavailable sections, and never fill gaps by turning assumptions into facts.

## Delivery Quality Gate

Apply this gate to full definitions and implementation handoffs, not every conversational answer.

- Each requirement traces to a user need and product objective; accepted exclusions and protected qualities reach acceptance checks.
- Scope distinguishes must, later, and not doing. Relevant lifecycles cover entry, success, failure, interruption, recovery, and exit.
- Product dimensions fit the product type; presentation cannot conceal unresolved value or delivery decisions.
- Metrics separate leading behavior from business outcomes; thresholds state their basis and sample limits.
- Material conflicts, rejected options, ownership, and revisit conditions remain clear.
- Executed validation records observed results and the decision changed or retained. Unknowns remain Pending, never invented facts.
- Apply the entrypoint's Pre-Response Checkpoint and language-specific voice guidance; keep maintenance IDs out of user-facing artifacts.
