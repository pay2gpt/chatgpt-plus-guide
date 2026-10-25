# 没有海外卡，怎么开 ChatGPT Plus / Go / Pro

**简体中文** · [English](README.en.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

> 最后核实：2026-10-25。价格、付款方式和售后规则每月对照官网核实一次，有变化会更新这里的日期。

想给自己的 ChatGPT 账号开 Plus，结果卡在付款这一步？这份指南讲清楚三件事：卡为什么会被拒，手上没有能用的卡时有哪几条路、各自的代价是什么，以及我们 Pay2GPT 是怎么做的。哪条路适合你，看完自己判断。

## 目录

- [先看一眼：你的账号现在是什么状态](#先看一眼你的账号现在是什么状态)
- [为什么卡会被拒](#为什么卡会被拒)
- [没有能用的卡，有哪几条路](#没有能用的卡有哪几条路)
- [Pay2GPT 是怎么做的](#pay2gpt-是怎么做的)
- [价格](#价格)
- [常见问题](#常见问题)

## 先看一眼：你的账号现在是什么状态

不管走哪条路，先确认账号上有没有还在生效的订阅。订阅不能叠加，还没到期就再开一次，要么开不上，要么白花钱。

- **网页版**：登录 chatgpt.com，点左下角头像 → 设置 → 账户，能看到当前方案和续费日期。
- **之前在 iPhone 上订阅过**：订阅是 Apple 扣的，去 iPhone 的「设置 → Apple ID → 订阅」里看，取消也在那里。
- **之前在安卓上订阅过**：去 Google Play 的「付款和订阅」里看。

如果显示的是 Free，或者订阅已经到期，就可以往下看了。想自己取消订阅，参考 OpenAI 官方说明：[Canceling your ChatGPT subscription](https://help.openai.com/en/articles/7232927-how-do-i-cancel-my-chatgpt-plus-subscription)。

## 为什么卡会被拒

OpenAI 的网页结账只接受它认可的卡，被拒的原因一般就这几种：

1. **发卡行不放行**。很多国内银行默认拦境外、线上的外币扣款，带 Visa 或 Mastercard 标的卡也一样。3D 验证没弹出来或者没完成，也会直接失败。
2. **发卡国家不在支持范围**。卡的发卡行所在国家或地区不在 OpenAI 的支持列表里，付款会被拒。
3. **账单地址对不上**。填的账单地址、邮编和银行登记的不一致，风控会拦。
4. **网络位置和卡对不上**。支付风控会把卡的国家、账单地址和你当前访问的网络位置放在一起看，差得太远容易被判成高风险。

OpenAI 自己也说，它一般拿不到银行拒付的具体原因，最快的办法是直接问银行。官方说明在这里：[Why was my credit card declined?](https://help.openai.com/en/articles/7232916-why-was-my-credit-card-declined)

## 没有能用的卡，有哪几条路

| 方法 | 你付多少 | 麻烦程度 | 是不是你自己的账号 | 主要风险 |
| --- | --- | --- | --- | --- |
| 自己有海外卡 / 海外亲友代付 | 官方价 | 低 | 是 | 每个月都得靠卡或靠人 |
| App Store 礼品卡 + 外区 Apple ID | App Store 价格 + 礼品卡溢价 | 中 | 是 | 礼品卡来路不正被回收，Apple ID 余额被锁 |
| 虚拟信用卡 | 官方价 + 开卡费、充值费、汇损 | 高 | 是 | 卡段被拒，或者开卡平台跑路、冻卡 |
| 合租 / 共享账号 | 最便宜 | 低 | 否 | 被挤下线、聊天记录别人能看、号说没就没 |
| 代充服务（比如 Pay2GPT） | 官方价 + 一点服务费 | 低，几分钟 | 是 | 选到不靠谱的服务 |

### 自己有海外卡，或者请海外亲友代付

有一张 OpenAI 认的卡，直接在官网付，是最便宜的。没有的话，信得过的亲友帮你付也是官方价，没有任何中间环节。代价是对方的卡会存在你的账号上，每个月续费都得靠他，扣款失败或者忘了取消，都得你们俩自己商量。

### App Store 礼品卡 + 外区 Apple ID

在 iPhone 上用 ChatGPT App 订阅，用 Apple ID 余额付。前提是 Apple ID 的地区卖这个订阅，再买对应地区的礼品卡。订阅由 Apple 扣款，续费、取消都走 Apple，App 内的价格也可能和网页版不一样。最大的坑是礼品卡：转手买来的卡如果是盗刷来的，事后被回收，Apple ID 余额可能被直接锁掉。只从靠得住的渠道买，记录留好。

### 虚拟信用卡

开一张境外发行的虚拟卡，在官网用官方价付。适合本来就要付很多海外服务的人。麻烦在开卡：一般要实名认证、交开卡费、通过另一个渠道往卡里充钱，每次扣款还有汇率损耗。有的卡段直接被 OpenAI 拒；开卡平台关门或者冻卡，下个月续费就断了。只为 ChatGPT 开一张卡，算下来常常比代充还贵。

### 合租 / 共享账号

几个人分摊一个订阅，人均最便宜，也是最不靠谱的一种。号不是你的，聊天记录别人能看，用量大家一起抢；多地频繁登录、反复改密码，正好是最容易触发风控的行为。OpenAI 的条款本来就不允许共享账号，号一旦被封，所有人的使用权和历史记录一起没了，找谁都没用。

### 代充服务

你用手上已有的方式付钱（支付宝、国内卡、USDT），服务方把订阅开到**你自己的** ChatGPT 账号上。比官方价贵一点，换来的是不用卡、不用外区 Apple ID、不用求人，聊天记录和设置都还在原来的号上。

风险在服务方，不在方法本身。超低价代充很多是用盗刷的卡付的，持卡人一申诉，订阅被撤销，相关账号可能被一起处理。挑的时候看四点：

- 从不要你的密码和验证码；
- 开在你自己的账号上，不给你一个新号；
- 退款规则写在明面上；
- 订单能自己查进度。

价格低得离谱的，基本就是答案。

## Pay2GPT 是怎么做的

Pay2GPT 是独立的第三方服务，和 OpenAI 没有关联。我们只做一件事：把 Go、Plus、Pro 开到你自己的 ChatGPT 账号上。

1. **选方案、付款**。不用注册，留个邮箱就行。支持银行卡（Visa、Mastercard、银联等）、支付宝、加密货币（USDT、USDC 等）。暂时不支持微信支付。订单按美元计价。
2. **连接你的账号**。付完款进入订单页（购买邮件里也有回到订单页的链接），先用邮箱验证码确认一下，然后在浏览器里登录 ChatGPT，打开 `chatgpt.com/api/auth/session`，全选复制这段 Session 文本，粘回订单页。手机上请用浏览器，别用 ChatGPT App。付款后 7 天内连接账号就行。
3. **开通**。提交后过 1–3 分钟刷新 ChatGPT，看到方案标识就好了。

几个你可能关心的点：

- **不要密码，也不要 ChatGPT 验证码**。谁以 Pay2GPT 的名义找你要，都是假的。
- **Session 只用来开通这一单**，加密存储，72 小时内删除。开通后你可以在 ChatGPT 的安全设置里「退出所有设备」，这段 Session 就失效了。
- **开不上，全额退回原付款方式。**
- **30 天质保**：开通后 30 天内，因为不是你这边的原因掉了，免费补开；补不了就退剩余天数。因为你自己的账号问题（比如共享、转卖、违反 OpenAI 使用政策）导致的封号不在售后范围内，具体看[服务条款](https://pay2gpt.com/zh-CN/terms?utm_source=github&utm_medium=readme&utm_campaign=guide)。
- **退款时效**：资料齐全后一般 3 个工作日内审核完，通过后一般 7 个工作日内到账，具体看付款渠道。USDT 退款会扣掉链上手续费。

用支付宝付：[支付宝开通 ChatGPT Plus](https://pay2gpt.com/zh-CN/guide/alipay?utm_source=github&utm_medium=readme&utm_campaign=guide)。用 USDT 付：支持 TRC20、ERC20、Base、BSC，TRC20 手续费最低，汇率锁定 15 分钟，1 个区块确认后自动跳到订单页，详见 [USDT 付款](https://pay2gpt.com/zh-CN/guide/usdt?utm_source=github&utm_medium=readme&utm_campaign=guide)。

## 价格

全部以美元计价，按月。

| 方案 | 价格 | 适合谁 |
| --- | --- | --- |
| Go | $6.90 | 日常聊天、查资料，比免费版额度多 |
| Plus | $21.90 | 写作、研究、写代码，大多数人选这个 |
| Plus 半价 | $13.90 | 账号拿到了 OpenAI 半价优惠的，就是一个月正常的 Plus，不自动续费 |
| Pro 100 | $119 | 每天重度使用，要用 Pro 模型 |
| Pro 200 | $185 | 比 Pro 100 用量更多，适合大量开发和研究 |
| Pro 500 | $499 | 最高档，唯一带 Ultrafast 模式 |

Plus 半价先[免费查一下账号有没有资格](https://pay2gpt.com/zh-CN/plus-half-price/check?utm_source=github&utm_medium=readme&utm_campaign=guide)，不用下单。拿不准选 Plus 还是 Pro，看[这篇](https://pay2gpt.com/zh-CN/guide/choose?utm_source=github&utm_medium=readme&utm_campaign=guide)。

[开通 Plus →](https://pay2gpt.com/zh-CN/checkout?plan=plus&utm_source=github&utm_medium=readme&utm_campaign=guide)

## 常见问题

**现在的订阅还没到期，能先充吗？**
能先买，但别急着开。订阅不叠加，等当前的快到期再开通。付款后 7 天内连接账号就行，订单不会作废；超过 7 天联系客服，按订单处理。

**会不会被封号？**
没人能保证一个号永远不被封。大多数封号和三件事有关：盗刷的卡付款、多人共享一个号、把密码交给别人。这三件我们都不做。详见[代充会不会封号](https://pay2gpt.com/zh-CN/guide/safe?utm_source=github&utm_medium=readme&utm_campaign=guide)。

**Session 是什么？为什么不是密码？**
它就是让你的浏览器保持登录状态的那个凭证。有了它，开通可以直接在你的账号上完成，不需要密码和验证码。正因为它有效期内等同于一个已登录的浏览器，只在你自己的订单页里粘贴，别发给任何人。

**开通后还是没有 Plus？**
退出 ChatGPT 再重新登录。10 分钟后还没生效，带上订单号发邮件给客服。

**提示 Session 不完整或已过期？**
刷新 chatgpt.com，重新打开登录信息页，用 Ctrl/⌘ + A 全选复制。手机上请用浏览器。

**能开 API 额度、Business 或 Enterprise 吗？**
不能。我们不卖 OpenAI API 额度或 API Key，也不开团队席位，这些直接找 OpenAI。

**我所在的地方能用 ChatGPT 吗？**
ChatGPT 只在 OpenAI 支持的国家和地区提供服务，在列表以外的地方访问，账号可能被限制。用之前对照一下官方列表：[ChatGPT Supported Countries](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)。

**付了 USDT 一直没到账？**
正常 1–3 分钟就有 1 个确认。超过 15 分钟，带上交易哈希发邮件给客服。转错网络的，提交哈希后客服 24 小时内核实。

**怎么联系你们？**
邮件 support@pay2gpt.com，带上订单号会快很多。订单进度随时在[我的订单](https://pay2gpt.com/zh-CN/orders?utm_source=github&utm_medium=readme&utm_campaign=guide)里用邮箱查，当前接单和开通情况看[服务状态](https://pay2gpt.com/zh-CN/status?utm_source=github&utm_medium=readme&utm_campaign=guide)。

## 相关链接

- [Pay2GPT 首页](https://pay2gpt.com/zh-CN?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [没有海外卡怎么开 Plus，5 种方法对比](https://pay2gpt.com/zh-CN/guide/compare?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [怎么开通 ChatGPT](https://pay2gpt.com/zh-CN/guide/activate?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [帮助中心](https://pay2gpt.com/zh-CN/help?utm_source=github&utm_medium=readme&utm_campaign=guide)

---

Pay2GPT 是独立的第三方服务，与 OpenAI 无关联。ChatGPT 是 OpenAI 的商标。本指南中 OpenAI 相关的说明以 OpenAI 官方帮助中心为准。
