# Changelog

## v0.1.1 — Telethon-Correct Mention Resolution

### ⚠️ Breaking Change
Mentions are no longer resolved during parsing.

Starting from **v0.1.1**, `parse()` produces **pure, offline-safe entities**.
Mention resolution is now an explicit, async step — matching Telethon’s
internal architecture.

---

### ✨ Added
- `resolve_mentions(client, entities)`
  - Resolves `tg://user?id=...` into `InputMessageEntityMentionName`
  - Async and network-aware
  - Required before sending messages with mentions

---

### 🔄 Changed
- `parse()` no longer performs async operations
- Mention entities are initially emitted as:

- `MessageEntityTextUrl("tg://user?id=...")`

- Mention resolution happens only when explicitly requested

---

### 🛡️ Benefits
- No event loop conflicts
- Offline-safe parsing and round-trips
- HTML ↔ Markdown ↔ Entities pipelines preserved
- Exact behavioral match with Telethon

---

### 🧠 Notes
This change aligns `delimiters` with Telethon’s two-phase message pipeline:
parse first, resolve mentions just before sending.


---

## Migrating from v0.1.0 to v0.1.1

### ❌ Old (v0.1.0)

Mentions were resolved automatically during parsing:

```python
text, entities = parse(md_text)
await client.send_message(chat_id, text, formatting_entities=entities)
```


---

### ✅ New (v0.1.1+)

Mentions must be resolved explicitly:

```python
text, entities = parse(md_text)
entities = await resolve_mentions(client, entities)

await client.send_message(
    chat_id,
    text,
    formatting_entities=entities
)

```

---

### ⚠️ Important

If you do not call `resolve_mentions()`:

- Mentions will be treated as normal text URLs
- Users will **NOT** be notified
- Telegram will **NOT** render a clickable mention

This change is intentional and matches Telethon’s internal behavior.
