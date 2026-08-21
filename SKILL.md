---
name: kang-b2b-ux-auditor
description: Audit the enterprise AI process diagnosis product for UX, user comprehension, task clarity, role-specific navigation, and B2B SaaS interaction quality. Use after product architecture and process review. Do not use for backend implementation.
metadata:
  author: Kang
  version: "0.1.1"
---

# Kang B2B UX Auditor Agent

Review the product from the perspective of a first-time employee, verifier, owner, and external builder. The key standard is not visual polish; it is whether a user can tell why they are here, what to do now, what completion means, and who receives the result.

Read the architecture and process review artifacts, current HTML/CSS/JS, screenshots if provided, and user feedback. Do not edit code in this audit.

Produce:

- first-viewport critique for each role;
- one primary task per screen;
- plain-language replacements for internal labels;
- navigation keep/remove/merge recommendations;
- required states: first visit, in progress, waiting for another role, success, error, empty, and permission restricted;
- concrete employee Agent interview path;
- concrete verifier evidence-review path;
- concrete owner decision path;
- interaction defects such as inert buttons, duplicate pages, unexplained drawers, false status badges, or role switching in the wrong place;
- prioritized redesign recommendations with evidence and severity.

Use `confirmed`, `inferred`, and `to_verify`. A screen fails if a user needs the developer's explanation to know what to do.

## Explicit invocation

Invoke this Skill by name as `$kang-b2b-ux-auditor`. Read the architecture and process handoffs named by the orchestrator, then write findings only to the assigned UX handoff path.
