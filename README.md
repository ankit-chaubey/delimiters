# 🧩 Delimiters

Advanced • Lossless Markdown & HTML ↔ Telegram Entities for Telethon  
Production-ready, round‑trip safe, two‑phase mention model — built for editors, userbots, mirrors and exporters.

[![PyPI](https://img.shields.io/pypi/v/delimiters.svg)](https://pypi.org/project/delimiters/)
[![Downloads](https://img.shields.io/pypi/dm/delimiters.svg)](https://pypi.org/project/delimiters/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/ankit-chaubey/delimiters/blob/6e99ff8632e060158982d812ff5549a731f60547/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-ankit--chaubey%2Fdelimiters-black.svg)](https://github.com/ankit-chaubey/delimiters)
[![Chat on Telegram](https://img.shields.io/badge/Telegram-@ankify-2CA5E0.svg)](https://t.me/ankify)

---

✨ Table of contents
- [What is delimiters?](#what-is-delimiters)
- [Why it matters](#why-it-matters)
- [Highlights & Features](#highlights--features)
- [Badges & Compatibility](#badges--compatibility)
- [Install](#install)
- [Quickstart (three lines)](#quickstart-three-lines)
- [Two‑phase mention model (v0.1.1+)](#two-phase-mention-model-v011)
- [Premium API Reference (clear & linkable)](#premium-api-reference-clear--linkable)
- [Recipes & Examples](#recipes--examples)
- [Best practices & troubleshooting](#best-practices--troubleshooting)
- [Project layout](#project-layout)
- [Contributing & release checklist](#contributing--release-checklist)
- [Author & Maintainers](#author--maintainers)
- [License & Links](#license--links)

---

## What is delimiters? 🚀

delimiters is a focused formatting engine that converts between human‑friendly Markdown/HTML and Telegram's native MessageEntity model — reliably and without losing data. Use it whenever you need exact fidelity when sending, editing, archiving, or exporting Telegram content.

Think: "Markdown/HTML as serialization; Telegram entities as the source of truth."

---

## Why it matters ❗

Telegram stores formatting as MessageEntity objects (e.g. `MessageEntityBold`, `MessageEntitySpoiler`) — not as Markdown or HTML text. Many tools:

- Break nested entities when editing
- Lose formatting on edits or round-trips
- Mistreat custom emojis and Unicode surrogate pairs
- Perform hidden network calls during parsing

delimiters solves these problems by:
- making parse() pure & offline,
- making mention resolution explicit (network/async),
- preserving nested entities, custom emojis, and collapsed/expanded blockquote state.

---

## Highlights & Features ✨

- Small, focused API: parse / unparse / resolve_mentions
- Full Telegram entity coverage used in chats:
  - Bold, Italic, Underline, Strike
  - Inline & block code
  - Inline spoilers and `<tg-spoiler>`
  - Collapsed & expanded blockquotes (state preserved)
  - Mentions (tg://user?id=...), text URLs, custom emojis (`<tg-emoji>`)
- Lossless round-trip: Markdown/HTML ↔ (text + entities) ↔ Markdown/HTML
- Deterministic parsing — no network I/O during parse()
- Explicit async mention resolution matching Telethon semantics (v0.1.1+)
- Unicode- and surrogate-pair-safe
- Telethon-friendly (compatible with Telethon ≥ 1.34)

---

## Badges & Compatibility 🧾

- PyPI: https://pypi.org/project/delimiters/
- GitHub repo: https://github.com/ankit-chaubey/delimiters
- Python 3.8+
- Telethon >= 1.34 recommended

---

## Install 📦

From PyPI (recommended):

```bash
pip install delimiters
```

Or install from source:

```bash
git clone https://github.com/ankit-chaubey/delimiters.git
cd delimiters
pip install .
```

---

## Quickstart — three lines ✨

```py
from delimiters import parse, resolve_mentions
text, entities = parse("**Hi** [User](tg://user?id=93602376)")
entities = await resolve_mentions(client, entities)
await client.send_message(chat_id, text, formatting_entities=entities)
```

---

## Two‑phase mention model (v0.1.1+) 🔁

delimiters intentionally mirrors Telethon: parsing and mention resolution are separate.

Phase 1 — Parsing (offline, pure)

```py
text, entities = parse(input_text, mode="md")  # or mode="html"
```

- Deterministic
- No network calls
- Mentions become: `MessageEntityTextUrl("tg://user?id=...")`

Phase 2 — Mention resolution (async, network)

```py
entities = await resolve_mentions(client, entities)
```

- Converts `MessageEntityTextUrl("tg://user?id=...")` → `InputMessageEntityMentionName` (resolved form)
- Required before sending or editing messages that should notify users or render clickable mentions
- Matches Telethon's pipeline; intentional design

Important: skip resolve_mentions and the mention stays a text URL — no notifications, no clickable @. This prevents hidden network calls during parse-time.

---

## Premium API Reference (clear, linkable, examples) 🔎

All functions are exported from the top-level package: `from delimiters import parse, unparse, resolve_mentions`.

1) parse(text: str, mode: Literal["md","html"]="md") -> Tuple[str, List[MessageEntity]]
- Purpose: Convert Markdown/HTML → (text, entities).
- Key behavior:
  - Pure function; no network I/O.
  - Mentions are left unresolved as text-URL entities (`tg://user?id=...`).
  - Supports extended markdown tokens: `!!underline!!`, `||spoiler||`, `%%collapsed%%`, `^^expanded^^`.
- Example:

```py
text, entities = parse("**Hello** ||secret|| [AnKiT](tg://user?id=93602376)")
```

2) unparse(text: str, entities: List[MessageEntity], mode: Literal["md","html"]="md") -> str
- Purpose: Convert (text + Telegram entities) → Markdown or HTML.
- Key behavior:
  - Preserves nesting and entity boundaries where possible.
  - Useful for round-trip editing workflows.
- Example:

```py
md = unparse(message.text, message.entities, mode="md")
```

3) resolve_mentions(client: TelegramClient, entities: List[MessageEntity]) -> List[Union[MessageEntity, InputMessageEntity]]
- Purpose: Convert text-URL mention entities into resolved mention entities accepted by the Telegram API.
- Key behavior:
  - Async; requires an active `client` (Telethon).
  - Uses the client to map `tg://user?id=...` into `InputMessageEntityMentionName` or equivalent.
  - Returns entities ready to pass to Telethon `send_message` or `message.edit` `formatting_entities` parameter.
- Example:

```py
entities = await resolve_mentions(client, entities)
await client.send_message(chat_id, text, formatting_entities=entities)
```

Notes:
- The returned entity objects are compatible with Telethon’s API.
- If your environment does not require notify/clickable mentions (e.g., drafts or previews), you can skip the resolve step.

---

## Recipes & Examples 🧩

Full send flow (Markdown):

```py
from delimiters import parse, resolve_mentions

md = "**Welcome** ||this is private|| [Bob](tg://user?id=93602376)"
text, entities = parse(md)
entities = await resolve_mentions(client, entities)
await client.send_message(chat_id, text, formatting_entities=entities)
```

Editing with round-trip safety:

```py
from delimiters import unparse, parse, resolve_mentions

# Get stable markdown representation of existing message
md = unparse(message.text, message.entities, mode="md")
# Make textual edits on md
md = md.replace("old", "new")
# Re-parse and resolve
text, entities = parse(md)
entities = await resolve_mentions(client, entities)
await message.edit(text, formatting_entities=entities)
```

HTML mode:

```py
html = '<b>Heads up</b> <tg-spoiler>secret</tg-spoiler> <a href="tg://user?id=93602376">Eve</a>'
text, entities = parse(html, mode="html")
entities = await resolve_mentions(client, entities)
await client.send_message(chat_id, text, formatting_entities=entities)
```

Helper utility (combine parse+resolve):

```py
async def parse_and_resolve(client, raw: str, mode: str = "md"):
    text, entities = parse(raw, mode=mode)
    return text, await resolve_mentions(client, entities)
```

Round-trip test (use in CI):

```py
md = unparse(orig_text, orig_entities, mode="md")
text2, entities2 = parse(md)
# After resolve_mentions(client, entities2), compare semantics with original entities
```

---

## Best practices & troubleshooting 🛠️

- Always call parse() as a pure function (no network).
- Always call resolve_mentions(...) immediately before sending/editing to ensure mentions are clickable and notify.
- Use unparse() → edit → parse() to preserve nested entities and collapsed/expanded blockquote state.
- If mentions are not notifying: make sure you resolved mentions and the client has necessary access.
- If formatting breaks on edit: ensure you pass `formatting_entities=entities` when editing and that entities were resolved appropriately.
- Test with surrogate pairs + custom emojis during CI to avoid rendering surprises.

---

## Project layout 🗂️

```
delimiters/
├── __init__.py          # Public API
├── api.py               # High-level parse/unparse/resolve_mentions
├── custom_markdown.py   # Markdown ↔ entities rules
├── markdown_ext.py      # Extra delimiters (underline, spoilers, blockquotes)
├── html_ext.py          # HTML ↔ entities rules
├── tests/               # Unit tests (recommended)
├── setup.py
├── LICENSE
└── README.md
```

---

## Contributing & release checklist 🤝

Contributions welcome — please open an issue first to discuss bigger changes.

PR checklist:
- Add/extend tests for Unicode, nested entities, custom emoji, collapsed quotes.
- Keep parse() offline and deterministic.
- Keep resolve_mentions() explicitly network-bound.
- Update CHANGELOG.md and bump version (semver).
- Run packaging checks:
  - python -m build
  - python -m pip install dist/delimiters-<version>-py3-none-any.whl
- Publish:
  - twine upload dist/*

---

## Changelog (summary) 📝

- v0.1.1 — Introduced explicit two‑phase mention resolution:
  - parse() is offline-only and no longer resolves mentions.
  - resolve_mentions(client, entities) added to explicitly resolve tg://user?id references to proper mention entities.

(Check CHANGELOG.md in the repo for detailed history.)

---

## Author / Creator / Maintainer 👨‍💻

✨ Creator & Maintainer  
[Ankit Chaubey](https://github.com/ankit-chaubey)

Profile
- Email: m.ankitchaubey@gmail.com
- Telegram: [@ankify](https://t.me/ankify)
- Personal: [GitHub Page](https://chaubey.is-a.dev/)

---

## License & Links 📜

- License: [MIT License](https://github.com/ankit-chaubey/delimiters/blob/6e99ff8632e060158982d812ff5549a731f60547/LICENSE) © 2026 Ankit Chaubey
- PyPI: https://pypi.org/project/delimiters/
- Repository: https://github.com/ankit-chaubey/delimiters
- Issues: https://github.com/ankit-chaubey/delimiters/issues

---

Thank you for using delimiters! built for clarity, correctness, and production workflows ❤️
