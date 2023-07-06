from pathlib import Path

from jinja2 import Environment, PackageLoader


class HoudiniPipeline:
    def process_item(self, item, spider):
        # 强制创建
        path = Path("./out/"+item['base'])
        path.mkdir(parents=True, exist_ok=True)

        file = Path("./out/"+item['base'] + '/' + item['node_name'] + '.md')
        file.touch(exist_ok=True)

        env = Environment(loader=PackageLoader('houdini', 'templates'))
        template = env.get_template("template.jinja2")
        text = template.render(item)

        file.write_text(text, encoding='UTF-8')
        print("保存文件: ", item['node_name'])
        return item
