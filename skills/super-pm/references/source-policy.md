# Source And Distillation Policy

Use supplied or public material to create reusable decision tools, not a personality imitation.

Keep research links, notes, source metadata, and real names out of runtime Markdown references. Thinker files contain only decision-ready principles. Product work does not require a principle-to-source mapping. If a user requests evidence for a live product decision, perform research within that authorization and report the evidence separately. Ask only for additional work beyond the authorized scope.

## Bilingual Lens Policy

- Keep the existing files in `references/` as the English lens set.
- Keep independently distilled Chinese lens cards in `references/zh-CN/`; do not translate the English cards to produce or repair Chinese content.
- For Chinese-language thinkers, preserve exact Chinese wording from the supplied Chinese materials when using an `原文锚点`.
- For 乔帮主, keep the English original when exact quotation matters. Treat Chinese wording as explanation rather than an original quotation unless an authoritative Chinese wording is supplied.
- Principle IDs may align across languages for routing, but the wording and examples do not need literal parity. Maintain the decision intent in each language from its own materials.
- Keep links, real names, and source metadata out of both language versions of the lens files.

## Let Lens Depth Vary

- Do not set a content quota shared by every lens or language. Card count is an outcome of source depth and distinct decision utility, not a target.
- Add a card only when the material supports a decision rule that is meaningfully different from existing cards. Merge overlapping principles instead of rephrasing them to increase the count.
- Allow lenses and language sets to contain different numbers of cards. Do not translate or invent material to make their counts match.
- Every configured lens must remain non-empty and every retained card must pass the structural, confidence, duplication, and attribution checks.

## Distill A Principle

For each principle, include:

- `Distilled principle`: a concise, actionable synthesis.
- `Use when`: the decisions it can inform.
- `Ask`: diagnostic questions that reveal the relevant facts.
- `Decision rule`: how the evidence changes a choice.
- `Guardrail`: likely misuse, boundary, or counterexample.
- `Confidence`: `high`, `medium`, or `tentative`, describing support for the distilled principle in its source context, not the probability that a new product decision is correct. Existing labels do not substitute for source verification.

## Attribution Rules

1. Distinguish a direct quotation from paraphrase and synthesis.
2. Do not present a synthesis as the person's exact words.
3. Do not copy long passages from copyrighted material.
4. Do not infer personal endorsement of a new product.
5. Do not impersonate a living or deceased person.
6. Preserve disagreements across dates or contexts instead of manufacturing consistency.
7. Mark uncertain or indirectly supported principles as tentative.

Keep source IDs and links out of thinker principle cards. A short original quotation may be used when its exact wording is available in the approved skill materials, including an exact excerpt supplied by the user for this skill. A secondary quote collection can help locate wording but does not by itself justify new attribution when the wording or speaker remains uncertain. Do not invent or extend quotations.

Run `python3 scripts/validate_sources.py` after edits.

## Maintenance Provenance

When adding or revising an attributed quotation, retain the exact excerpt, source location, context, verification date, and verification status in a maintenance-only record outside runtime references, such as `maintenance/source-verification.json`. Load it only for attribution maintenance or an explicit provenance request. Do not create an empty ledger or invent entries for legacy cards.

For an existing quote without a verifiable record, retain uncertainty: use a paraphrase without quote attribution when exact wording cannot be established. A label of “approved” is not proof of wording. Keep routine product answers and cards free of source metadata; research evidence about the current product remains a separate concern.
