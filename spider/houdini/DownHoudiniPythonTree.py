import requests
from lxml import etree
import json
from utils import tool

f = open('x.txt', 'r')
content = f.read()
a = json.loads(content)
f.close()
# print(a)
for i in a:
# for i in [a[0]]:
    print(i)
    root_path = "./" + i['root_name']
    utils.mkdir(root_path)
    for j in i['child']:
        r = requests.get(j['href'])
        index = etree.HTML(r.content)
        main = index.xpath('//main')[0]
        # type1 = index.xpath('//span@class="subtitle"')[0]
        utils.html_to_markdown_and_save(etree.tostring(main).decode("utf-8"), root_path + "/" + j['name'] + ".md")
        # if type1 == 'class':
        #     print('')
        # elif type1 == 'HOM function':
        #     print('c')
#
