import os

def get_next_out_directory():
    i = 1
    while True:
        dir_name = "out{}".format(i)
        if not os.path.exists(dir_name):
            return dir_name
        i += 1

def create_folders_from_txt(txt_file):
    out_directory = get_next_out_directory()

    # 创建新的文件夹
    os.makedirs(out_directory)

    with open(txt_file, 'r',encoding="utf-8") as file:
        for line in file:
            # 去除每行两边的空格和换行符
            folder_name = line.strip()

            # 在新的文件夹中创建子文件夹
            folder_path = os.path.join(out_directory, folder_name)
            os.makedirs(folder_path)

            print("Created folder: {}".format(folder_path))

if __name__ == "__main__":
    # 请替换为你的txt文件路径
    txt_file_path = "textfile1.txt"
    create_folders_from_txt(txt_file_path)
