import requests
from lxml import etree
import json
from utils import tool
import os

f = open('x.json', 'r')
content = f.read()
a = json.loads(content)
f.close()


# print(a)
def tree_file(path, children):
    for i in children:
        if len(i['child']) != 0:
            url = path + i['name'] + "/"
            tool.mkdir(url)
            file = url + i['name'] + '.md'
            r = requests.get(i['href'])
            index = etree.HTML(r.content)
            main = index.xpath('//div[@id="pagecontainer"]')[0]
            s = etree.tostring(main).decode("utf-8")
            print(s)
            tool.html_to_markdown_and_save(etree.tostring(main).decode("utf-8"), file)
            tree_file(url, i['child'])
        else:
            file = path + i['name'] + '.md'
            tool.create_file(file, "")


tree_file("../../getUeC++/", a["child"])
