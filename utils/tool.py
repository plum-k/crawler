import os
import html2text

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("创建文件夹成功: " + path)
    else:
        print("已有文件夹成功")


def create_file(path, text):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
            print("创建文件成功: " + path)
    except:
        print("创建失败 " + path)


def html_to_markdown(html):
    return html2text.html2text(html)


def html_to_markdown_and_save(html, path):
    markdown = html_to_markdown(html)
    create_file(path, markdown)
