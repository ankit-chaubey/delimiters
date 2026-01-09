# 🧩 Delimiters

## Advanced Markdown & HTML Formatting for Telethon

**delimiters** is a production-grade formatting engine for **Telethon** that provides **lossless, round-trip safe** conversion between:

- Markdown  
- HTML  
- Telegram message entities  

It is designed for **userbots, bots, editors, exporters, mirrors, and archives** that need **full control** over Telegram formatting — including **custom emojis**, **spoilers**, **blockquotes**, and **mentions**.

---

## ✨ Why Delimiters Exists

Telegram internally **does not use Markdown or HTML**.  
It stores formatting as **entities** (`MessageEntityBold`, `MessageEntitySpoiler`, etc.).

Most libraries:

- Lose formatting on edit  
- Break nested entities  
- Mishandle emojis & Unicode  
- Cannot round-trip safely  

**Delimiters solves this properly.**

> Markdown and HTML are treated as *serialization formats*.  
> Telegram entities are treated as the *source of truth*.

---

## 🔥 Key Features

### ✅ Unified API

One API for everything:

```python
parse(text, mode="md" | "html")
unparse(text, entities, mode="md" | "html")
```

---

✅ Full Telegram Entity Support

- Bold / Italic / Underline / Strike

- Spoilers

- Inline code & code blocks

- Collapsed & expanded blockquotes

- Mentions `(tg://user?id=...)`

- Text URLs

- Custom emojis

- Email & URL entities

- HTML `<tg-spoiler>` and `<tg-emoji>`



---

### ✅ Lossless Round-Trip

 - Markdown → Entities → Markdown
   HTML     → Entities → HTML

No formatting is lost.
No corruption.
No surprises.


---

### ✅ Advanced Markdown Extensions

`!!underline!!`

`||spoiler||`

`%%collapsed blockquote%%`

`^^expanded blockquote^^`


Activated automatically on import.


---

### ✅ Unicode & Emoji Safe

 - Fully surrogate-safe

 - Works with all Unicode text

 - Handles custom emojis correctly



---

## 📦 Installation

From project root:

```
pip install delimiters
```


---
```
📁 Project Structure

delimiters/
├── __init__.py          # Public API
├── api.py               # Unified parse / unparse
├── custom_markdown.py   # Markdown ↔ Telegram entities
├── markdown_ext.py      # Extra markdown delimiters
├── html_ext.py          # HTML ↔ Telegram entities
setup.py

```
---

## 📥 Importing

### ✅ Recommended (Unified API)

```
from delimiters import parse, unparse
```


---

### 🔧 Advanced Imports (Optional)

```
from delimiters import CustomMarkdown
from delimiters import CustomHtmlParser
from delimiters import markdown
```

Use these only if you need low-level control.


---

## 🧠 Core Concepts (Must Read)

Telegram messages consist of:

`text: str`
`entities: List[MessageEntity]`

❌ Telegram does NOT store Markdown or HTML.

delimiters converts between:

Markdown / HTML  ↔  (text + entities)


---

## 🚀 Basic Usage

Sending a Formatted Message

```
text, entities = parse("**Hello** ||secret||")
await client.send_message(chat_id, text, entities=entities)
```


---

Editing a Message Safely

```
text, entities = parse("!!Edited!!")
await message.edit(text, entities=entities)
```


---

Round-Trip Editing (Lossless)

```
md = unparse(message.text, message.entities)
text, entities = parse(md)
await message.edit(text, entities=entities)
```


---

## ✍️ Markdown Support

Inline Formatting

`**bold**
__italic__
!!underline!!
~~strike~~
||spoiler||
`inline code``


---

Blockquotes

`^^Expanded quote^^`

`%%Collapsed quote%%`

- Per-entity collapsed state preserved

- Nesting supported



---

Mentions (Safe Everywhere)

`[User](tg://user?id=93602376)`

 - ✔ Works in Saved Messages
 - ✔ Not stripped by Telegram


---

Custom Emojis

```
![🙂](emoji/5210952531676504517)
![🔥](emoji/5210952531676504518)
```

 - ✔ Converts to `MessageEntityCustomEmoji`
 - ✔ Fully round-trip safe


---

### 🌐 HTML Support

Supported Tags

```
<b>Bold</b>
<i>Italic</i>
<u>Underline</u>
<del>Strike</del>

<tg-spoiler>Spoiler</tg-spoiler>

<blockquote collapsed>Collapsed</blockquote>
<blockquote>Expanded</blockquote>

<tg-emoji emoji-id="5210952531676504517"></tg-emoji>

<a href="tg://user?id=93602376">Mention</a>
```


---

HTML → Telegram

```
text, entities = parse(html, mode="html")
```


---

Telegram → HTML

```
html = unparse(text, entities, mode="html")
```


---

## 🧩 Public API Reference

```
parse(text, mode="md")
```

Convert Markdown or HTML into Telegram-ready text & entities.

Parameters

`text: str`

`mode: "md" | "html"`


Returns

`Tuple[str, List[MessageEntity]]`


---

```
unparse(text, entities, mode="md")
```

Convert Telegram entities back to Markdown or HTML.

Parameters

`text: str`

`entities: Iterable[MessageEntity]`

`mode: "md" | "html"`


Returns

`str`


---

## 🧪 Advanced Usage

Accessing Low-Level Parsers

```
text, entities = CustomMarkdown.parse(md)
md = CustomMarkdown.unparse(text, entities)
```

```
text, entities = CustomHtmlParser.parse(html)
html = CustomHtmlParser.unparse(text, entities)
```


---

Using Extra Markdown Delimiters Directly

```
from delimiters import markdown
````

This activates:

`!! → underline`

`|| → spoiler`

`%% → collapsed quote`

`^^ → expanded quote`



---

### 🛡️ Safety Guarantees

 - No entity overlap corruption
 - Emoji & Unicode safe
 - Nested entities preserved
 - Telethon ≥ 1.34 compatible
 - No monkey-patching core logic


---

## 🧠 Design Philosophy

 - Telegram entities are the source of truth

 - Markdown & HTML are serialization layers

 - Explicit > magic

 - Predictable > clever


This library is built for developers who understand Telegram deeply.


---

### 📌 When You Should Use This

 - ✔ Advanced userbots
 - ✔ Message editors
 - ✔ Telegram → HTML exporters
 - ✔ Telegram mirrors
 - ✔ Archival tools
 - ✔ Emoji-heavy chats

---

### 🤍 Final Words

This project is intentionally:

- Minimal

- Explicit

- Lossless

- Production-ready


If you maintain a serious Telethon project,
this is the formatting layer you want.


---

## 📄 License

This project is licensed under the **MIT License**.  
See the full [license](LICENSE) or text here: https://opensource.org/licenses/MIT

© 2026 **Ankit Chaubey**. All rights reserved.  
This project was initially developed for personal use and is now released publicly.

---

## 📬 Contact

- **Email:** m.ankitchaubey@gmail.com  
- **Telegram:** @ankify
