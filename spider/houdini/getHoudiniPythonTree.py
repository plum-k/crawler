# http://127.0.0.1:48626/nodes/obj/index.html
from lxml import etree
import json
from utils import tool
indexTree = etree.parse("a.html", etree.HTMLParser())
filtered_body = indexTree.xpath('//div[@class="original filtered-body"]')
# print(filtered_body)
a = filtered_body[0].xpath('//section[@class="heading pull left  "]')
# print(a)
ddd = []
for i in a:
    node = {}
    node['child'] = []
    c = i.xpath("./h2/text()")[0]
    print(i)
    print(c)
    node["root_name"] = c.strip()
    d = i.xpath('./div/ul/li/p[@class="label"]/a')
    # print(d)
    print(len(d))
    for j in d:
        cccc = {}
        aa = j.xpath('./text()')[0]
        bb = j.xpath('./@href')[0]
        cccc["name"] = aa
        # print(aa)
        cccc["href"] = "http://127.0.0.1:48626/hom/hou/" + bb
        node['child'].append(cccc)
    ddd.append(node)

json_str = json.dumps(ddd)
# print(json_str)
utils.create_file("./x.txt", json_str)