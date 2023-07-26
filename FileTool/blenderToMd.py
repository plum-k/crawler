import os
import shutil
import html2text

def custom_modify_content(content):
    # 在这个函数中实现你的自定义修改逻辑
    # 这里只是一个示例，将文件内容的所有小写字母转换为大写
    return html2text.html2text(content)

def convert_html_to_md(src_dir, dest_dir):
    # 替换反斜杠为正斜杠，避免转义问题
    src_dir = src_dir.replace('\\', '/')
    dest_dir = dest_dir.replace('\\', '/')

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.html'):
                # 获取文件的相对路径，去除 .html 后缀
                relative_path = os.path.relpath(root, start=src_dir)
                dest_subdir = os.path.join(dest_dir, relative_path)

                # 创建目标文件所在的目录（如果不存在）
                os.makedirs(dest_subdir, exist_ok=True)

                # 拼接目标文件的完整路径，将 .html 替换为 .md
                dest_path = os.path.join(dest_subdir, os.path.splitext(file)[0] + '.md')

                # 复制文件内容并写入新文件，同时调用自定义函数修改文件内容
                src_file_path = os.path.join(root, file)
                with open(src_file_path, 'r') as src_file:
                    content = src_file.read()

                modified_content = custom_modify_content(content)

                with open(dest_path, 'w') as dest_file:
                    dest_file.write(dest_path + '\n' + modified_content)


# 示例用法
# 示例用法
src_directory = r'C:\Users\l\Downloads\blender_manual_html\blender_manual_vexp_zh-hans'
dest_directory = r'./out'
convert_html_to_md(src_directory, dest_directory)
