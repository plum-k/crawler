
from pathlib import Path
import html2text
from jinja2 import Environment, PackageLoader

class GetvexfunctionPipeline:
    def process_item(self, item, spider):
        # 强制创建
        path = Path("./out/" + item['h2'])
        path.mkdir(parents=True, exist_ok=True)

        file = Path("./out/" + item['h2'] + '/' + item['h1'] + '.md')
        file.touch(exist_ok=True)

        markdown = html2text.html2text(item['main'])

        file.write_text(markdown, encoding='UTF-8')
        print("保存文件: ", item['h1'])
        return item
