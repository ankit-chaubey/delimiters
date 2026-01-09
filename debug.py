from delimiters import parse, unparse

md = """
||Spoiler||

%%COLLAPSED BLOCKQUOTE
Hidden line
Hidden line 2
Hidden line 3
Hidden line 4
Hidden line 5
Hidden line 6
Ending line
%%

^^EXPANDED BLOCKQUOTE
Visible line
^^

[User](tg://user?id=93602376)
"""

print("\n=== MD → ENTITIES ===")
text, entities = parse(md, mode="md")
for e in entities:
    print(type(e).__name__, e)

print("\n=== ENTITIES → HTML ===")
html = unparse(text, entities, mode="html")
print(html)

print("\n=== HTML → ENTITIES ===")
text2, entities2 = parse(html, mode="html")
for e in entities2:
    print(type(e).__name__, e)
