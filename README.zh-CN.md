# Kang B2B UX Auditor

[English](README.md) | 简体中文

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-b2b-ux-auditor?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-b2b-ux-auditor?style=flat-square)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/commits/main)

> 审查企业用户能不能真正理解并完成工作，而不是界面看起来够不够漂亮。

这是一个面向 AI Agent 的只读 UX 审查 Skill，适用于 B2B SaaS、内部工具、工作流产品和运营后台。它审查首屏、角色导航、任务路径、表格、筛选、抽屉、批量操作、响应式行为，以及 loading、empty、error、waiting、stale、conflict、permission 这些决定任务能否真正完成的状态。

它的实现是提示词文本而不是代码：`SKILL.md`（`manifest.json` 声明的 entrypoint）加一份参考文档 [`references/ux-rubric.md`](references/ux-rubric.md)。本仓库不包含审查引擎、不包含脚本、不包含任何自动化，也不包含任何示例审查结果。依赖它之前请先读 [状态与限制](#状态与限制)。

## 为什么需要它

企业界面很少是因为少了一个按钮而失败。它失败的真正原因是：用户说不清自己为什么在这个页面上、下一步该做什么、什么算做完、结果交给谁。这类问题能通过评审，因为一张漂亮的截图和一个返回 `200` 的接口看起来都像成功，而这两者都不能证明一个新来的运营能把手上的活干完。

设计偏好很容易争论，也很难有结论；任务能否完成却是可检验的。这个 Skill 把评审拉回到可检验的问题上，并要求每条建议都说明它背后的任务失败或理解成本（`references/ux-rubric.md`）。

## 对比：外观结论与任务结论

下表的对照是本 README 对这个 Skill 规则的解释，不是仓库里的原文框架；右侧每一行规则都能追溯到 `SKILL.md` 或 `references/ux-rubric.md`。

| 停留在外观的评审结论 | 本项目要求给出什么 |
| --- | --- |
| "工具栏太挤了。" | 具体卡住哪一个任务步骤、影响哪个角色、`evidence_status` 是什么，以及能证明修好的 `success_signal`。纯外观问题最高只能是 `low`。 |
| "按钮在，所以流程没问题。" | 不会因为界面好看、按钮可见或接口返回 `200` 就宣布可用性已经修好。 |
| "主流程能跑通。" | 每个任务都要对照十二状态矩阵检查；一个状态如果没有说明、下一步动作、归属方或安全重试，就不算完成。 |
| "用户好像有点困惑。" | 先记录观察到的困惑或失败，观察发生在哪一步也要写进 finding。 |
| "这是个权限 bug。" | 权限、业务规则、流程归属问题会中止审查，升级给产品架构或流程审查。 |

这并不意味着视觉质量不重要。这条规则是严重度上限，不是对设计的判决：纯外观问题不能被评为 `high` 或 `blocker`，它迫使审查者说清任务后果，而不是陈述个人偏好。真正阻塞任务完成的视觉缺陷，按普通 finding 一样评级。

## 工作方式

方法是「四问任务透镜」加「十二状态矩阵」。

**1. 四问任务透镜。** 对每个被审查的产品表面，先定义一个主任务，再回答四个问题——用仓库自己的说法是 "why here, do what now, what counts as done, and who receives the result"（`SKILL.md`）。`reports/creation-handoff.md` 把同一组问题称为 "the four-question task lens"。

| 问题 | 它要确定什么 |
| --- | --- |
| why here | 用户能看懂这个页面为什么存在、自己为什么在这里 |
| do what now | 对这个角色来说，下一步动作是否只有一种合理解释 |
| what counts as done | 完成信号是否可见、是否有意义 |
| who receives the result | 交接对象和下游归属方是否清楚 |

透镜是四个问题。权限、当前状态、恢复这类关注点在本项目中以**状态矩阵条目**的形式存在，从不以额外问题的形式出现。

**2. 十二状态矩阵。** 每个任务都要检查——或显式标记为未检查——以下十二个状态（`references/ux-rubric.md`）：

`first_visit` · `loading` · `saving` · `success` · `validation_error` · `server_error` · `empty` · `waiting` · `stale` · `conflict` · `permission_denied` · `recovery`

一个状态如果没有说明、下一步动作、归属方或安全重试行为，就不算完成。这正是"主流程能跑通"不能作为审查结论的原因：`permission_denied` 和 `recovery` 本身就在必查范围内。

**3. 先证据、后改版。** 每条 finding 必须带三个证据标签之一（`references/ux-rubric.md`）：

| 标签 | 含义 |
| --- | --- |
| `confirmed` | 在可运行路径、可复现录屏或已获批准的用户研究中直接观察到 |
| `inferred` | 对界面或所给反馈的合理解读，仍需确认 |
| `to_verify` | 状态、设备、用户或行为证据缺失、过期或相互矛盾 |

<details>
<summary><strong>方法步骤、严重度分级、任务成功记录与 B2B 交互检查项</strong></summary>

**方法步骤**（`SKILL.md`）

1. 为每个被审查的产品表面定义一个主任务：why here、do what now、what counts as done、who receives the result。
2. 从干净入口走最短的真实路径，包含中断后的重新进入。
3. 检查角色相关导航、信息层级、文案、控件、密度、表格、筛选、抽屉、批量操作、键盘/焦点和响应式行为。
4. 实际触发或检查 loading、saving、success、validation error、server error、empty、waiting、stale、conflict、permission 和 recovery 状态。
5. 在提出改版方案之前，先记录观察到的困惑或失败。
6. 应用 UX Rubric，按任务影响排序，并把上游架构或流程缺陷转给对应角色。

**严重度分级**（`references/ux-rubric.md`）

- `blocker`：关键任务无法完成、用户对重要结果产生误解，或权限边界不安全。
- `high`：核心任务需要开发人员解释、很可能导致错误操作，或没有支持就无法恢复。
- `medium`：任务能完成，但反复出现歧义、步骤过多，或缺少非关键反馈。
- `low`：局部文案、对齐、密度或外观问题，对任务没有实质影响。

**任务成功记录**（`references/ux-rubric.md`）——对每个用户和任务记录：entry state、intent、first action、path、decision points、completion signal、handoff、recovery path 和 evidence。只有当用户能执行预期动作、理解其结果，并且能重新进入而不丢失或重复工作时，才算成功。

**B2B 交互检查项**（`references/ux-rubric.md`）

- 角色相关导航只暴露该角色相关的工作，并让不可用的工作可以被理解；
- 每个屏幕上有一个主任务，在视觉和文案上都清晰；
- 表格支持扫描、排序、筛选、选择和查看详情，且不丢失上下文；
- 抽屉和弹窗保持方向感，并有明确的关闭/保存/取消结果；
- 批量操作说明范围、确认、进度、部分失败，以及在安全时提供撤销；
- 响应式布局保持任务可达，不隐藏关键状态；
- 标签描述用户概念，而不是内部阶段名；
- 焦点、键盘、对比度、点击区域和文本适配满足目标环境要求。

</details>

## 核心能力

被审查的产品表面，以及每个表面上要看什么：

| 产品表面 | 检查内容 |
| --- | --- |
| 首屏 | 每个屏幕是否有一个在视觉和文案上都清晰的主任务 |
| 角色导航 | 每个角色是否只看到相关工作，不可用的工作是否有解释 |
| 任务路径 | 从干净入口出发的最短真实路径，包含中断后的重新进入 |
| 表格与筛选 | 在不丢失上下文的前提下完成扫描、排序、筛选、选择和查看详情 |
| 抽屉与弹窗 | 是否保持方向感，是否有明确的关闭 / 保存 / 取消结果 |
| 批量操作 | 范围、确认、进度、部分失败，以及安全时的撤销 |
| 响应式行为 | 各视口下任务是否仍然可达，关键状态是否被隐藏 |
| 文案与标签 | 标签描述的是用户概念，还是内部阶段名 |
| 非顺利路径状态 | loading、empty、error、waiting、stale、conflict、permission、recovery |

## 输出与产物

这个包定义了一份输出契约，但没有随包提供任何已产出的输出。

| 声明的产物 | 定义位置 | 本仓库中是否存在 |
| --- | --- | --- |
| 范围与证据登记 | `SKILL.md` | 否——只有 schema |
| 角色 / 任务矩阵 | `SKILL.md` | 否——只有 schema |
| 首屏与路径 finding | `SKILL.md` | 否——只有 schema |
| 状态矩阵 | `SKILL.md`、`references/ux-rubric.md` | 否——只有 schema |
| 导航与文案建议 | `SKILL.md` | 否——只有 schema |
| 按优先级排序的 finding | `SKILL.md` | 否——只有 schema |
| 建议的验证场景 | `SKILL.md` | 否——只有 schema |
| 下游交接 | `SKILL.md`、`references/ux-rubric.md` | 否——只有 schema |

每条 finding 必须包含十个字段（`SKILL.md`）：`id`、`severity`、`evidence_status`、`source_or_step`、`affected_user`、`task_impact`、`observed_issue`、`recommendation`、`success_signal`、`owner`。

下游交接包含十个字段（`references/ux-rubric.md`）：`skill_name`、`skill_version`、`scope`、`input_paths`、`output_path`、`critical_tasks`、`blockers`、`evidence_status`、`upstream_owner`、`next_role`。

**本仓库中不存在任何审查输出。** 没有示例报告、没有 golden file、没有截图、没有 fixture 输出。仓库里唯一实体化的产物是 `reports/trigger-eval.json` 和 `reports/skill-ir.json`，两者都是包元数据，不是 UX 审查结果。schema 的文本形式见 [示例](#示例)。

## 证据与验证

以下内容都实际运行过，结果按观察到的原样陈述。它们都不验证审查行为本身。

| 检查项 | 命令 | 结果 |
| --- | --- | --- |
| 包契约测试 | `python3 -m unittest discover -s tests -v` | `Ran 3 tests` — `OK`，退出码 0 · **VERIFIED** |
| trigger fixtures | `trigger_eval.py . --cases evals/trigger_cases.json`，再与 `reports/trigger-eval.json` 做 `diff` | 逐字节一致；阈值 `0.3` 下 11/11 · **VERIFIED** |
| 包校验（外部工具） | `quick_validate.py`（`skill-creator`）与 `scripts/validate_skill.py`（`kang-meta-skill`），针对已安装副本运行 | 均退出码 0，无 failure，无 warning · **VERIFIED** |

这三项结果需要按它们的实际含义来读：

- **测试是包契约测试，不是行为测试套件。** 三个测试只断言文件存在、以及某些字符串出现在 `SKILL.md` 和 `references/ux-rubric.md` 中。没有任何一个测试真正执行审查，也没有任何一个测试校验 UX finding。把 rubric 正文全部删掉、只留四个标题，测试仍然会通过。
- **trigger 报告是关键词匹配器。** runner 用概念关键词组（`ux`、`task`、`role`、`states`）与 skill description 和 prompt 的重叠度打分，阈值 `0.3`，并配硬性负向模式（例如 `只评价颜色`）。它从不调用模型。通过只说明关键词对得上，不说明这个 Skill 在真实 Agent 里能被正确触发。
- **没有任何东西自动运行。** 本仓库没有 CI——没有 `.github/` 目录，没有 workflow。上面每一项检查都是手工运行的。

| 未验证项 | 状态 |
| --- | --- |
| output contract evaluation | **TO_VERIFY**——`evals/output_cases.json` 只有 1 个 case（`input_files: []`）和 4 条自由文本断言。本仓库和 `kang-meta-skill` 中都不存在对应的 runner，也没有任何执行记录——但 `manifest.json` 把 "output contract evaluation" 列为 release gate。 |
| 安装 | **TO_VERIFY**——见 [快速开始](#快速开始)。 |
| 在真实产品上的审查行为 | **TO_VERIFY**——仓库中不存在任何审查输出、截图、对话记录或用户反馈。`reports/creation-handoff.md` 明确写着 provider-backed 和人工可用性证据缺失。 |
| 多平台 adapter | **TO_VERIFY**——`agents/interface.yaml` 声明四个 adapter target，`manifest.json` 只声明两个，且不存在 adapter 代码或测试。 |

## 状态与限制

**声明的状态：`public-release-candidate`**（`manifest.json`）。`reports/creation-handoff.md` 对同一个包的说法是 "a public release candidate pending release evidence"。本 README 采用仓库自己的说法，而不写 "public release"。

| 项目 | 值 |
| --- | --- |
| 版本 | `0.2.0`，在 `SKILL.md`、`manifest.json`、`reports/skill-ir.json` 和 `tests/test_contract.py` 中一致 |
| Release | `v0.2.0`，发布于 2026-08-22，非 prerelease |
| Release 与 `main` 的关系 | `main` 比 `v0.2.0` tag 多一个提交（`v0.2.0-1-g00d539e`），因此该 release 并不指向当前分支顶端 |
| 许可证 | MIT（`LICENSE`、`manifest.json`） |

`manifest.json` 记录 `"maturity_tier": "production"`，但仓库里没有任何东西能支撑这一成熟度作为行为层面的结论：没有运行过或记录过任何审查，output contract evaluation 没有 runner，包自己的交接报告也写明 provider-backed 和人工可用性证据缺失。**本 README 不主张 production 成熟度。**

已知限制：

- 没有可执行的审查引擎，没有脚本，没有 CI。
- 没有任何示例审查、截图或 UI fixture；仓库中图片文件数为 0——尽管这个 Skill 会把截图作为支持性输入。
- 契约测试校验的是包结构，不是审查行为。
- `reports/skill-ir.json` 声明 `inputs`、`outputs`、`exclusions` 为空，与 `SKILL.md` 矛盾。请以 `SKILL.md` 和 `references/ux-rubric.md` 作为能力事实来源。
- adapter 支持只是声明的元数据，不是经过测试的能力。
- 这个包没有定义任何数据范围、PII、脱敏或留存规则。"read-only" 和 "write only the assigned UX artifact" 是它唯一声明过的处理约束。

## 示例

**本节没有任何内容来自真实审查。** 本仓库没有执行过、也没有记录过任何一次审查。下面给出的是取自已记录 trigger fixtures 的调用形态，以及取自输出契约的 schema，用来说明这个 Skill 被要求产出什么。

一条调用，来自已记录的 fixture 集合（`evals/trigger_cases.json`）：

> 审查内容编辑 UX 从草稿到法务审阅的任务路径和失败恢复

一条 finding 的字段骨架——十个必填字段（`SKILL.md`）。字段名是契约本身；前三行给出的取值是允许的枚举值，不是观察到的值：

```yaml
id: <稳定的 finding id>
severity: blocker | high | medium | low
evidence_status: confirmed | inferred | to_verify
source_or_step: <观察到的步骤或证据来源>
affected_user: <任务失败的角色>
task_impact: <任务的哪一部分失败，以及如何失败>
observed_issue: <观察到的现象，记录在提出改版之前>
recommendation: <改动建议，绑定到该任务失败>
success_signal: <什么能证明已经修好>
owner: <谁来修>
```

审查最后以一个交接块结束，包含 `skill_name`、`skill_version`、`scope`、`input_paths`、`output_path`、`critical_tasks`、`blockers`、`evidence_status`、`upstream_owner` 和 `next_role`（`references/ux-rubric.md`）。

## 适用与不适用

**适用场景**

- B2B SaaS、内部工具、工作流或运营后台需要在发布前后做一次任务理解度审查；
- 要回答的问题是：某个角色的新用户，能不能在没人解释内部标签的情况下完成某个具体任务；
- 需要的是能指出任务失败和成功信号的 finding，而不是设计偏好；
- 能提供可运行路径、截图、HTML/CSS/JS、录屏或用户反馈作为审查对象。

**不适用场景**

- 只评价视觉品味（`SKILL.md` frontmatter）；
- 后端实现（`SKILL.md` frontmatter）；
- 业务流程归属（`SKILL.md` frontmatter）；
- 权限、业务规则、流程归属的判断——这些会中止审查并升级给产品架构或流程审查；
- 没有明确用户、任务或证据来源的对象——此时审查会停止，或只返回受限的产物审查，绝不从视觉打磨程度反推任务。

## 安全边界与人工决策

| 规则 | 来源 |
| --- | --- |
| 默认只读；实施需要人工批准 | `manifest.json` |
| "Do not edit code." | `SKILL.md` |
| "Write only the assigned UX artifact." | `SKILL.md` |
| 当任务、角色、授权或运行证据缺失时停止 | `SKILL.md` |
| 权限、业务规则、流程归属问题升级给产品架构或流程审查 | `SKILL.md` |
| 先记录观察到的困惑或失败，再提出改版 | `SKILL.md` |
| 每条 finding 必须带 `evidence_status` 和 `source_or_step` | `SKILL.md` |
| "Visual preference alone cannot be `high` or `blocker`." | `references/ux-rubric.md` |
| "Do not declare usability fixed because a screen is attractive, a button is visible, or an API returns 200." | `SKILL.md` |

这个包在 `reports/skill-ir.json` 中还带有一条明确的证据边界策略：生成的报告算证据、计划中的工作不算证据、缺失外部或人工证据时标注 "missing evidence"，公开主张只能陈述本地验证、安装证明、人工评审或 provider-backed 证据真正支持的内容。

**不存在数据范围规则。** 这个包没有对客户数据、PII、脱敏，或什么东西可以被复制进审查产物作出任何规定。请把它当作一个待补的缺口，而不是一种默认许可——在把它指向生产数据之前先补上。

## 快速开始

**1. 准备必需输入**（`SKILL.md`）：目标用户、他们的任务和完成信号、相关产品表面，以及可运行或可检查的证据来源。截图、HTML/CSS/JS、录屏、用户反馈和无障碍约束属于支持性输入。

**2. 安装。** 这个包此前的 README 记录了这条命令：

```bash
npx skills add KanG-ciyuan/kang-b2b-ux-auditor
```

它在本次仓库审查中**没有被执行**——该命令需要 registry 访问且会改动本地环境——所以安装仍是 **TO_VERIFY**。本仓库不包含安装脚本，也没有依赖清单。

**3. 调用。** `$kang-b2b-ux-auditor`。记录输入路径、输出路径、设备和视口，以及本次审查是运行时审查还是仅产物审查。

**4. 在本地验证这个包。**

```bash
python3 -m unittest discover -s tests -v
```

在本工作副本上的结果：`Ran 3 tests` — `OK`，退出码 0。[`tests/test_contract.py`](tests/test_contract.py) 是包契约测试，不是行为测试套件；详见 [证据与验证](#证据与验证)。

**5. 复现 trigger 报告。** runner 位于另一个包 `kang-meta-skill`，没有 vendor 到本仓库，因此路径依环境而定：

```bash
python3 <path-to-kang-meta-skill>/scripts/trigger_eval.py . --cases evals/trigger_cases.json > /tmp/repro.json
diff /tmp/repro.json reports/trigger-eval.json    # 无输出即逐字节一致
```

**6. 校验包结构。** 针对本包的已安装副本运行过两个外部校验器——`skill-creator` 的 `quick_validate.py`，以及 `kang-meta-skill` 的 `scripts/validate_skill.py`。两者都以退出码 0 结束，无 failure，无 warning。这两个工具位于其他仓库，本 README 不固定它们的路径。

---

## 属于 Kang 开源 AI 体系

本项目是「面向企业 AI 转型、Agent 协作与 AI 原生产品交付的证据驱动体系」的一部分。

| 阶段 | 项目 | 作用 |
| --- | --- | --- |
| DISCOVER 发现 | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | 在自动化之前，先弄清企业真实业务如何运行 |
| DEFINE 定义 | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | 把模糊需求转化为可实施、可审查的产品契约 |
| DEFINE 定义 | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | 审查流程是否可执行、可追责、可恢复 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | 角色化的 Agent 数字员工团队与显式交接 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent 协作与交接协议 |
| BUILD & COORDINATE 构建与协同 | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | AI 构建界面的前端质量标准 |
| VERIFY 验证 | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | 用户能否真正把工作做完 |
| VERIFY 验证 | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | AI 构建产品的独立验收 |
| DELIVER 交付 | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | 证据感知的 README 工程 |
| DELIVER 交付 | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | 证据感知的演示文稿设计 |

**横向基础设施：** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill 工程化、评估与发布治理。

**早期工作：** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules)、
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps)、
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent)。

### 生态地图

```text
发现 DISCOVER
企业 AI 诊断 Skills
        ↓
定义 DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
构建与协同 BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
验证 VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
交付 DELIVER
Kang GitHub README
Kang PPT Skill
```

> 这是一张生态地图，不是严格的运行时流水线。各阶段描述的是项目所处的工作位置，
> 而不是强制的执行顺序。

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->

## 开源许可证

本项目采用 [MIT License](LICENSE) 开源。
