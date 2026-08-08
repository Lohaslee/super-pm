# Worked Example: Automatic Meeting-Note Delivery

## User Question

“Our AI meeting notes can already produce a summary. Should we add automatic delivery to every attendee after the meeting?”

Known facts: summary generation works; authorization preferences, wrong-send rate, and edit rate are unknown.

## One Default Decision Loop

**Direct recommendation (俞老师 as Primary Owner)**: Do not enable automatic delivery by default in this release. Test “preview, then host confirms delivery,” and measure confirmation, edit, and abandonment rates. The user value is trustworthy delivery with less effort, not automation by itself.

**Strongest objection (乔老师 as Challenger)**: If confirmation still requires deliberate action, this may only replace copy-and-paste with another button. If it does not save meaningful time, do not build even the confirmation flow.

**Negative Boundary check**:

- Must not: send incorrect, sensitive, or unapproved content to all attendees.
- Not now: automatic delivery to external contacts or complex approval chains.
- Protected quality: the user retains final control over content and recipients.

**Provisional decision**: Validate “preview and confirm,” not “automatic delivery by default.” If fewer than 40% of hosts confirm delivery across 20 real meetings, or more than 30% of summaries need substantial edits, stop delivery automation and improve summary quality and editing first.

**Cheapest evidence**: Use a clickable prototype and manual delivery for 20 meetings. Record confirmation, edits, abandonment, recipient mistakes, and time saved.

## Why The Workflow Stops Here

The question now has a reversible, testable scope decision. Do not require mode selection, a complete Decision Brief, all five product dimensions, or a PRD. Expand permissions, recovery, audit, and notification experience only when the feature enters implementation.
