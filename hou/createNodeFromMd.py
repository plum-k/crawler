import os
from pathlib import Path

def extract_text_after_hashes(filename):
    extracted_text = []
    with open(filename, 'r') as file:
        for line in file:
            if '##' in line:
                index = line.index('##')
                extracted_text.append(line[index + 2:].strip())  # +2 to skip '##'
    return extracted_text

# 示例使用方法
input_filename = r"E:\note\houdini\node overview\VOP\Control Flow.md"  # 替换为你的输入文件名

# 处理输入文件路径
processed_input_filename = os.path.normpath(input_filename)

extracted_text_list = extract_text_after_hashes(processed_input_filename)
print(extracted_text_list)
extracted_text_list.reverse()
node = hou.node("/obj")

# 要被复制的节点
base_node = hou.node("/obj/geo1")

i = 0
for file in extracted_text_list:
    print(file.replace(" ", "_"))
    # 拷贝节点
    new_node = node.copyItems([base_node])[0]
    # 设置节点的位置
    new_node.setPosition(hou.Vector2((0, i)))
    # 设置节点的名称
    new_node.setName(file.replace(" ", "_"))
    i += 1