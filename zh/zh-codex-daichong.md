---
title: "Codex 代充怎么选：加点数、开 Plus 还是升 Pro（对照表 + 常见问题）"
lang: zh-CN
---
# Codex 代充怎么选：加点数、开 Plus 还是升 Pro（对照表 + 常见问题）

搜“Codex 代充”的人，情况其实不一样：有人还在免费版，想正经用 Codex；有人开着 Plus，写到一半提示用量到上限；也有人 Codex 走的是 API key，充了半天发现不管用。要买的东西不同，先对一下自己是哪种。

本文的套餐规则按 OpenAI 帮助中心核对，日期 2026 年 11 月 15 日。

## 先对号入座

| 你现在的情况 | 该买什么 | Pay2GPT 价格（银行卡 / 支付宝） |
|---|---|---|
| 免费版或 Go，偶尔让 Codex 写点脚本 | 先不用买。Codex 各套餐都能用，免费版和 Go 也有，只是用量少，也没有 Codex Cloud | — |
| 免费版或 Go，想每天用、想跑云端任务 | 开 Plus | $25.10 / 月 |
| Plus，赶项目那几天撞上限 | 加 Codex 点数 | 250 点 $15.65 起 |
| Plus，几乎每周都撞上限 | 升 Pro 100 | $131.15 / 月 |
| Pro 还不够用 | 加点数，或换 Pro 200、Pro 500 | 见下表 |
| Codex 用 API key 登录 | 点数和会员都不管用，费用记在 OpenAI API 账户上 | 我们不卖 API 余额 |

最后一行最容易踩坑。在终端跑 `codex login status`，显示用 ChatGPT 登录，才是在用会员额度。用过中转站或 CC Switch 的，先切回 ChatGPT 官方登录再买。

## Codex 点数各档价格

| 点数 | 银行卡 / 支付宝 | USDT / USDC |
|---|---|---|
| 250 | $15.65 | $14.90 |
| 500 | $29.30 | $27.90 |
| 1000 | $52.40 | $49.90 |
| 2500 | $113.30 | $107.90 |
| 5000 | $225.65 | $214.90 |

支付宝付款时，人民币金额在付款前会显示。

## 点数怎么扣

按 OpenAI 的说明，Plus 和 Pro 上先用套餐自带的用量，用完才从点数里扣，套餐本身不变。Codex、ChatGPT Work、Excel、PowerPoint 共用同一份额度，所以 Work 用得多，Codex 剩得就少。

扣得快慢看模型、上下文、推理量和速度档。OpenAI 写明 Fast 档按标准速率的 2.5 倍消耗额度，Ultrafast 是 8 倍，而且只有 Pro 500 有 Ultrafast。默认开着 Fast 的，关掉能多撑一阵。

几个任务并行跑的时候，余额可能被扣成负数：任务开始时余额是正的，跑完时已经被别的任务用光了。下次买点数会先补上负数部分。

## 在 Pay2GPT 加点数

1. 在 [Pay2GPT](https://pay2gpt.com/codex-credits?utm_source=github_pages&utm_campaign=offsite) 选点数，用支付宝、银行卡或 USDT 付款，不用注册，留个邮箱。
2. 在订单页粘贴 ChatGPT Session。页面会先显示账号和当前套餐，确认后才加，全程不要密码。
3. 一般几分钟到账，页面实时更新，也会发邮件。余额在 ChatGPT → 设置 → 用量里看，Codex 应用里是 Usage & Billing；终端里输 `/status`。

## 常见问题

### Go 或免费版能加点数吗？

通过 Pay2GPT 不行。点数要加在已开通、在有效期内的 Plus 或 Pro 个人版上；免费版、Go 和 Business 工作区账号加不了。先开 Plus 再加。

### 加点数会改我的套餐或续费日期吗？

不会。点数叠加在套餐上，套餐和续费日期都不动。

### 点数多久过期？

购买后 12 个月。没用完的不结转。

### 能不能让 OpenAI 客服帮我重置额度？

不能。OpenAI 帮助中心写明客服不能重置 ChatGPT 或 Codex 的用量上限，只会排查计算错误。等恢复、加点数、升 Pro 是仅有的几条路。

### 点数能当 API 额度用吗？

不能。点数只在 ChatGPT 和 Codex 里用，API key 登录的 Codex 用不上。

### 加点数还是升 Pro，怎么算？

偶尔超一点，加点数，一次付款，用多少扣多少。几乎每周都撞上限，或者经常一连几个小时跑 Codex，升 Pro 更合适，每个月自带的用量多得多。Pro 各档的区别见 [pay2gpt.com](https://pay2gpt.com/blog/pro?utm_source=github_pages&utm_campaign=offsite)。

## 参考

以下 OpenAI 帮助中心页面于 2026 年 11 月 15 日核对，规则以官方最新说明为准：

- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- [Using Credits for Flexible Usage in ChatGPT](https://help.openai.com/en/articles/12642688)
- [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro)

Pay2GPT 是独立的代充服务，和 OpenAI 没有隶属关系。
