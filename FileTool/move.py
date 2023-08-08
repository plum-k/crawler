import os
import shutil


def move_files_in_subdirectories(root_directory):
    for root, _, files in os.walk(root_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            parent_directory = os.path.dirname(root)
            destination_path = os.path.join(parent_directory, file_name)

            try:
                shutil.move(file_path, destination_path)
                print(f"文件已成功移动到上一层目录: {destination_path}")
            except Exception as e:
                print(f"移动文件时出错: {e}")


# 替换为你的根目录路径
root_directory =r"D:\web_code\note\Blender\建模\modifiers"
move_files_in_subdirectories(root_directory)
