# B2B UX Audit Rubric

## Evidence labels

- `confirmed`: directly observed in a runnable path, reproducible recording, or approved user research.
- `inferred`: a reasoned interpretation of the interface or supplied feedback that needs confirmation.
- `to_verify`: state, device, user, or behavior evidence is absent, stale, or contradictory.

## Task success test

For each user and task record: entry state, intent, first action, path, decision points, completion signal, handoff, recovery path, and evidence. A user succeeds only when they can perform the intended action, understand its result, and re-enter without losing or duplicating work.

## State matrix

Inspect or explicitly mark `first_visit`, `loading`, `saving`, `success`, `validation_error`, `server_error`, `empty`, `waiting`, `stale`, `conflict`, `permission_denied`, and `recovery`. A state is not complete if it has no explanation, next action, ownership, or safe retry behavior.

## Severity

- `blocker`: a critical task cannot be completed, the user is misled about a consequential result, or a permission boundary is unsafe.
- `high`: a core task requires developer explanation, causes likely wrong action, or cannot recover without support.
- `medium`: the task can complete but has repeated ambiguity, excess steps, or missing non-critical feedback.
- `low`: local wording, alignment, density, or aesthetic issue with no material task impact.

Visual preference alone cannot be `high` or `blocker`. Explain the task failure or comprehension risk behind every recommendation.

## B2B interaction checks

- role-specific navigation exposes only relevant work and makes unavailable work understandable;
- one primary task is visually and verbally clear per screen;
- tables support scan, sort, filter, selection, and detail without losing context;
- drawers and modals preserve orientation and have an explicit close/save/cancel outcome;
- bulk actions state scope, confirmation, progress, partial failure, and undo where safe;
- responsive layouts preserve task access and do not hide critical states;
- labels describe user concepts, not internal stage names;
- focus, keyboard, contrast, touch targets, and text fit are adequate for the target environment.

## Handoff fields

Include `skill_name`, `skill_version`, `scope`, `input_paths`, `output_path`, `critical_tasks`, `blockers`, `evidence_status`, `upstream_owner`, and `next_role`.
