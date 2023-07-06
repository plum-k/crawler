from pathlib import Path

node = hou.node("/obj")

base_dir = Path("G:/note/houdini/node/VOP/Array")

file_list = [f for f in base_dir.iterdir() if f.is_file()]

for file in file_list:
    print(file.stem.replace(" ", "_"))
    geo = node.createNode("geo", file.stem.replace(" ", "_"))
node.layoutChildren()



