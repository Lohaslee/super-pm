# Evidence Ledger And Decision Branches

Choose the lightest evidence treatment that changes the decision:

- **Brief source check**: when a recommendation materially relies on a small sample, user-reported behavior, an unverified factual claim, or a numeric decision threshold, state source, scope or sample limits, and uncertainty in ordinary prose. A number alone does not require a record; a deadline is not automatically a validation threshold.
- **Validation record**: when designing or conducting validation, reconciling conflicting evidence, or reversing a direction, use the relevant record fields below. Show only what helps the user act; a full table is optional and file persistence still requires authorization.
- **Ordinary decision**: when accepted boundaries and a low-loss tradeoff suffice, answer directly. Check the evidence underlying a boundary if it is disputed; “scope decision” is not an exemption from material evidence.

## Source labels

Distinguish source from sample scope: user-reported behavior remains user-reported; a small sample is a scope limit, not proof of direct observation. Label material inputs when this distinction affects the decision; do not force a ledger table into every answer. Use the user's working language.

Keep source and interpretation distinguishable using these labels as needed; source and sample scope may apply together:

- `User statement`: what the user explicitly reported or decided.
- `Observed behavior`: what was directly observed in a product, interview, test, or public source.
- `Small-sample finding`: an observation with a limited sample; state the sample and do not generalize.
- `External research`: a checked outside source with scope and date.
- `Business baseline`: an existing internal metric or operational fact.
- `Inference`: a reasoned interpretation that still needs testing.
- `Working target`: a provisional threshold chosen for the experiment, not an industry fact.

Do not let example numbers, illustrative thresholds, or lens advice enter the ledger as observations.

## Compact record

```text
Hypothesis:
Source and scope:
Predicted behavior or outcome:
Method and sample:
Decision threshold and basis:
Observed result:
Interpretation and limits:
Decision changed or retained:
Next action:
```

The record is incomplete until the evidence changes or deliberately retains a decision. A result can reduce confidence without selecting a new direction.

## Branch conditions

When two directions remain plausible, express the next decision as observable branches:

```text
If observation A -> retain direction X
If observation B -> switch to direction Y
If neither is distinguishable -> run the smallest reversible test
```

Tie each branch to a cost, failure consequence, baseline, or explicitly provisional working target. Preserve sample limits and do not call mechanism evidence market validation.
