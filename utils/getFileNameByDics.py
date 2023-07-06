from pathlib import Path

path1 = Path("D:/UE_5.2/Engine/Plugins/FX/NiagaraFluids/Content/Modules")
# path1 = Path("D:/UE_5.2/Engine/Plugins/FX/NiagaraFluids/Modules")

root = {
    "isDir": True,
    "name": "",
    "child": []
}

java = ""


# def ff(path):
#     text = ""
#     child = []
#     dirs_list = [f for f in path.iterdir() if f.is_dir()]
#     file_list = [f for f in path.iterdir() if f.is_file()]
#     for i in file_list:
#         file_node = {
#             "isDir": False,
#             "name": i.stem,
#             "child": []
#         }
#         text += "- " + i.stem + "\n"
#         child.append(file_node)
#     for i in dirs_list:
#         a = ff(i)
#         dirs_node = {
#             "isDir": True,
#             "name": i.name,
#             "child": a
#         }
#         text += "## " + i.stem + "\n"
#         text +=
#         child.append(dirs_node)
#     return child

def ff(path):
    text = ""
    dirs_list = [f for f in path.iterdir() if f.is_dir()]
    file_list = [f for f in path.iterdir() if f.is_file()]
    for i in file_list:
        text += "- " + i.stem + "\n"
    for i in dirs_list:
        a = ff(i)
        text += "## " + i.stem + "\n"
        text += "\n"
        text += a
    return text
print(ff(path1))
