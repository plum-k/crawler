from pathlib import Path
import shutil
path1 = Path("G:/note/houdini/node overview/VOP")

file_list = [f for f in path1.iterdir() if f.is_file()]

for file in file_list:
    shutil.copy(Path("D:/hip/example/vop/base.hip"), Path(f"D:/hip/example/vop/{file.stem}.hip"))

