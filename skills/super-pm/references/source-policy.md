# Source And Distillation Policy

Use public material to create traceable decision tools, not a personality imitation.

## Source Tiers

- **Tier 1**: the person's own speech, interview, article, letter, course, book, or official company publication/video.
- **Tier 2**: a reputable publisher's complete transcript or direct interview.
- **Tier 3**: commentary, notes, summaries, or reposts. Use only to locate stronger evidence or mark the resulting principle as tentative.

Prefer Tier 1. Keep the publication date and situation because a person's view may change over time.

## Distill A Principle

For each principle, include:

- `Source basis`: one or more declared source IDs.
- `Distilled principle`: a concise, actionable synthesis.
- `Use when`: the decisions it can inform.
- `Ask`: diagnostic questions that reveal the relevant facts.
- `Decision rule`: how the evidence changes a choice.
- `Guardrail`: likely misuse, boundary, or counterexample.
- `Confidence`: `high`, `medium`, or `tentative`.

## Attribution Rules

1. Distinguish a direct quotation from paraphrase and synthesis.
2. Do not present a synthesis as the person's exact words.
3. Do not copy long passages from copyrighted material.
4. Do not infer personal endorsement of a new product.
5. Do not impersonate a living or deceased person.
6. Preserve disagreements across dates or contexts instead of manufacturing consistency.
7. Use Tier 3 material only with explicit low confidence when the original cannot be found.

## Source Entry Format

```markdown
- [XX-S01] [Tier 1] Title (publisher, date, type) - https://example.com
```

Run `python3 scripts/validate_sources.py` after edits.
