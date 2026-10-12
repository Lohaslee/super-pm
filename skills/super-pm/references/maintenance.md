# Maintain The Knowledge Base

Read [source-policy.md](source-policy.md) before adding or changing a thinker principle. From the repository root, run:

```bash
python3 skills/super-pm/scripts/validate_sources.py
```

Keep source links, research notes, source metadata, and real names out of runtime Markdown references. Maintain verification records separately as described in source-policy.md; never invent missing provenance. Thinker files contain only decision-ready principle cards. The product workflow does not require every principle to trace to a specific source entry.

Do not target a uniform card count across lenses or languages. Let each lens grow according to source depth and distinct decision utility. Add a card only when it contributes a non-duplicate decision rule; merge overlaps instead of padding a quota. Keep every configured lens non-empty so routing never points to an unusable reference.

Maintain English thinker cards and Chinese thinker cards as two source-material-based sets, not as translations of each other. Preserve stable principle IDs when their decision intent aligns. Run the validator after any language or lens change.

Before changing the workflow, review [behavior-evals.md](behavior-evals.md) and [中文行为评测](zh-CN/behavior-evals.md). Forward-test the affected cases when an independent evaluation surface is available. For concise software and offline-service examples, read [worked-example.md](worked-example.md) in English mode or [中文工作样例](zh-CN/worked-example.md) in Chinese mode.

When the trigger description or product boundary changes, update the natural positive and negative cases in `evals/trigger-cases.json`. `validate_sources.py` checks the fixture schema and bilingual boundary coverage; it does not claim that a model actually routed every case correctly. Use an independent runtime for behavioral trigger tests when one is available.

## Release From One Source

The repository's `skills/super-pm/` directory is the maintained source, including its optional easter-egg experience. Installed copies are release targets, not independent variants.

After validation, compare the full directory with each intended installation, inspect destination-only content before syncing, and preserve unrelated files. Copy the same release to the intended installations; exclude `.DS_Store` and `__pycache__`. Verify content equality afterward and run the validators from the installed paths. Follow the user's authorization for installation, commits, and publishing; never infer Git push permission from a request to improve the skill.

Structural checks do not establish runtime routing or conversation quality. For behavior evaluation, report the tested inputs, actual outputs, pass/fail judgments, and limitations separately. Do not claim unrun cases passed.
