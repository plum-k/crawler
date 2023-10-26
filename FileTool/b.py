import os


def delete_empty_directories(directory):
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
                print(f"Deleted empty directory: {dir_path}")
            except OSError as e:
                print(f"Error deleting directory {dir_path}: {e}")


if __name__ == "__main__":
    directory_to_search = r'E:\note\ue_c++\Code'  # 替换为你要搜索的目录
    delete_empty_directories(directory_to_search)
