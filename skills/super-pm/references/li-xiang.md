# Li Xiang Lens

Use this lens for product definition, target-segment completeness, technology choices, business loops, organization, scale, and execution. These cards synthesize public courses, speeches, and direct interviews; they are not quotations or impersonation.

## Sources

- [LX-S01] [Tier 1] Li Xiang: 16 Lectures on Product Practice (Dedao, official course page) - https://www.igetget.com/course/%E6%9D%8E%E6%83%B3%C2%B7%E4%BA%A7%E5%93%81%E5%AE%9E%E6%88%9816%E8%AE%B2?param=wpysGYsVfGg&token=v12pOMZN7mbJwgMs4jJDrjxdYaGkoE
- [LX-S02] [Tier 1] Li Xiang Product Practice course launch, complete event (Li Auto official Bilibili account, 2023, video) - https://www.bilibili.com/video/BV1kh4y1U7cH/
- [LX-S03] [Tier 2] Three-hour conversation with Li Xiang, complete edition (Sina Finance, 2024, direct interview transcript) - https://finance.sina.com.cn/tech/2024-12-27/doc-ineccwtt4449919.shtml
- [LX-S04] [Tier 2] Li Xiang speech: most people are gold living like scrap (Sohu/Investor, speech transcript) - https://www.sohu.com/a/524196196_532789
- [LX-S05] [Tier 2] Conversation with Li Xiang: iterations of an ideal nation (HyT Capital, direct interview) - https://eng.huacapital.com/news_detail_90.html

## Distilled Principles

### LX-P01 Define the product before listing features

- Source basis: LX-S01, LX-S02
- Distilled principle: Product definition aligns target user, specific situation, promised outcome, category, price or cost boundary, and the capabilities necessary to deliver it.
- Use when: A team begins with a feature backlog or broad technology ambition.
- Ask: For exactly whom is this product the obvious choice, in which situation, and why?
- Decision rule: Reject features that do not strengthen the chosen definition or a required end-to-end experience.
- Guardrail: A crisp sentence is not enough; the organization must be capable of delivering the implied promise.
- Confidence: high

### LX-P02 Choose a precise target segment

- Source basis: LX-S01, LX-S02, LX-S05
- Distilled principle: A product becomes stronger by making coherent choices for a valuable target segment rather than averaging conflicting needs across everyone.
- Use when: Requirements from multiple user groups create a compromised product.
- Ask: Which user situation creates the strongest willingness to choose and the clearest product tradeoffs?
- Decision rule: Prioritize one segment and explicitly exclude needs that would weaken its core experience.
- Guardrail: Segment focus must not become discriminatory exclusion or ignore essential accessibility.
- Confidence: high

### LX-P03 Deliver a complete core experience

- Source basis: LX-S01, LX-S02
- Distilled principle: The minimum viable product should be narrow but complete across the target user's critical journey, not a collection of disconnected partial features.
- Use when: MVP is interpreted as low quality or missing essential steps.
- Ask: Can the target user achieve the promised outcome reliably from entry through recovery?
- Decision rule: Reduce breadth before removing an essential link in the core journey.
- Guardrail: Completeness should not expand into every adjacent use case before evidence exists.
- Confidence: high

### LX-P04 Technology must serve the product route

- Source basis: LX-S01, LX-S02, LX-S03
- Distilled principle: Select and sequence technology according to the product outcome, timing, cost curve, and organizational ability to turn it into user value.
- Use when: Teams pursue technology leadership without a product path.
- Ask: Which user outcome becomes possible or materially better, and when can we deliver it reliably?
- Decision rule: Invest deeply when the technology is central to differentiation and compounds; partner or defer when it is peripheral.
- Guardrail: Near-term product fit should not blind the team to a technology shift that will invalidate the current route.
- Confidence: high

### LX-P05 Build a closed business loop

- Source basis: LX-S01, LX-S05
- Distilled principle: User value, delivery cost, acquisition, monetization, service, and repeat behavior must form a sustainable loop rather than independent optimistic assumptions.
- Use when: A product has demand but unclear economics or operational load.
- Ask: Who pays, why repeatedly, what does serving them cost at scale, and which capability improves the loop?
- Decision rule: Test the weakest link in the business loop before scaling the strongest visible metric.
- Guardrail: Early products may intentionally subsidize learning; define the evidence and deadline for sustainability.
- Confidence: high

### LX-P06 Organization is part of the product system

- Source basis: LX-S01, LX-S03, LX-S05
- Distilled principle: Product quality reflects how goals, ownership, information, incentives, and capabilities are organized; repeated cross-team failures are product problems.
- Use when: The same integration or execution issue recurs across releases.
- Ask: Which organizational boundary prevents an end-to-end owner from seeing or fixing the user outcome?
- Decision rule: Align ownership and metrics with the complete user journey or core product module.
- Guardrail: Do not reorganize around every temporary issue; distinguish structural failure from normal coordination.
- Confidence: high

### LX-P07 Use a consistent hierarchy of goals

- Source basis: LX-S01, LX-S02
- Distilled principle: Strategy, product line, release, team, and individual decisions should connect through a small hierarchy of measurable outcomes.
- Use when: Teams optimize local tasks that do not add up to the product objective.
- Ask: Which higher-level outcome does this work change, and how will we observe the contribution?
- Decision rule: Remove or redesign work that cannot trace to an agreed outcome or necessary capability.
- Guardrail: Goal trees must not pretend uncertain causal links are guaranteed.
- Confidence: high

### LX-P08 Learn through demanding real-world use

- Source basis: LX-S01, LX-S02, LX-S03
- Distilled principle: Product truth emerges when the complete system faces representative high-stakes scenarios, not only component tests and friendly demos.
- Use when: A complex product appears successful in isolated tests.
- Ask: Which real scenario combines the hardest user, environment, operational, and recovery demands?
- Decision rule: Test end-to-end in the most informative representative scenario before broad rollout.
- Guardrail: High-stakes testing requires safety controls and must not externalize experimental risk onto users.
- Confidence: high

### LX-P09 Make tradeoffs explicit and irreversible bets rare

- Source basis: LX-S01, LX-S03, LX-S05
- Distilled principle: Strong execution separates reversible operating decisions from expensive long-horizon commitments and raises the evidence bar for the latter.
- Use when: Infrastructure, hardware, channel, brand, or organizational choices create long lock-in.
- Ask: What becomes costly to reverse, and what evidence justifies committing now?
- Decision rule: Prototype or stage commitments when uncertainty is high; commit deeply only where timing or compounding advantage requires it.
- Guardrail: Excessive optionality can cause strategic drift and underinvestment.
- Confidence: medium

### LX-P10 Scale only after the product mechanism is legible

- Source basis: LX-S01, LX-S02, LX-S05
- Distilled principle: Scale multiplies both value and defects; the team should understand why target users choose, succeed, and return before accelerating distribution and complexity.
- Use when: Early demand triggers pressure for rapid expansion.
- Ask: Which repeatable mechanism drives choice and success, and where does it fail under load or new segments?
- Decision rule: Scale the proven mechanism while using guardrails to detect experience or economic degradation.
- Guardrail: Waiting for perfect certainty can miss a time-sensitive market; define an acceptable evidence threshold in advance.
- Confidence: high
