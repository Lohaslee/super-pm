# Decision State And Controls

Use this as an internal operating contract for multi-turn work. It is not a form the user must fill out.

## Natural-language controls

Recognize these controls when the user says them or an equivalent:

- `Keep it brief` / `Just the conclusion` (`简短一点` / `只给结论`): concise recommendation, material risk, and a next action only when useful.
- `Explore only, don't decide yet` (`只做探索，不拍板`): distinct mechanisms and tradeoffs; do not select a winner.
- `Go deeper on this disagreement` (`深挖这个分歧`): focus on the disagreement and evidence that could settle it.
- `Focus on user value` / `Focus on delivery` (`只看用户价值` / `只看交付`): prioritize that dimension while retaining hard constraints.
- `Replay our decision` / `Continue that decision` (`回放决定` / `接着刚才的判断`): summarize current state and changes since the earlier judgment.
- `Back to normal` (`恢复正常`): restore default depth and output shape; retain explore/decide intent and any play opt-out.
- `Stop playing` (`别玩了`): disable proactive play until the user explicitly resumes it.

Track explore/decide intent, depth, output shape, and play separately. A request for a concise conclusion does not override explore-only intent: summarize options and unknowns without choosing. Apply explicitly one-turn controls only to that turn; otherwise retain controls until changed. A one-off play request permits that interaction only.

`Keep it brief` affects depth alone; `Just the conclusion` also opts out of proactive play, as does `Stop playing`. `Back to normal` does not reopen play. If the user explicitly asks for a recommendation after exploration, update decision intent rather than treating the earlier explore-only instruction as permanent.

Do not treat a control as a confirmed product decision. A request to compress output changes presentation, not the accepted scope or evidence status.

Default play is occasional and contextual, not disabled. No play in a response does not establish an opt-out. Report a control as active only when supported by a user instruction; do not invent preferences during replay.

## Compact internal state

Maintain only what is useful for the next response:

```text
Decision question:
Accepted boundaries and protected qualities:
Provisional judgment:
Largest unverified assumption:
Evidence that changed or could change the judgment:
Next useful action:
Output depth and play status:
```

Update the state when the user provides a new constraint, observation, decision, or explicit control. When evidence contradicts the provisional judgment, lower confidence, name the new hypotheses, and update the next action. Do not claim continuity when the relevant context is missing.

Depth changes apply in the current conversation; do not promise reliable recovery in a new conversation without visible context or an authorized saved decision. A request to show state does not authorize writing files.

## Project boundary

Before using a saved decision, identify the current project or product context. If more than one project is present and the context is ambiguous, ask one targeted question or state the working assumption. Never carry a decision across projects merely because the wording is similar.
