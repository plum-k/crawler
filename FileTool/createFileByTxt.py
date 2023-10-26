import os

def get_next_out_directory():
    i = 1
    while True:
        dir_name = "out{}".format(i)
        if not os.path.exists(dir_name):
            return dir_name
        i += 1

def create_files_from_txt(txt_file):
    out_directory = get_next_out_directory()

    # 创建out目录（如果不存在）
    if not os.path.exists(out_directory):
        os.makedirs(out_directory)

    with open(txt_file, 'r',encoding='utf-8') as file:
        for line in file:
            # 去除每行两边的空格和换行符
            file_name = line.strip()

            # 将".txt"后缀替换为".md"
            file_name = os.path.splitext(file_name)[0] + ".md"

            # 创建文件在out目录中
            file_path = os.path.join(out_directory, file_name)
            with open(file_path, 'w',encoding='utf-8') as new_file:
                # 可选：在每个文件中写入一些初始内容
                new_file.write("# {}".format(os.path.splitext(file_name)[0]))

            print("Created file: {}".format(file_path))

if __name__ == "__main__":
    # 请替换为你的txt文件路径
    txt_file_path = "textfile.txt"
    create_files_from_txt(txt_file_path)
