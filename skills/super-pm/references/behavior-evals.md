# Behavior Evaluations

Use these tasks for independent forward tests after workflow changes. Evaluate behavior, not whether the output repeats the instructions.

## 1. Focused Feature Decision

**Input**: “Should a photo app add daily check-ins?”

**Pass**: Give a provisional decision, strongest objection, boundary assumption, and cheapest evidence. Ask only if missing information could reverse the recommendation.

**Fail**: Require mode, lens, or framework selection first; produce seven lens monologues; generate a PRD.

## 2. Ambiguous Zero-To-One Idea

**Input**: “I want to build something that helps older adults who live alone.”

**Pass**: Offer concrete exclusions, ask no more than three high-information questions, and form a provisional Negative Boundary.

**Fail**: Brainstorm features immediately; demand a complete abstract vision; force all five dimensions as sequential stages.

## 3. Immediate PRD Request

**Input**: “Give me a PRD from what we know now. Do not ask more questions.”

**Pass**: Produce it immediately, label maturity, and mark unknowns `Pending` with reasons.

**Fail**: Continue discovery; convert assumptions into facts; label a one-page brief `Implementation-ready`.

## 4. Existing Decision File Without Write Authorization

**Environment**: `.super-pm/decisions.md` exists. The user asks only for a feature review.

**Pass**: Read relevant boundaries, surface conflicts or stale assumptions, and make no file changes.

**Fail**: Write merely because the skill ran; treat historical decisions as unquestionable facts.

## 5. Explicit Persistence Request

**Input**: “Save the decision we just confirmed in the project.”

**Pass**: Persist only confirmed decisions, boundaries, evidence, unresolved assumptions, next validation, and revisit triggers.

**Fail**: Store hidden reasoning, full lens dialogue, or unconfirmed inference.

## 6. Lens Conflict

**Input**: “Should the free plan lose export to drive upgrades?”

**Pass**: Use one Primary Owner and at most two challengers with named tests. Preserve disagreements that change the decision.

**Fail**: Give all seven lenses equal airtime or blend incompatible recommendations into vague consensus.
