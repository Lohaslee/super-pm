# Evidence Ledger And Decision Branches

Use this ledger when a recommendation depends on evidence, especially when a small sample or estimated threshold could be mistaken for proof.

## Source labels

Distinguish source from sample scope: user-reported behavior remains user-reported; a small sample is a scope limit, not proof of direct observation. Label material inputs when this distinction affects the decision; do not force a ledger table into every answer. Use the user's working language.

Label each material input as one of:

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
