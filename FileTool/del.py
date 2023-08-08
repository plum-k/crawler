import os

import os


def delete_non_matching_files_in_subdirectories(parent_directory):
    if not os.path.exists(parent_directory):
        print("父目录不存在")
        return

    subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

    for subdir in subdirectories:
        subdir_path = os.path.join(parent_directory, subdir)
        for root, dirs, files in os.walk(subdir_path):
            for file in files:
                file_name = os.path.splitext(file)[0]  # 获取文件名，不包含后缀
                subdir_name = os.path.basename(subdir)

                if file_name != subdir_name:  # 如果文件名（不包含后缀）与子目录名不相同
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"已删除文件：{file_path}")


# 用法示例
parent_directory_to_clean = r"D:\web_code\note\Blender\建模\modifiers"
delete_non_matching_files_in_subdirectories(parent_directory_to_clean)
