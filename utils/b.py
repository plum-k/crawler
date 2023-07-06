from pathlib import Path
aaa = ["Comments",
"Parameter Map",
"Special Purpose Parameters",
"事件",
"位置",
"函数",
"创建",
"工具",
"布尔",
"数字型",
"整致",
"特殊用途数",
"矩阵",
"参数脚本",
"转换"]

for m_dir in aaa:
    file = Path("./out/" + m_dir + '.md')
    file.touch(exist_ok=True)