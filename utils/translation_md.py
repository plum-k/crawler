from pathlib import Path

import re


def translation_md(file: str):
    path = Path(file)
    text = path.read_text(encoding='utf-8')
    # print(text)
    list_ = re.findall(r'(?!.)(?:[A-Za-z0-9.]| |\n)+', text, re.M | re.I)
    # print(list_.group())
    print(list_)
    for i in list_:
        print(i)

translation_md("./Attribute Adjust Color.md")
# translation_md("./c.md")
