# Behavior Coverage And Known Failures

Tested version: **1.0.0 local candidate**, 2026-10-30; base checkout `58ac9b8` plus uncommitted edits.
Runtime SHA-256: `67b19cdd519469323e513ece8373999e423b228f894b6c53348fb3793dd43405`. The fingerprint covers SKILL.md, agents/, and references/ in the isolated snapshot. Working-copy runtime content matched after the runs; evaluation records and scripts are excluded from this runtime fingerprint.

Statuses apply to this tested content. Pass means the case contract was observed in the linked scenario once, not sustained reliability. Partial means some conditions were exercised. No old pass is silently carried forward.

| Case | Chinese | English | Current evidence |
|---|---|---|---|
| 01 | Not run | Not run | — |
| 02 | Not run | Not run | — |
| 03 | Not run | Not run | — |
| 04 | Not run | Not run | — |
| 05 | Not run | Not run | — |
| 06 | Not run | Not run | — |
| 07 | Not run | Not run | — |
| 08 | Not run | Not run | — |
| 09 | Not run | Not run | — |
| 10 | Not run | Not run | — |
| 11 | Not run | Not run | — |
| 12 | Not run | Partial | [EN 7](2026-10-30-transcript-en.md#turn-7), [cold 1](2026-10-30-transcript-simple.md#turn-1): reversible A only; irreversible B unrun |
| 13 | Not run | Not run | — |
| 14 | Not run | Not run | — |
| 15 | Not run | Not run | — |
| 16 | Partial | Partial | [ZH 2](2026-10-30-transcript-zh.md#turn-2), [EN 2](2026-10-30-transcript-en.md#turn-2): alternate user situation, distinct mechanisms and no winner |
| 17 | Not run | Not run | — |
| 18 | Not run | Partial | [EN 5–6](2026-10-30-transcript-en.md#turn-5): opt-out, one-off exercise, return to no play; no user selection continuation |
| 19 | Pass | Not run | [ZH 5](2026-10-30-transcript-zh.md#turn-5): replay, contradictory reported sample, distinguishing next action |
| 20 | Not run | Not run | — |
| 21 | Not run | Pass | [EN 8](2026-10-30-transcript-en.md#turn-8): no-baseline test, explicitly provisional go/no-go rules and limits |
| 22 | Not run | Not run | — |
| 23 | Pass | Pass | [ZH 2–4](2026-10-30-transcript-zh.md#turn-2), [EN 2–4](2026-10-30-transcript-en.md#turn-2): explore intent, new constraints, brevity, replay |
| 24 | Pass | Not run | [ZH 5](2026-10-30-transcript-zh.md#turn-5): reported observation versus market proof and branches |
| 25 | Pass | Partial | [ZH 2–8](2026-10-30-transcript-zh.md#turn-2): restore, opt-out, product switch, continue, restore after opt-out; EN controls only |
| 26 | Pass | Pass | [ZH 1](2026-10-30-transcript-zh.md#turn-1), [EN 1](2026-10-30-transcript-en.md#turn-1): options, recommendation, brief; Chinese response has repetition |
| 27 | Not run | Pass | [cold 1](2026-10-30-transcript-simple.md#turn-1), [EN 7–8](2026-10-30-transcript-en.md#turn-7): concise A and scoped evidence/threshold B |
| 28 | Not run | Pass | [EN 9](2026-10-30-transcript-en.md#turn-9): unresolved recipient permission explicitly changes recommendation |

The 18 trigger fixtures retain structural validation only; actual automatic routing was not run. Twenty dialogue turns across three conversations are not twenty independently covered cases. Historical evidence: [September review](2026-09-10-review.md), [October review](2026-10-09-upgrade-review.md).

## Known failure index

- **Observed: invented play opt-out.** The [October trial](2026-10-09-upgrade-review.md) reported play disabled without a user instruction. Current [English brief replay](2026-10-30-transcript-en.md#turn-3), [Chinese brief replay](2026-10-30-transcript-zh.md#turn-3), and [English normal-depth restoration](2026-10-30-transcript-simple.md#turn-3) retain occasional play when no opt-out occurred. [Chinese restoration after opt-out](2026-10-30-transcript-zh.md#turn-8) retains disabled play. Status: regression passed in these scenarios, not a universal guarantee.

Other Fail conditions in behavior-evals.md are preventive risks, not evidence of reproduced bugs. No new failure library or runtime load is added for them.

## Limits

- One execution per scenario, using the local CLI default model; no old/new A/B, cross-model study, or production user research.
- Chinese combined output repeats some content between exploration and brief; completeness passed, strict rendered one-page layout was not tested.
- Cold simple decision read only the entrypoint (twice). This observation does not measure all system-prompt tokens or guarantee the same load for every request.
- Historical and partially covered cases remain visible above; unused English/Chinese case variants are not inferred to pass.
