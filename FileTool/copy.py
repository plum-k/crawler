import os


def extract_and_write(directory_path):
    for root, _, files in os.walk(directory_path):
        if len(files) > 0:
            # 获取目录名称
            directory_name = os.path.basename(root)

            # 创建新文件路径
            new_file_path = os.path.join(root, f"{directory_name}.md")

            # 遍历目录下的所有文件
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                for file_name in files:
                    if file_name.lower() == "index.md":
                        # 删除 index.md 文件
                        os.remove(os.path.join(root, file_name))
                        continue

                    file_path = os.path.join(root, file_name)
                    with open(file_path, "r", encoding="utf-8") as file:
                        file_contents = file.read()
                        new_file.write(file_contents)
                        new_file.write("\n\n")

                    # 删除原始文件
                    # os.remove(file_path)

# 指定要遍历的目录路径，注意使用双反斜杠或者单正斜杠来兼容 Windows 路径格式
target_directory = r"D:\web_code\note\Blender\建模\modifiers"

extract_and_write(target_directory)
