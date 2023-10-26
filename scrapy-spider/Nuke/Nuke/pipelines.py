# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
from pathlib import Path
import html2text

class NukePipeline:
    def process_item(self, item, spider):
        print(item)
        # 强制创建
        path = Path("./out/" + item['sort'])
        path.mkdir(parents=True, exist_ok=True)

        file = Path("./out/" + item['sort'] + '/' + item['name'] + '.md')
        file.touch(exist_ok=True)

        markdown = html2text.html2text(item['main'])
        text = '# ' + item['name'] + "\n"

        text += item['url'] + "\n"
        text += markdown
        file.write_text(text, encoding='UTF-8')
        print("保存文件: ", item['name'])
        return item
