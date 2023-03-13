# http://127.0.0.1:48626/nodes/obj/index.html
from lxml import etree
import json
from utils import tool

indexTree = etree.parse("index.html", etree.HTMLParser())
base_td = indexTree.xpath('//div[@class="hierarchy"]/table/tr/td[2]')[0]
# name = base_td.xpath('./a/p/text()')
# href = base_td.xpath('./a/@href')
# print(base_td)
# print(name)
# print(href)
# table = base_td.xpath('./table//tr')
base_node = {'child': []}

base_tr = indexTree.xpath('//div[@class="hierarchy"]/table/tr')


# print(base_table)


def tree(node_root, tr):
    for i in tr:
        node = {'child': []}
        td = i.xpath('./td[2]')[0]
        name = td.xpath('./a/p/text()')
        href = td.xpath('./a/@href')
        node["name"] = name[0].strip()
        # print(aa)
        node["href"] = href[0].strip()
        tr_child = td.xpath('./table/tr')
        node_root['child'].append(node)
        # print(name)
        # print(href)
        if len(tr_child) != 0:
            tree(node, tr_child)


tree(base_node, base_tr)
json_str = json.dumps(base_node)
# print(json_str)
tool.create_file("./x.json", json_str)