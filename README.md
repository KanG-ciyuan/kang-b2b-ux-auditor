# Kang B2B UX Auditor

English | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-b2b-ux-auditor?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-b2b-ux-auditor?style=flat-square)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/commits/main)

> Audit whether enterprise users can actually understand and complete their work — not whether the interface merely looks polished.

A read-only UX audit Skill for AI agents, aimed at B2B SaaS, internal tools, workflow products, and operational interfaces. It reviews first viewport, role navigation, task paths, tables, filters, drawers, bulk actions, responsive behavior, and the loading, empty, error, waiting, stale, conflict, and permission states that decide whether a task actually completes.

The implementation is prompt text, not code: `SKILL.md` (the entrypoint declared in `manifest.json`) plus one reference document, [`references/ux-rubric.md`](references/ux-rubric.md). This repository ships no audit engine, no scripts, no automation, and no example audit output. Read [Status and Limitations](#status-and-limitations) before depending on it.

## Why

Enterprise interfaces rarely fail because a control is missing. They fail because a user cannot tell why they are on a screen, what to do next, when the task counts as done, or who receives the result. Those failures survive review, because an attractive screenshot and an API returning `200` both look like success — and neither one proves that a new operator can finish the job.

Design debate is easy to start and hard to settle. Task completion is testable. This package moves the review onto the testable question and forces every recommendation to name the task failure or comprehension risk behind it (`references/ux-rubric.md`).

## Before / After

The contrast below is this README's own explanation of the package's rules, not a quoted framework from the repository. Every "required instead" rule is traceable to `SKILL.md` or `references/ux-rubric.md`.

| A review that stops at appearance | What this package requires instead |
| --- | --- |
| "The toolbar feels cluttered." | A named task step, the role it blocks, an `evidence_status`, and the `success_signal` that would prove it fixed. A purely aesthetic issue stays `low`. |
| "The button is visible, so the flow works." | Usability is never declared fixed because a screen is attractive, a button is visible, or an API returns `200`. |
| "The happy path works." | Every task is checked against a twelve-state matrix. A state is not complete without an explanation, a next action, an owner, or safe retry behavior. |
| "Users seem confused." | Observed confusion or failure is recorded first, and the step where it was observed becomes part of the finding. |
| "That is a permission bug." | Permission, business-rule, and process-ownership questions stop the audit and escalate to architecture or process review. |

None of this dismisses visual quality. The rule is a severity ceiling, not a verdict on design: a purely aesthetic issue cannot be rated `high` or `blocker`, which forces the reviewer to state the task consequence instead of asserting a preference. A visual defect that genuinely blocks completion is rated like any other finding.

## How It Works

The method is a four-question task lens plus a twelve-state matrix.

**1. The four-question task lens.** For each audited surface the auditor defines one primary task and answers four questions — in the repository's own wording, "why here, do what now, what counts as done, and who receives the result" (`SKILL.md`). `reports/creation-handoff.md` names the same set "the four-question task lens".

| Question | What it decides |
| --- | --- |
| why here | the user can tell why this surface exists and why they are on it |
| do what now | the next action is unambiguous for this role |
| what counts as done | the completion signal is visible and meaningful |
| who receives the result | the handoff recipient and downstream owner are clear |

The lens is four questions. Concerns such as permission, current state, and recovery appear in this package as **state-matrix entries**, never as additional questions.

**2. The twelve-state matrix.** Every task is inspected — or explicitly marked — across twelve states (`references/ux-rubric.md`):

`first_visit` · `loading` · `saving` · `success` · `validation_error` · `server_error` · `empty` · `waiting` · `stale` · `conflict` · `permission_denied` · `recovery`

A state is not complete if it has no explanation, next action, ownership, or safe retry behavior. This is why "the happy path works" is not an acceptable result: `permission_denied` and `recovery` are inside the required scope.

**3. Evidence before redesign.** Every finding carries one of three evidence labels (`references/ux-rubric.md`):

| Label | Meaning |
| --- | --- |
| `confirmed` | directly observed in a runnable path, reproducible recording, or approved user research |
| `inferred` | a reasoned interpretation of the interface or supplied feedback that needs confirmation |
| `to_verify` | state, device, user, or behavior evidence is absent, stale, or contradictory |

<details>
<summary><strong>Method steps, severity scale, task-success record, and the B2B interaction checks</strong></summary>

**Method steps** (`SKILL.md`)

1. Define one primary task per audited surface: why here, do what now, what counts as done, and who receives the result.
2. Walk the shortest realistic path from a clean entry, including re-entry after interruption.
3. Check role-specific navigation, information hierarchy, copy, controls, density, tables, filters, drawers, bulk actions, keyboard/focus and responsive behavior.
4. Exercise or inspect loading, saving, success, validation error, server error, empty, waiting, stale, conflict, permission, and recovery states.
5. Record observed confusion or failure before suggesting a redesign.
6. Apply the UX Rubric, prioritize by task impact, and route upstream architecture or process defects to the correct role.

**Severity scale** (`references/ux-rubric.md`)

- `blocker`: a critical task cannot be completed, the user is misled about a consequential result, or a permission boundary is unsafe.
- `high`: a core task requires developer explanation, causes likely wrong action, or cannot recover without support.
- `medium`: the task can complete but has repeated ambiguity, excess steps, or missing non-critical feedback.
- `low`: local wording, alignment, density, or aesthetic issue with no material task impact.

**Task-success record** (`references/ux-rubric.md`) — for each user and task, record entry state, intent, first action, path, decision points, completion signal, handoff, recovery path, and evidence. A user succeeds only when they can perform the intended action, understand its result, and re-enter without losing or duplicating work.

**B2B interaction checks** (`references/ux-rubric.md`)

- role-specific navigation exposes only relevant work and makes unavailable work understandable;
- one primary task is visually and verbally clear per screen;
- tables support scan, sort, filter, selection, and detail without losing context;
- drawers and modals preserve orientation and have an explicit close/save/cancel outcome;
- bulk actions state scope, confirmation, progress, partial failure, and undo where safe;
- responsive layouts preserve task access and do not hide critical states;
- labels describe user concepts, not internal stage names;
- focus, keyboard, contrast, touch targets, and text fit are adequate for the target environment.

</details>

## Core Capabilities

Reviewed surfaces and what the auditor looks for on each:

| Surface | What is examined |
| --- | --- |
| First viewport | whether one primary task per screen is visually and verbally clear |
| Role navigation | whether each role sees relevant work, and whether unavailable work is explained |
| Task path | the shortest realistic path from a clean entry, including re-entry after interruption |
| Tables and filters | scan, sort, filter, selection, and detail access without losing context |
| Drawers and modals | orientation, and an explicit close / save / cancel outcome |
| Bulk actions | scope, confirmation, progress, partial failure, and undo where safe |
| Responsive behavior | task access preserved across viewports, with critical states not hidden |
| Copy and labels | whether labels describe user concepts or internal stage names |
| Non-happy states | loading, empty, error, waiting, stale, conflict, permission, and recovery |

## Outputs / Artifacts

The package defines an output contract. It does not ship a produced output.

| Declared artifact | Defined in | Present in this repository |
| --- | --- | --- |
| Scope and evidence register | `SKILL.md` | no — schema only |
| Persona / task matrix | `SKILL.md` | no — schema only |
| First-viewport and path findings | `SKILL.md` | no — schema only |
| State matrix | `SKILL.md`, `references/ux-rubric.md` | no — schema only |
| Navigation and copy recommendations | `SKILL.md` | no — schema only |
| Prioritized findings | `SKILL.md` | no — schema only |
| Recommended verification scenarios | `SKILL.md` | no — schema only |
| Downstream handoff | `SKILL.md`, `references/ux-rubric.md` | no — schema only |

Every finding must carry ten named fields (`SKILL.md`): `id`, `severity`, `evidence_status`, `source_or_step`, `affected_user`, `task_impact`, `observed_issue`, `recommendation`, `success_signal`, and `owner`.

The downstream handoff carries ten fields (`references/ux-rubric.md`): `skill_name`, `skill_version`, `scope`, `input_paths`, `output_path`, `critical_tasks`, `blockers`, `evidence_status`, `upstream_owner`, and `next_role`.

**No audit output exists in this repository.** There is no sample report, golden file, screenshot, or fixture output. The only materialized artifacts are `reports/trigger-eval.json` and `reports/skill-ir.json`, and both are package metadata rather than UX audit results. See [Example](#example) for the schema as text.

## Evidence / Validation

Everything below was run and its result is stated as observed. None of it validates audit behavior.

| Check | Command | Result |
| --- | --- | --- |
| Package contract tests | `python3 -m unittest discover -s tests -v` | `Ran 3 tests` — `OK`, exit 0 · **VERIFIED** |
| Trigger fixtures | `trigger_eval.py . --cases evals/trigger_cases.json`, then `diff` against `reports/trigger-eval.json` | byte-identical; 11/11 at threshold `0.3` · **VERIFIED** |
| Package validation (external) | `quick_validate.py` (`skill-creator`) and `scripts/validate_skill.py` (`kang-meta-skill`), run against an installed copy | both exit 0, no failures, no warnings · **VERIFIED** |

Read those three results for what they are:

- **The tests are package contract tests, not a behavioral suite.** All three assert that files exist and that strings appear in `SKILL.md` and `references/ux-rubric.md`. None executes an audit, and none validates a UX finding. Deleting the body of the rubric while keeping its four headings would still pass.
- **The trigger report is a keyword matcher.** The runner scores overlap between concept keyword groups (`ux`, `task`, `role`, `states`) and the skill description and prompts, against a threshold of `0.3`, with hard negative patterns such as `只评价颜色`. It never invokes a model. Passing proves the vocabulary lines up; it does not prove the skill triggers correctly in a live agent.
- **Nothing runs automatically.** There is no CI here — no `.github/` directory, no workflow. Every check above was run by hand.

| Unverified item | Status |
| --- | --- |
| Output-contract evaluation | **TO_VERIFY** — `evals/output_cases.json` holds exactly one case (`input_files: []`) with four free-text prose assertions. No runner for it exists in this repository or in `kang-meta-skill`, and no record of execution exists — yet `manifest.json` lists "output contract evaluation" as a release gate. |
| Installation | **TO_VERIFY** — see [Quick Start](#quick-start). |
| Audit behavior on a real product | **TO_VERIFY** — no audit output, screenshot, transcript, or user feedback exists in the repository. `reports/creation-handoff.md` states that provider-backed and human usability evidence are missing. |
| Multi-platform adapters | **TO_VERIFY** — `agents/interface.yaml` declares four adapter targets while `manifest.json` declares two, and no adapter code or test exists. |

## Status and Limitations

**Declared status: `public-release-candidate`** (`manifest.json`). `reports/creation-handoff.md` calls the same package "a public release candidate pending release evidence". This README uses that wording rather than "public release".

| Item | Value |
| --- | --- |
| Version | `0.2.0`, consistent across `SKILL.md`, `manifest.json`, `reports/skill-ir.json`, and `tests/test_contract.py` |
| Release | `v0.2.0`, published 2026-08-22, not a prerelease |
| Release vs `main` | `main` is one commit past the `v0.2.0` tag (`v0.2.0-1-g00d539e`), so the release does not point at the current tip |
| License | MIT (`LICENSE`, `manifest.json`) |

`manifest.json` records `"maturity_tier": "production"`, but nothing in the repository supports that tier as a behavioral claim: no audit has been run or recorded, the output-contract evaluation has no runner, and the package's own handoff report states that provider-backed and human usability evidence are missing. **This README does not claim production maturity.**

Known limitations:

- No executable audit engine, no scripts, and no CI.
- No sample audit, screenshot, or UI fixture of any kind; the repository contains zero image files, although the skill consumes screenshots as supporting input.
- The contract tests validate package structure, not audit behavior.
- `reports/skill-ir.json` declares empty `inputs`, `outputs`, and `exclusions`, which contradicts `SKILL.md`. Treat `SKILL.md` and `references/ux-rubric.md` as the capability source of truth.
- Adapter support is declared metadata, not tested behavior.
- The package defines no data-scope, PII, redaction, or retention rule. "Read-only" and "write only the assigned UX artifact" are the only handling constraints it states.

## Example

**Nothing in this section is output from a real audit.** No audit has been performed or recorded in this repository. What follows is the invocation shape taken from the recorded trigger fixtures, and the output schema taken from the contract, so that a reader can see what the auditor is asked to produce.

An invocation, from the recorded fixture set (`evals/trigger_cases.json`):

> 审查内容编辑 UX 从草稿到法务审阅的任务路径和失败恢复

A finding skeleton — the ten required fields (`SKILL.md`). The field names are the contract; the values shown in the first three lines are the permitted enumerations, not observed values:

```yaml
id: <stable finding id>
severity: blocker | high | medium | low
evidence_status: confirmed | inferred | to_verify
source_or_step: <the observed step or the evidence source>
affected_user: <the role that fails>
task_impact: <which part of the task fails, and how>
observed_issue: <what was observed, recorded before any redesign>
recommendation: <the change, tied to that task failure>
success_signal: <what would prove it is fixed>
owner: <who fixes it>
```

The audit then ends with a handoff block carrying `skill_name`, `skill_version`, `scope`, `input_paths`, `output_path`, `critical_tasks`, `blockers`, `evidence_status`, `upstream_owner`, and `next_role` (`references/ux-rubric.md`).

## Use / Not Use

**Use it when**

- a B2B SaaS, internal-tool, workflow, or operations surface needs a task-comprehension review before or after release;
- the question is whether a new user in a specific role can complete a specific task without a developer explaining internal labels;
- you need findings that name a task failure and a success signal rather than a design preference;
- a runnable path, screenshots, HTML/CSS/JS, a recording, or user feedback is available to audit against.

**Do not use it for**

- visual taste alone (`SKILL.md` frontmatter);
- backend implementation (`SKILL.md` frontmatter);
- business-process ownership (`SKILL.md` frontmatter);
- permission, business-rule, or process-ownership decisions — these stop the audit and escalate to architecture or process review;
- targets with no identified user, task, or evidence source — the auditor stops or returns a limited artifact audit, and never infers a task from visual polish alone.

## Safety / Human Boundary

| Rule | Source |
| --- | --- |
| Read-only by default; implementation requires human approval | `manifest.json` |
| "Do not edit code." | `SKILL.md` |
| "Write only the assigned UX artifact." | `SKILL.md` |
| Stop when the task, actor, authority, or runtime evidence is missing | `SKILL.md` |
| Escalate permission, business-rule, or process-ownership questions to architecture or process review | `SKILL.md` |
| Record observed confusion or failure before suggesting a redesign | `SKILL.md` |
| Every finding carries `evidence_status` and `source_or_step` | `SKILL.md` |
| "Visual preference alone cannot be `high` or `blocker`." | `references/ux-rubric.md` |
| "Do not declare usability fixed because a screen is attractive, a button is visible, or an API returns 200." | `SKILL.md` |

The package also carries an evidence-boundary policy in `reports/skill-ir.json`: generated reports are evidence, planned work is not, missing external or human evidence is labelled "missing evidence", and a public claim may state only what local validation, install proof, human review, or provider-backed evidence actually supports.

**No data-scope rule exists.** The package states no rule about customer data, PII, redaction, or what may be copied into an audit artifact. Treat that as a gap to close before pointing the auditor at production data, not as an implied permission.

## Quick Start

**1. Prepare the required inputs** (`SKILL.md`): the target user(s), their task and completion signal, the product surface, and a runnable or inspectable evidence source. Screenshots, HTML/CSS/JS, recordings, user feedback, and accessibility constraints are supporting inputs.

**2. Install.** The package's earlier README documents this command:

```bash
npx skills add KanG-ciyuan/kang-b2b-ux-auditor
```

It was **not executed** during the audit of this repository — it requires registry access and mutates the local environment — so installation remains **TO_VERIFY**. This repository contains no install script and no dependency manifest.

**3. Invoke.** `$kang-b2b-ux-auditor`. Record the input paths, output path, device and viewports, and whether the audit is runtime or artifact-only.

**4. Verify the package locally.**

```bash
python3 -m unittest discover -s tests -v
```

Result on this working copy: `Ran 3 tests` — `OK`, exit 0. [`tests/test_contract.py`](tests/test_contract.py) holds package contract tests, not a behavioral suite; see [Evidence / Validation](#evidence--validation).

**5. Reproduce the trigger report.** The runner lives in the separate `kang-meta-skill` package and is not vendored here, so the path is environment-specific:

```bash
python3 <path-to-kang-meta-skill>/scripts/trigger_eval.py . --cases evals/trigger_cases.json > /tmp/repro.json
diff /tmp/repro.json reports/trigger-eval.json    # no output means byte-identical
```

**6. Validate the package structure.** Two external validators were run against an installed copy of this package — `quick_validate.py` from the `skill-creator` tooling, and `scripts/validate_skill.py` from `kang-meta-skill`. Both exited 0 with no failures and no warnings. Both tools live in other repositories and are not pinned to a path here.

---

## Part of the Kang Open-Source AI System

This project is one part of an evidence-driven system for enterprise AI transformation,
agent collaboration, and AI-native product delivery.

| Stage | Project | Role |
| --- | --- | --- |
| DISCOVER | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | Understand how the business actually works before automating it |
| DEFINE | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | Turn ambiguous requirements into an implementation-ready product contract |
| DEFINE | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | Review whether workflows are executable, accountable and recoverable |
| BUILD & COORDINATE | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | Role-based AI product workforce with explicit handoffs |
| BUILD & COORDINATE | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent collaboration and handoff protocol |
| BUILD & COORDINATE | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | Frontend quality standard for AI-built interfaces |
| VERIFY | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | Can users actually finish the work? |
| VERIFY | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | Independent acceptance of AI-built products |
| DELIVER | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | Evidence-aware README engineering |
| DELIVER | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | Evidence-aware presentation design |

**Cross-cutting infrastructure:** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill engineering, evaluation and release governance.

**Earlier work:** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules),
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps),
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent).

### Ecosystem map

```text
DISCOVER
Enterprise AI Diagnostic Skills
        ↓
DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
DELIVER
Kang GitHub README
Kang PPT Skill
```

> This is an ecosystem map, not a strict runtime pipeline. The stages describe where
> each project sits in the work, not a mandatory execution order.

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->

## License

Released under the [MIT License](LICENSE).
