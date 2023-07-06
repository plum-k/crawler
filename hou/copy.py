from pathlib import Path

node = hou.node("/obj")

base_dir = Path("E:/note/houdini/node/SOP/KinFX")

file_list = [f for f in base_dir.iterdir() if f.is_file()]
# 要被复制的节点
base_node = hou.node("/obj/geo1")

file_list.reverse()
i = 0
for file in file_list:
    print(file.stem.replace(" ", "_"))
    # 拷贝节点
    new_node = node.copyItems([base_node])[0]
    # 设置节点的位置
    new_node.setPosition(hou.Vector2((0, i)))
    # 设置节点的名称
    new_node.setName(file.stem.replace(" ", "_"))
    i += 1
# node.layoutChildren()
