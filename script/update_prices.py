#!/usr/bin/env python3
"""Rewrites the price block of every README from https://pay2gpt.com/prices.json.

Pay2GPT's prices live in its database; this repository keeps no price of its own. The block between the
"prices:begin" and "prices:end" comments in each README is generated here. Edit the wording in COPY below, never the
numbers in a README. Run it with no arguments; it exits non-zero, changing nothing, when the catalog cannot be read
or looks wrong, so a failed fetch never empties a table.

    python3 script/update_prices.py            # rewrite the READMEs
    python3 script/update_prices.py --check    # exit 1 if a README is out of date
    PRICES_JSON=path/to/prices.json python3 script/update_prices.py   # read a saved copy instead of the site
"""
import json
import os
import re
import sys
import urllib.request

SOURCE = "https://pay2gpt.com/prices.json"
BEGIN = "<!-- prices:begin · generated from pay2gpt.com/prices.json by script/update_prices.py, do not edit by hand -->"
END = "<!-- prices:end -->"
UTM = "utm_source=github&utm_medium=readme&utm_campaign=guide"

# Per README: the table's head, who each plan suits, and the Codex credits sentence. {first}, {more} and {url} are
# filled in; {more} lists the next tiers with `tier`, joined by `join`.
COPY = {
    "README.md": {
        "head": ("方案", "价格", "适合谁"),
        "plans": {
            "go": "日常聊天、查资料，比免费版额度多",
            "plus": "写作、研究、写代码，大多数人选这个",
            "pro-100": "每天重度使用，要用 Pro 模型",
            "pro-200": "比 Pro 100 用量更多，适合大量开发和研究",
            "pro-500": "最高档，唯一带 Ultrafast 模式",
        },
        "credits": "Codex 点数（一次购买，不是包月）：{first}起{more}，[全部档位看这里]({url})。仅适用于已有个人 Plus/Pro 的账号，不是 OpenAI API 余额。",
        "first": "{credits} 点 {price} ", "tier": "{credits} 点 {price}", "join": "，", "lead": "，",
        "credits_url": "https://pay2gpt.com/codex-credits", "currency": "$",
    },
    "README.en.md": {
        "head": ("Plan", "Price", "Good for"),
        "plans": {
            "go": "Everyday chat and lookups, with more room than the free plan",
            "plus": "Writing, research and coding. Most people pick this one",
            "pro-100": "Heavy daily use, with Pro models",
            "pro-200": "More usage than Pro 100, for heavy development and research",
            "pro-500": "The top tier, and the only one with Ultrafast mode",
        },
        "credits": "Codex credits (one-time purchase, not a monthly plan): {first}{more}. [All tiers]({url}). For existing personal Plus/Pro accounts only; these are not OpenAI API credits.",
        "first": "from {price} for {credits} credits", "tier": "{credits} credits {price}", "join": ", ", "lead": "; ",
        "credits_url": "https://pay2gpt.com/en/codex-credits", "currency": "$",
    },
    "README.ru.md": {
        "head": ("План", "Цена", "Кому подойдёт"),
        "plans": {
            "go": "Повседневные вопросы и поиск, лимиты больше, чем на бесплатном плане",
            "plus": "Тексты, исследования, код. Большинство выбирает его",
            "pro-100": "Активная ежедневная работа, Pro-модели",
            "pro-200": "Больше лимитов, чем у Pro 100, для серьёзной разработки и исследований",
            "pro-500": "Максимальный тариф, только в нём есть режим Ultrafast",
        },
        "credits": "Кредиты Codex (разовая покупка, не месячная подписка): {first}{more}. [Все пакеты]({url}). Только для действующих личных аккаунтов Plus/Pro; это не баланс OpenAI API.",
        "first": "от {price} за {credits} кредитов", "tier": "{credits} кредитов — {price}", "join": ", ", "lead": "; ",
        "credits_url": "https://ru.pay2gpt.com/codex-credits", "currency": "$",
    },
    "README.es.md": {
        "head": ("Plan", "Precio", "Para quién"),
        "plans": {
            "go": "Chat y consultas del día a día, con más margen que el plan gratis",
            "plus": "Escribir, investigar y programar. Es el que elige la mayoría",
            "pro-100": "Uso intenso todos los días, con modelos Pro",
            "pro-200": "Más uso que Pro 100, para desarrollo e investigación pesada",
            "pro-500": "El nivel más alto y el único con modo Ultrafast",
        },
        "credits": "Créditos Codex (compra única, no suscripción mensual): {first}{more}. [Todos los paquetes]({url}). Solo para cuentas personales con Plus/Pro activo; no son saldo de la API de OpenAI.",
        "first": "desde {price} por {credits} créditos", "tier": "{credits} créditos {price}", "join": ", ", "lead": "; ",
        "credits_url": "https://pay2gpt.com/es/codex-credits", "currency": "$",
    },
    "README.pt-BR.md": {
        "head": ("Plano", "Preço", "Para quem"),
        "plans": {
            "go": "Conversa e consultas do dia a dia, com mais espaço que o plano grátis",
            "plus": "Escrever, pesquisar e programar. É o que a maioria escolhe",
            "pro-100": "Uso pesado todo dia, com os modelos Pro",
            "pro-200": "Mais uso que o Pro 100, para desenvolvimento e pesquisa pesados",
            "pro-500": "O nível mais alto e o único com o modo Ultrafast",
        },
        "credits": "Créditos Codex (compra única, não assinatura mensal): {first}{more}. [Todos os pacotes]({url}). Apenas para contas pessoais com Plus/Pro ativo; não são saldo da API da OpenAI.",
        "first": "a partir de {price} por {credits} créditos", "tier": "{credits} créditos {price}", "join": ", ", "lead": "; ",
        "credits_url": "https://pay2gpt.com/pt-BR/codex-credits", "currency": "$", "credits_currency": "US$",
    },
}


