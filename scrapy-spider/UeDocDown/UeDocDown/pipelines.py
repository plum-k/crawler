from pathlib import Path
import html2text

class UedocdownPipeline:
    def process_item(self, item, spider):
        isDir = item['isDir']
        if isDir:
            print("===============")
            print("./out/" + item['dir'])
            path = Path("./out/" + item['dir'])
            print(path.name)
            path.mkdir(parents=True, exist_ok=True)
        else:
            print("-----------------------")
            print("./out/" + item['file'] + ".md")
            file = Path("./out/" + item['file'] + ".md")
            file.touch(exist_ok=True)
            main =  item['main']
            if main is None:
                return item
            markdown = html2text.html2text(item['main'])
            text = '# ' + item['name'] + "\n"
            text += item['href'] + "\n"
            text += markdown
            file.write_text(text, encoding='UTF-8')
            print("保存文件: ", item['name'])
        return item
