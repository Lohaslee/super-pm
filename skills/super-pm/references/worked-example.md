# Worked Examples

## 1. Automatic Meeting-Note Delivery

### User Question

“Our AI meeting notes can already produce a summary. Should we add automatic delivery to every attendee after the meeting?”

Known facts: summary generation works; authorization preferences, wrong-send rate, and edit rate are unknown.

### One Default Decision Loop

**Direct recommendation (俞老师 as Primary Owner)**: Do not enable automatic delivery by default in this release. Test “preview, then host confirms delivery,” and measure confirmation, edit, and abandonment rates. The user value is trustworthy delivery with less effort, not automation by itself.

**Strongest objection (乔老师 as Challenger)**: If confirmation still requires deliberate action, this may only replace copy-and-paste with another button. If it does not save meaningful time, do not build even the confirmation flow.

**Negative Boundary check**:

- Must not: send incorrect, sensitive, or unapproved content to all attendees.
- Not now: automatic delivery to external contacts or complex approval chains.
- Protected quality: the user retains final control over content and recipients.

**Provisional decision**: Validate “preview and confirm,” not “automatic delivery by default.” If fewer than 40% of hosts confirm delivery across 20 real meetings, or more than 30% of summaries need substantial edits, stop delivery automation and improve summary quality and editing first.

**Cheapest evidence**: Use a clickable prototype and manual delivery for 20 meetings. Record confirmation, edits, abandonment, recipient mistakes, and time saved.

### Why The Workflow Stops Here

The question now has a reversible, testable scope decision. Do not require mode selection, a complete Decision Brief, all five product dimensions, or a PRD. Expand permissions, recovery, audit, and notification experience only when the feature enters implementation.

## 2. Last-Minute Home-Care Cancellation

### User Question

“A home-care worker cancels two hours before a scheduled visit. Is an automatic refund enough?”

Known facts: some customers live alone; the service can contact customers and emergency contacts; there is no backup-worker dispatch mechanism.

### One Service-Product Decision Loop

**Direct recommendation (李老师 as Primary Owner)**: A refund is not a complete recovery. First validate a three-level recovery process with human dispatch: confirm the customer's status within 10 minutes; prioritize a replacement; otherwise let the customer choose a delay or reschedule. Escalate immediate safety risks to the emergency contact or local emergency services, and do not present ordinary home care as medical response.

**Strongest objection (雷老师 as Challenger)**: Maintaining backup capacity for rare failures may make costs unsustainable. Limit the pilot to higher-risk customers, core service areas, and defined hours instead of promising the same protection for every order.

**Negative Boundary check**:

- Must not: issue a refund without confirming that a customer who lives alone has an understood next arrangement.
- Not now: build medical emergency response or promise guaranteed arrival without the capacity to deliver it.
- Protected qualities: transparent status, customer choice, and one accountable owner for every exception.

**Adaptive dimensions**: 产品系统 defines exception states and ownership; 使用与交付 covers absence, contact, replacement, rescheduling, and escalation; 触点与形态 defines phone and message updates; 体验与信任 forbids hiding the cancellation or falsely showing “on the way.”

**Provisional decision and cheapest evidence**: Use a human on-call operator for 30 cancellation incidents in one area. Pass if at least 90% of customers are contacted within 10 minutes, at least 80% have a replacement or confirmed alternative within 30 minutes, and no case closes without a clear arrangement. Record recovery cost per incident before building automated dispatch.
