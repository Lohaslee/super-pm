# Zhang Xiaolong Lens

Use this lens for human motivation, social behavior, restrained interaction, attention, communication products, and tools that recede after use. These cards are traceable syntheses, not quotations or impersonation.

## Sources

- [ZX-S01] [Tier 2] 2016 WeChat Open Class: Zhang Xiaolong's first public speech, official unabridged edition (Woshipm, 2016, transcript) - https://www.woshipm.com/it/265492.html
- [ZX-S02] [Tier 2] Zhang Xiaolong explains Mini Programs, full speech and video (Tencent Cloud Developer, 2017, transcript/video) - https://developer.cloud.tencent.com/article/1136014
- [ZX-S03] [Tier 2] Zhang Xiaolong responds to everything, four-hour WeChat Open Class speech (Tencent News, 2019, transcript) - https://view.inews.qq.com/a/TEC2019011000005000
- [ZX-S04] [Tier 1] 2019 WeChat Open Class: Zhang Xiaolong full speech review (Tencent Video, 2019, event video) - https://origin-m.v.qq.com/x/cover_seo/b86kk0n60chvn5j/b0029zsv8t9.html
- [ZX-S05] [Tier 2] Zhang Xiaolong speech transcript: ten years of product thinking at WeChat (Tencent News, 2021, transcript) - https://xw.qq.com/cmsid/TEC202101190138711A

## Distilled Principles

### ZX-P01 A good tool helps the user leave

- Source basis: ZX-S01, ZX-S02, ZX-S05
- Distilled principle: Judge a tool by how efficiently it helps users complete real-world intent, not by how long it retains attention.
- Use when: Engagement time is treated as the default success metric.
- Ask: What does the user want to finish, and what is the shortest trustworthy path back to their life?
- Decision rule: Prefer completion, successful return, and reduced effort metrics over raw duration for utility products.
- Guardrail: Some products create value through sustained participation; distinguish chosen immersion from engineered friction.
- Confidence: high

### ZX-P02 Begin with human motivation, not feature demand

- Source basis: ZX-S01, ZX-S03, ZX-S05
- Distilled principle: A stated feature request often masks a deeper need involving identity, recognition, control, safety, curiosity, or connection.
- Use when: Users request familiar features or a competitor copy.
- Ask: What human tension would remain if this requested feature did not exist anywhere?
- Decision rule: Solve the underlying motivation with the least burdensome mechanism, not necessarily the requested implementation.
- Guardrail: Do not invent psychological explanations that contradict user behavior or evidence.
- Confidence: high

### ZX-P03 Minimize unnecessary social pressure

- Source basis: ZX-S03, ZX-S05
- Distilled principle: Social features create obligations, comparison, performance, and interruption; design them as costs that require justification.
- Use when: Adding feeds, rankings, read states, public metrics, invitations, or notifications.
- Ask: What obligation or anxiety does this signal create for sender, receiver, and observer?
- Decision rule: Remove public or interruptive signals unless they create essential reciprocal value.
- Guardrail: Visibility can be necessary for coordination and accountability; make it contextual and controllable.
- Confidence: high

### ZX-P04 Let interaction follow an existing intuition

- Source basis: ZX-S01, ZX-S02
- Distilled principle: Prefer interactions that match users' existing mental models and situational intent over novel mechanics requiring explanation.
- Use when: Designing navigation, gestures, onboarding, or cross-channel entry.
- Ask: What would the user naturally try before being taught?
- Decision rule: Choose the mechanism with the lowest explanation and recall burden while preserving discoverability.
- Guardrail: Familiarity should not preserve a harmful convention or block a clearly superior learned behavior.
- Confidence: high

### ZX-P05 Use context as the entry point

- Source basis: ZX-S02, ZX-S05
- Distilled principle: A service becomes lighter when it appears in the physical or digital context where the need arises instead of demanding installation, search, and repeated setup.
- Use when: Designing Mini Program-like services, QR entry, links, integrations, or embedded workflows.
- Ask: Where does the need occur, and what is the most direct trustworthy entry from that moment?
- Decision rule: Remove acquisition and setup steps that do not contribute to safety, consent, or retained value.
- Guardrail: Frictionless entry must not erase informed consent, permissions, or a reliable way to return.
- Confidence: high

### ZX-P06 Product rules express values

- Source basis: ZX-S01, ZX-S03, ZX-S05
- Distilled principle: Ranking, messaging, identity, and platform rules inevitably favor certain behaviors; make those value choices explicit.
- Use when: Designing feeds, ecosystems, moderation, incentives, or growth mechanics.
- Ask: Which behavior does this rule reward at scale, and would we accept the resulting culture?
- Decision rule: Evaluate a rule by its system-level behavior after repeated use, not only its immediate metric lift.
- Guardrail: Values need operational definitions and enforcement; slogans are not product rules.
- Confidence: high

### ZX-P07 Decentralize creation while centralizing fair rules

- Source basis: ZX-S01, ZX-S02, ZX-S05
- Distilled principle: Platforms should enable participants to create value without the platform micromanaging every outcome, while maintaining clear and stable boundaries.
- Use when: Building ecosystems, creator tools, marketplaces, or extension platforms.
- Ask: What can participants decide themselves, and which shared rule is necessary for trust?
- Decision rule: Move domain decisions to participants unless central control is needed for safety, interoperability, or fairness.
- Guardrail: Decentralization without governance lets powerful actors externalize costs onto weaker users.
- Confidence: medium

### ZX-P08 Protect attention as a user resource

- Source basis: ZX-S03, ZX-S05
- Distilled principle: Notifications, badges, feeds, and prompts spend the user's finite attention and must earn that cost.
- Use when: Adding reminders, campaigns, red dots, recommendations, or re-engagement loops.
- Ask: Is this interruption important to the user at this moment, or only valuable to the sender?
- Decision rule: Default to pull, batching, or user control unless immediacy is part of the promised value.
- Guardrail: Under-notifying can cause real harm in urgent or time-sensitive workflows.
- Confidence: high

### ZX-P09 Identity expression is a product function

- Source basis: ZX-S03, ZX-S05
- Distilled principle: In social products, users manage how different people perceive them; publishing and visibility controls must support that reality.
- Use when: Designing profiles, posts, status, sharing, privacy, or audience selection.
- Ask: Who is the user performing for, and which audiences or contexts should remain separate?
- Decision rule: Give users legible control over audience and persistence before optimizing distribution.
- Guardrail: Excessive controls can become unusable; use safe defaults and understandable boundaries.
- Confidence: high

### ZX-P10 Resist metric-driven product deformation

- Source basis: ZX-S01, ZX-S03, ZX-S05
- Distilled principle: A local metric can push a product away from its purpose by rewarding interruption, low-quality information, or compelled behavior.
- Use when: Growth targets conflict with trust, information quality, or task completion.
- Ask: If this metric doubles, what unwanted behavior will also increase?
- Decision rule: Pair growth metrics with user-value and trust guardrails; reject tactics whose success depends on user regret.
- Guardrail: Product restraint does not remove the need for sustainable economics and accountable measurement.
- Confidence: high
