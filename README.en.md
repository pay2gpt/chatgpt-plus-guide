# How to get ChatGPT Plus, Go or Pro when OpenAI declines your card

[简体中文](README.md) · **English** · [Русский](README.ru.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

> Last verified: 2026-10-25. Prices, payment methods and refund rules are checked against the live site every month, and this date moves when they are.

You picked a plan, typed in your card, and got "Your card was declined." Or you only have a local debit card, a mobile wallet or crypto. This guide covers why the payment fails, the options you actually have when you can't pay OpenAI directly (with the downside of each), and how Pay2GPT does it. Pick whatever fits you.

## Contents

- [First, check what your account has now](#first-check-what-your-account-has-now)
- [Why your card gets declined](#why-your-card-gets-declined)
- [Your options without a card OpenAI accepts](#your-options-without-a-card-openai-accepts)
- [How Pay2GPT works](#how-pay2gpt-works)
- [Prices](#prices)
- [FAQ](#faq)

## First, check what your account has now

Do this before you pay anyone. Subscriptions don't stack, so paying while one is still running either fails or wastes the money.

- **On the web**: sign in at chatgpt.com, click your profile picture → Settings → Account. You'll see your current plan and when it renews.
- **If you subscribed on an iPhone**: Apple bills it. Look in iPhone Settings → your name → Subscriptions, and cancel there if you need to.
- **If you subscribed on Android**: check Payments & subscriptions in Google Play.

If it says Free, or the paid plan has ended, you're ready. To cancel a plan yourself, OpenAI explains it here: [Canceling your ChatGPT subscription](https://help.openai.com/en/articles/7232927-how-do-i-cancel-my-chatgpt-plus-subscription).

## Why your card gets declined

OpenAI's web checkout only takes cards it accepts. Most declines come down to one of these:

1. **Your bank blocks it.** Plenty of banks block international or online charges in foreign currency by default, even on Visa and Mastercard debit cards. A 3D Secure prompt that never shows up, or one you didn't finish, also fails the payment.
2. **The card's country isn't supported.** If the bank that issued the card is in a country or region OpenAI doesn't support, the charge is refused.
3. **The billing address doesn't match.** An address or postcode that differs from what your bank has on file trips the fraud check.
4. **Your location and your card don't line up.** Payment risk checks look at the card's country, the billing address and where you're connecting from together. When they're far apart, the payment is more likely to be flagged.

OpenAI says it usually doesn't get the exact decline reason from the bank, so calling your bank is often the quickest fix. Their article: [Why was my credit card declined?](https://help.openai.com/en/articles/7232916-why-was-my-credit-card-declined)

## Your options without a card OpenAI accepts

| Option | What you pay | Effort | Your own account | Main risk |
| --- | --- | --- | --- | --- |
| Your own card from abroad, or someone abroad pays | Official price | Low | Yes | Depends on that card or person every month |
| App Store gift card on a foreign Apple ID | App Store price plus the gift card markup | Medium | Yes | A gift card that gets recalled can lock your Apple ID balance |
| Virtual card | Official price plus card, top-up and conversion fees | High | Yes | The card range gets declined, or the issuer freezes the card or shuts down |
| Shared account | Cheapest | Low | No | Getting logged out, others reading your chats, the account vanishing |
| Top-up service such as Pay2GPT | Official price plus a service fee | Low, a few minutes | Yes | Picking a service you can't trust |

### Your own card from abroad, or someone abroad pays

If you have a card OpenAI accepts, pay OpenAI directly. Nothing is cheaper. A friend or relative abroad paying on your account also gets you the official price with nobody in between. The catch is that their card stays on your account, every renewal depends on them, and a failed renewal or a forgotten cancellation is something the two of you have to sort out.

### App Store gift card on a foreign Apple ID

On an iPhone you can subscribe inside the ChatGPT app and pay from your Apple ID balance. You need an Apple ID set to a region where the subscription is sold, plus gift cards for that region. Apple bills it, so renewals and cancellations go through Apple, and the in-app price can differ from the web price. The real danger is the gift card itself: one bought second-hand that turns out to be fraudulent can be recalled later, and the Apple ID balance gets locked. Buy from sources you trust and keep the receipts.

### Virtual card

A virtual card issued in another country lets you pay OpenAI at the official price, and it makes sense if you pay for lots of foreign services anyway. Setting it up is the hard part: usually an ID check, an opening fee, topping the card up through some other channel, and a conversion fee on every charge. Some card ranges are declined by OpenAI outright, and if the issuer freezes your card or closes, next month's renewal fails. For ChatGPT alone, it often ends up costing more than a top-up service.

### Shared account

Several people split one subscription, so it's the cheapest per head. It's also the weakest option. The account isn't yours, other people can read your chats, usage limits are shared, and constant sign-ins from different places and password changes are exactly what trips OpenAI's risk checks. OpenAI's terms don't allow sharing an account, and when it gets closed, everyone loses access and their history at once with nobody to complain to.

### Top-up service

You pay with something you already have, such as a local card, Alipay or USDT, and the service activates the plan on **your own** ChatGPT account. It costs a bit more than OpenAI's price. In return you don't need a foreign card, a foreign Apple ID or a favour from anyone, and your chats and settings stay where they are.

The risk is the service, not the method. Very cheap top-ups are often paid for with stolen cards; when the real cardholder disputes the charge, the subscription is reversed and the accounts involved may be closed together. Before you pay anyone, check that the service:

- never asks for your password or a verification code;
- activates your existing account instead of handing you a new one;
- publishes its refund rules;
- lets you track your order yourself.

A price far below everyone else's is the clearest warning sign.

## How Pay2GPT works

Pay2GPT is an independent service and isn't affiliated with OpenAI. It does one thing: puts Go, Plus or Pro on the ChatGPT account you already have.

1. **Pick a plan and pay.** No sign-up, just an email address. You can pay by card (Visa, Mastercard, UnionPay and others), Alipay or crypto (USDT, USDC and others). WeChat Pay isn't available yet. Orders are charged in US dollars.
2. **Connect your account.** After paying you land on your order page (the purchase email links back to it). Confirm your email with a one-time code. Then, in a browser where you're signed in to ChatGPT, open `chatgpt.com/api/auth/session`, select everything, copy it and paste this Session text into the order page. On a phone, use the browser, not the ChatGPT app. You have 7 days after paying to do this.
3. **Done.** Refresh ChatGPT after 1–3 minutes. When your plan's badge shows up, it worked.

What you'll probably want to know:

- **No password, and no ChatGPT verification code.** Anyone asking for those in Pay2GPT's name is a fake.
- **The Session is used only to activate your order.** It's stored encrypted and deleted within 72 hours. Once your plan shows up, you can sign out of all devices in ChatGPT's security settings and that session stops working.
- **If the plan can't be activated, you get the full amount back** to the way you paid.
- **30-day warranty.** If the plan stops working within 30 days of activation for a reason that isn't on your side, it's restored free or the remaining days are refunded. Bans caused by how the account itself is used (sharing it, reselling it, breaking OpenAI's usage policies) aren't covered. The [Terms of Service](https://pay2gpt.com/terms?utm_source=github&utm_medium=readme&utm_campaign=guide) list the exclusions.
- **Refund timing.** Once support has your order details, review usually takes up to 3 business days. After approval the money usually arrives within 7 business days, depending on the payment channel. USDT refunds are sent less the network fee.

Paying with USDT: TRC20, ERC20, Base and BSC are supported, TRC20 has the lowest fee, and the rate is locked for 15 minutes. After 1 on-chain confirmation you're taken to your order. See [Pay with USDT](https://pay2gpt.com/guide/usdt?utm_source=github&utm_medium=readme&utm_campaign=guide).

In Pakistan with only JazzCash or Easypaisa? There's a [guide for that](https://pay2gpt.com/guide/pakistan?utm_source=github&utm_medium=readme&utm_campaign=guide).

## Prices

All in US dollars, per month.

| Plan | Price | Good for |
| --- | --- | --- |
| Go | $6.90 | Everyday chat and lookups, with more room than the free plan |
| Plus | $21.90 | Writing, research and coding. Most people pick this one |
| Plus Half Price | $13.90 | Accounts that got OpenAI's half-price offer. It's regular Plus for one month, no auto-renewal |
| Pro 100 | $119 | Heavy daily use, with Pro models |
| Pro 200 | $185 | More usage than Pro 100, for heavy development and research |
| Pro 500 | $499 | The top tier, and the only one with Ultrafast mode |

For Plus Half Price, [check your eligibility for free](https://pay2gpt.com/plus-half-price/check?utm_source=github&utm_medium=readme&utm_campaign=guide) first. No order needed. Not sure between Plus and Pro? [This helps](https://pay2gpt.com/guide/choose?utm_source=github&utm_medium=readme&utm_campaign=guide).

[Get Plus →](https://pay2gpt.com/checkout?plan=plus&utm_source=github&utm_medium=readme&utm_campaign=guide)

## FAQ

**My current plan hasn't ended. Can I buy now?**
You can buy, just don't activate yet. Subscriptions don't stack, so activate when the current one ends. You have 7 days after paying to connect your account, and the order isn't used up in the meantime. Past 7 days, contact support and they'll handle it by order.

**Can this get my account banned?**
Nobody can promise an account will never be banned. Most bans come from three things: payments with stolen cards, many people sharing one account, and handing over the password. Pay2GPT does none of them. More in [Will a top-up get my account banned?](https://pay2gpt.com/guide/safe?utm_source=github&utm_medium=readme&utm_campaign=guide)

**What is the Session text, and why isn't it a password?**
It's the credential that keeps your browser signed in. It lets the activation happen on your account without your password or a code. Because it works like a signed-in browser while it's valid, paste it only on your own order page and never send it to anyone.

**I activated but still don't see Plus.**
Sign out of ChatGPT and sign back in. If it's still not there after 10 minutes, email support with your order number.

**It says my login details are incomplete or expired.**
Refresh chatgpt.com, open the login details page again and copy everything with Ctrl/⌘ + A. On a phone, use the browser.

**Can I buy API credits, or Business or Enterprise seats?**
No. Pay2GPT doesn't sell OpenAI API credits or API keys, and doesn't do team seats. Go to OpenAI for those.

**Is ChatGPT available where I live?**
ChatGPT is offered only in the countries and territories OpenAI supports, and using it from elsewhere can get the account restricted. Check OpenAI's list first: [ChatGPT Supported Countries](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries).

**I sent USDT and nothing happened.**
One confirmation usually takes 1–3 minutes. After 15 minutes, email support with the transaction hash. Sent it on the wrong network? Submit the hash and support checks it within 24 hours.

**How do I reach you?**
Email support@pay2gpt.com. It's faster with your order number. You can look up an order anytime under [Orders](https://pay2gpt.com/orders?utm_source=github&utm_medium=readme&utm_campaign=guide) with your email, and [Service status](https://pay2gpt.com/status?utm_source=github&utm_medium=readme&utm_campaign=guide) shows whether orders are open and how long activations are taking.

## More

- [Pay2GPT home](https://pay2gpt.com/?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [5 ways to pay for ChatGPT Plus without an overseas card, compared](https://pay2gpt.com/guide/compare?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [How to activate ChatGPT](https://pay2gpt.com/guide/activate?utm_source=github&utm_medium=readme&utm_campaign=guide)
- [Help center](https://pay2gpt.com/help?utm_source=github&utm_medium=readme&utm_campaign=guide)

---

Pay2GPT is an independent service and is not affiliated with OpenAI. ChatGPT is a trademark of OpenAI. For anything about OpenAI's own rules, OpenAI's help center is the authority.
