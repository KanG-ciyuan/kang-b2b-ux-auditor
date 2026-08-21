# kang-b2b-ux-auditor

[![status](https://img.shields.io/badge/status-public%20release-2ea44f)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![version](https://img.shields.io/github/v/release/KanG-ciyuan/kang-b2b-ux-auditor?label=version)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![tests](https://img.shields.io/badge/local%20tests-1%20passed-2ea44f)](tests/)
[![license](https://img.shields.io/badge/license-Kang%20terms-6f42c1)](LICENSE)

Kang 的 B2B SaaS UX 审查 Skill。用于检查不同角色能否理解“为什么进入、现在做什么、何时完成、交给谁”，以及状态反馈和权限导航是否清楚。

调用：`$kang-b2b-ux-auditor`

输入：架构和流程交接、页面代码或截图、用户反馈。输出：按角色和严重度排序的 UX 审查。它不做后端实现，也不替业务确认事实。

## 你可以直接这样说

“使用 `$kang-b2b-ux-auditor` 检查每个角色是否知道为什么进入、现在做什么和完成后交给谁。”

## 安装与验证

```bash
npx skills add KanG-ciyuan/kang-b2b-ux-auditor
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/kang-b2b-ux-auditor
python3 ~/.codex/skills/kang-meta-skill/scripts/validate_skill.py ~/.codex/skills/kang-b2b-ux-auditor
```

## 前置条件

- [ ] 已准备架构/流程交接和页面证据
- [ ] 已确认不修改代码
- [ ] 已确认视觉建议不能替代任务路径判断

## Troubleshooting

如果页面需要开发者解释才能使用，直接记录为 UX 阻塞，不要用视觉偏好掩盖问题。

## License

Copyright (c) Kang. See [LICENSE](LICENSE).

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->

