# kang-b2b-ux-auditor

[![status](https://img.shields.io/badge/status-public%20release-2ea44f)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![version](https://img.shields.io/github/v/release/KanG-ciyuan/kang-b2b-ux-auditor?label=version)](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor/releases)
[![tests](https://img.shields.io/badge/contract%20tests-3-2ea44f)](tests/)
[![license](https://img.shields.io/badge/license-MIT-6f42c1)](LICENSE)

Kang 的通用 B2B UX 审查数字员工 Skill。适用于 SaaS、内部工具、工作流和运营后台，检查用户能否理解为什么进入、现在做什么、何时完成、交给谁，以及异常和权限状态如何恢复。

调用：`$kang-b2b-ux-auditor`

输入：目标用户、核心任务、产品表面和可运行或可检查的证据。输出：任务路径、状态矩阵、证据定位、严重度和可验证改进。它不做后端实现，也不替业务确认事实。

## 你可以直接这样说

“使用 `$kang-b2b-ux-auditor` 检查客服工单台是否能让新人完成转派、批量处理和失败恢复。”

## 安装与验证

```bash
npx skills add KanG-ciyuan/kang-b2b-ux-auditor
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/kang-b2b-ux-auditor
python3 ~/.codex/skills/kang-meta-skill/scripts/validate_skill.py ~/.codex/skills/kang-b2b-ux-auditor
```

## 前置条件

- [ ] 已准备目标用户、核心任务和页面/运行证据
- [ ] 已确认不修改代码
- [ ] 已确认视觉建议不能替代任务路径判断

## Troubleshooting

如果任务、用户或运行证据缺失，标记 `to_verify` 或停止；不要用颜色偏好、按钮可见或 API 200 掩盖任务问题。

## License

MIT. See [LICENSE](LICENSE). This is a reusable product-development agent Skill, separate from any private enterprise product.

<!-- kang-author:start -->
## About Kang

Maintained by Kang. GitHub: https://github.com/KanG-ciyuan/

<!-- kang-author:end -->