def catalog():
    saved = os.environ.get("PRICES_JSON")
    if saved:
        with open(saved, encoding="utf-8") as file:
            data = json.load(file)
    else:
        request = urllib.request.Request(SOURCE, headers={"User-Agent": "chatgpt-plus-guide price sync", "Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
    products = [p for p in data["products"] if p["saleable"] and p["currency"] == "usd" and p["list_cents"] > 0]
    plans = [p for p in products if p["kind"] == "subscription"]
    credits = sorted((p for p in products if p["kind"] == "codex_credits"), key=lambda p: p["credits"])
    if not any(p["slug"] == "plus" for p in plans):
        sys.exit("prices.json has no Plus on sale; refusing to rewrite the price tables")
    return plans, credits


def money(cents, symbol):
    return f"{symbol}{cents // 100}" if cents % 100 == 0 else f"{symbol}{cents / 100:.2f}"


def block(copy, plans, credits):
    lines = [BEGIN, "| " + " | ".join(copy["head"]) + " |", "| --- | --- | --- |"]
    for plan in plans:
        lines.append(f"| {plan['name']} | {money(plan['list_cents'], copy['currency'])} | {copy['plans'].get(plan['slug'], '')} |")
    if credits:
        symbol = copy.get("credits_currency", copy["currency"])
        tier = lambda template, p: template.format(credits=p["credits"], price=money(p["list_cents"], symbol))
        more = copy["join"].join(tier(copy["tier"], p) for p in credits[1:3])
        sentence = copy["credits"].format(first=tier(copy["first"], credits[0]), more=(copy["lead"] + more) if more else "",
                                          url=f"{copy['credits_url']}?{UTM}")
        lines += ["", sentence]
    return "\n".join(lines + [END])


def main():
    check = "--check" in sys.argv[1:]
    plans, credits = catalog()
    stale = []
    for name, copy in COPY.items():
        with open(name, encoding="utf-8") as file:
            text = file.read()
        pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
        if not pattern.search(text):
            sys.exit(f"{name} has no prices:begin … prices:end block")
        updated = pattern.sub(lambda _: block(copy, plans, credits), text, count=1)
        if updated != text:
            stale.append(name)
            if not check:
                with open(name, "w", encoding="utf-8") as file:
                    file.write(updated)
    print(("out of date: " if check else "rewrote: ") + (", ".join(stale) or "nothing"))
    sys.exit(1 if check and stale else 0)


if __name__ == "__main__":
    main()
