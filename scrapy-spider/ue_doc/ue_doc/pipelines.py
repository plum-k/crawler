from pathlib import Path
from jinja2 import Environment, PackageLoader


class UeDocPipeline:
    def process_item(self, item, spider):
        # 强制创建
        path = Path(item['dir_url'])
        path.mkdir(parents=True, exist_ok=True)

        file = Path(item['file_url'])
        file.touch(exist_ok=True)

        env = Environment(loader=PackageLoader('ue_doc', 'templates'))
        template = env.get_template("template.jinja2")
        text = template.render(item)

        file.write_text(text,encoding='UTF-8')
        print("保存文件: ", item['file_url'])
        return item
