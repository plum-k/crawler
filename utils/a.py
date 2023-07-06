# from lxml import etree
from ftfy import fix_text

print(fix_text("\åç¯äº"))
# html_txt = """
# <li id="tag-1">列表项_1</li>
# <li id="tag-2">列表项_2</li>
# <li id="tag-3">列表项_3</li>
# <li id="item-4">列表项_4</li>
# """
#
# # etree选择器
# selector = etree.HTML(html_txt)
# # 使用starts-with()获取class属性开头为"tag"的<li>标签的文本
# contents = selector.xpath('//li[starts-with(@class, "tag")]/text()')
#
# # 打印获取到的文本
# for content in contents:
#     print(content)