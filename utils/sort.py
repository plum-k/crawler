from pathlib import Path


def sort_file(base, s="_"):
    path = Path(base)
    files = [f.stem for f in path.iterdir() if f.is_file()]

    tree = {}
    for name in files:
        name_list = name.split(s)
        sort = name_list[0]
        if sort not in tree:
            tree[sort] = [Path(base + name + '.md')]
        else:
            sort = tree[sort]
            sort.append(Path(base + name + '.md'))
    # print(path)
    # print(tree)

    for (key, value) in tree.items():
        # print(key)
        # print(value)
        if len(value) > 1:
            new_path = Path(base + key)
            print(value)
            print(new_path)
            new_path.mkdir(parents=True, exist_ok=True)
            for i in value:
                txt_path = Path(i)
                res = txt_path.replace(base + key + "/" + txt_path.name)
    # else:
    #     for i in value:
    #         txt_path = Path(i)
    #         res = txt_path.replace(txt_path.name)


def base(dir):
    path = Path(dir)
    dirs = [f for f in path.iterdir() if f.is_dir()]
    for i in dirs:
        sort_file(str(i)+"/", " ")


base("D:/web_code/note/substance designer/new节点")
# sort_file("D:/web_code/note/substance designer/new节点/Noises", " ")
