from pathlib import Path
from jinja2 import Environment, PackageLoader


class UeDocPipeline:
    # 类
    # def process_item(self, item, spider):
    #     list = item['url'].split("https://docs.unrealengine.com/5.2/en-US/API/")
    #     a = list[1]
    #     c = a.split('/')
    #     a.rstrip("/" + c[-1])
    #     a = "./out/"+a
    #     # 强制创建
    #     path = Path(a)
    #     path.mkdir(parents=True, exist_ok=True)
    #
    #     file = Path(a + ".md")
    #     file.touch(exist_ok=True)
    #
    #     env = Environment(loader=PackageLoader('ue_doc', 'templates'))
    #     template = env.get_template("template.jinja2")
    #     text = template.render(item)
    #
    #     file.write_text(text, encoding='UTF-8')
    #     print("保存文件: ", a)
    #     return item
    # 枚举
    # def process_item(self, item, spider):
    #     list = item['url'].split("https://docs.unrealengine.com/5.2/en-US/API/")
    #     a = list[1]
    #     c = a.split('/')
    #     a.rstrip("/" + c[-1])
    #     a = "./out/"+a
    #     # 强制创建
    #     path = Path(a)
    #     path.mkdir(parents=True, exist_ok=True)
    #
    #     file = Path(a + ".md")
    #     file.touch(exist_ok=True)
    #
    #     env = Environment(loader=PackageLoader('ue_doc', 'templates'))
    #     template = env.get_template("enum.jinja2")
    #     text = template.render(item)
    #
    #     file.write_text(text, encoding='UTF-8')
    #     print("保存文件: ", a)
    #     return item
    # 函数
    def process_item(self, item, spider):
        list = item['url'].split("https://docs.unrealengine.com/5.2/en-US/API/")
        a = list[1]
        c = a.split('/')
        a.rstrip("/" + c[-1])
        a = "./out/"+a
        # 强制创建
        path = Path(a)
        path.mkdir(parents=True, exist_ok=True)

        file = Path(a + ".md")
        file.touch(exist_ok=True)

        env = Environment(loader=PackageLoader('ue_doc', 'templates'))
        template = env.get_template("fun.jinja2")
        text = template.render(item)

        file.write_text(text, encoding='UTF-8')
        print("保存文件: ", a)
        return item