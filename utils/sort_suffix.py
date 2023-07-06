from pathlib import Path

def is_suffix(str, s, suffix):
    array = str.split(s)
    if array[len(array) - 1] == suffix:
        return True
    else:
        return False


def base(start_dir, end_path, s, suffix):
    path = Path(start_dir)
    dirs = [f for f in path.iterdir() if f.is_dir()]
    files = [f for f in path.iterdir() if f.is_file()]
    array = []
    file1 = [f for f in files if (f.is_file() and is_suffix(f.stem, s, suffix))]
    # print(file1)
    array.extend(file1)
    for d in dirs:
        file_array = [f for f in d.iterdir() if (f.is_file() and is_suffix(f.stem, s, suffix))]
        # print(file_array)
        array.extend(file_array)
    print(array)
    for f in array:
        f.replace(end_path+"/"+f.name)


base("D:/web_code/note/houdini/node/VOP", "D:/web_code/note/houdini/node/VOP/Shader", " ", "Shader")
# sort_file("D:/web_code/note/substance designer/new节点/Noises", " ")
