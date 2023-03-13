from lxml import etree

indexTree = etree.parse("a.html", etree.HTMLParser())
root_li = indexTree.xpath("/html/body/ul/li")

def get_name(node_root, child):
    for i in child:
        node = {}
        node['child'] = []
        node['name'] = i.xpath("./p/a/span/text()")[0]
        node['url'] = "https://docs.unrealengine.com/5.1" + i.xpath("./p/a/@href")[0]
        # print(i.xpath("./p/a/span/text()"))
        c_child = i.xpath("./ul/li")
        node_root['child'].append(node)
        if len(c_child) != 0:
            get_name(node, c_child)


node_root1 = {'child': []}
get_name(node_root1, root_li)
print(node_root1)
