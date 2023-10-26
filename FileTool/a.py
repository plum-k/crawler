import os

# 指定要遍历的目录
root_dir = r'C:\Program Files\Adobe\Adobe Substance 3D Painter\resources\starter_assets'

# 用于保存Markdown内容的列表
markdown_content = []
# 用于跟踪已经添加的文件
added_files = set()

# 定义一个递归函数来处理目录
def process_directory(directory, level):
    # 添加目录名到Markdown内容中，并在前面加上#符号
    markdown_content.append('#' * (level + 1) + ' ' + os.path.basename(directory))

    # 遍历目录中的文件和子目录
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            # 如果是子目录，递归处理
            process_directory(item_path, level + 1)
        else:
            # 如果是文件，添加文件名到Markdown内容中，并在前面加上-符号
            file_name = '- ' + item
            if file_name not in added_files:
                markdown_content.append(file_name)
                added_files.add(file_name)

# 调用递归函数开始处理目录
process_directory(root_dir, -1)  # 初始层级为-1

# 将Markdown内容写入文件
with open('output.md', 'w', encoding='utf-8') as file:
    file.write('\n'.join(markdown_content))

print('Markdown文件已生成。')