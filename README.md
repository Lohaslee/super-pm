# Super PM

`super-pm` is a reusable Codex skill for turning unclear product ideas into defensible product decisions and executable PRDs.

It starts by asking what must not be built and what qualities must be protected. It then dynamically selects seven distilled product lenses presented under the aliases 乔老师、张老师、梁老师、俞老师、王老师、李老师、雷老师. They independently reframe the problem, propose designs, challenge the current direction, and expose tradeoffs before working through strategy, scope, structure, skeleton, and surface.

The lenses are active product-advisory perspectives, not decorative labels. Their disagreements remain visible and their accepted advice is translated into downstream design and implementation constraints. They are method-oriented syntheses, not personality simulations, and do not imply endorsement by any real person. Dialogue may occasionally borrow a lens's question shape or a short verified phrase, but never impersonates the person.

Users may optionally appoint one lens as the Lead PM for a project. The Lead PM owns the coherent product direction while other lenses provide specialist proposals and independent challenges; evidence and the user's negative boundaries still outrank role status.

## Install

Ask Codex:

```text
Install the skill from https://github.com/Lohaslee/super-pm/tree/main/skills/super-pm
```

Alternatively, copy `skills/super-pm` into your Codex skills directory.

## Use

```text
Use $super-pm to clarify this product idea from what we should not build, then produce a PRD.
```

The skill supports full product definition, product diagnosis, single-plane work, decision reviews, and on-demand reports or PRDs at any point in the discussion. Early artifacts are explicitly labeled as snapshots or drafts, with assumptions and missing decisions kept visible.

## Validate

```bash
python3 skills/super-pm/scripts/validate_sources.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/super-pm
```

## License

MIT. Public source links and attributed ideas remain subject to their respective owners' terms.
