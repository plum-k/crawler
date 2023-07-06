import html2text

md_text = open('cc.html', 'r', encoding='utf-8').read()

markdown = html2text.html2text(md_text)

with open('make2.md', 'w', encoding='utf-8') as file:

    file.write(markdown)

