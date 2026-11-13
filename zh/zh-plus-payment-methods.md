---
title: "ChatGPT Plus 支付方式对照表：你手上的卡和钱包分别能在哪付"
lang: zh-CN
---
# ChatGPT Plus 支付方式对照表：你手上的卡和钱包分别能在哪付

搜“ChatGPT Plus 支付方式”的人，手上一般已经有一两样东西：一张国内银行卡、一个支付宝，也许还有一点 USDT。订 Plus 有三个入口：chatgpt.com 网页结账、ChatGPT App 里的苹果或谷歌内购、第三方代充。同一张卡换个入口，结果可能完全不同。下面按支付工具逐个对照。

## 对照表

| 你手上的支付工具 | chatgpt.com 网页结账 | Pay2GPT 代充 |
|---|---|---|
| 中国大陆或香港银行发的 Visa、万事达、银联卡 | 付不了。OpenAI 要求发卡行在它支持的国家和地区，大陆和香港都不在名单上 | 能付，Plus $25.10；发卡行拦境外线上交易时，这里也可能被拒 |
| 支持地区银行发的信用卡、借记卡 | 能付，要完成银行的 3D Secure 验证 | 能付 |
| 预付卡、虚拟卡 | OpenAI 只写明预付卡不能买 API 额度；订阅能否通过，要看卡有没有开境外、定期扣款和 3D Secure | 按银行卡结算，同样看发卡方设置 |
| 支付宝 | 付不了，官网付款方式里没有 | 能付，Plus $25.10，按付款当时汇率换成人民币 |
| 微信支付 | 付不了 | 暂不支持 |
| USDT、USDC 等加密货币 | 付不了 | 能付，Plus $23.90 |

## 网页结账基本只认银行卡

OpenAI 帮助中心的多币种结算页把付款方式分了地区：所有国家都能用信用卡和借记卡，另外只有少数地区有本地方式，比如英国和欧洲经济区的 Link 银行扣款、印度的 UPI、巴西的 Pix、印尼的 GoPay。中国大陆和香港不在这份名单上，也不在 ChatGPT 支持的国家和地区列表里。

卡被拒时，OpenAI 列的第一类原因是银行拦截，第三类是地区：你本人和发卡行都要在支持地区。后一条决定了很多人的结果。大陆发的卡，开境外支付、换账单地址、挂 VPN 都改变不了发卡地，OpenAI 反而建议验证时把 VPN 关掉。

## App 内购是另一本账

在 iPhone 或安卓的 ChatGPT App 里升级，扣费的是苹果或谷歌，用的是 Apple ID 或 Google 账号上的付款方式和余额，续订、取消也都在那边操作。按 OpenAI 的说明，iOS App 只在它列出的国家和地区提供；App 内订阅按当地货币扣费，价格可能和网页不一样。

同一个账号在网页和 App 各订一次，会同时扣两份钱。想从 App 换到网页付，先在原平台取消，等当期结束再订。

## 用支付宝或 USDT 走代充

[Pay2GPT](https://pay2gpt.com/guide/compare?utm_source=github_pages&utm_campaign=offsite) 是独立的代充服务，和 OpenAI 没有隶属关系。付款后在自己的订单页连接 ChatGPT 账号，Plus 开到你原来的号上，聊天记录和设置都在，大多几分钟开好。全程不要密码和验证码；开不了全额原路退，开通后 30 天内不是你这边的原因掉了会员，免费补开。

价格分两档：银行卡和支付宝都是 $25.10，加密货币是 $23.90。

## 常见问题

### 国内的卡在官网被拒，打电话让银行放行有用吗？

银行能解决的是它自己的风控拦截。卡如果是大陆或香港的银行发的，卡在发卡地区这一关，银行开了境外支付也过不去。

### 支付宝付款时人民币金额为什么每天不一样？

套餐按美元定价，支付宝按付款当时的汇率换算，确认页上显示的金额为准。

### 能用微信付吗？

官网不行，Pay2GPT 暂时也不支持。可以用支付宝、银行卡或 USDT。

### 已经在 iPhone 上订了 Plus，想改成别的方式付？

先在 iPhone 的“设置”里取消苹果那边的订阅，等这一期结束，再用新方式订，不然两边都会扣。

### 代充开出来的 Plus 和官网订的有区别吗？

套餐开在你自己的 ChatGPT 账号上，用法一样。区别在付款和售后：钱付给代充平台，问题找平台处理。

## 参考

以下 OpenAI 帮助中心页面于 2026 年 11 月 13 日核对，规则以官方最新说明为准：

- [Why was my credit card declined?](https://help.openai.com/en/articles/7232916-why-was-my-credit-card-declined)
- [ChatGPT Supported Countries](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)
- [Multi-currency billing](https://help.openai.com/en/articles/10421635)
- [ChatGPT iOS app: Upgrading to a paid subscription](https://help.openai.com/en/articles/7905739-chatgpt-ios-app-upgrading-to-a-paid-subscription)
- [How do I avoid being charged twice if I subscribe to ChatGPT on iOS, Android, and the web?](https://help.openai.com/en/articles/20001043)
