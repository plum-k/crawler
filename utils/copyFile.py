from pathlib import Path
import shutil
path1 = Path("E:/note/houdini/node overview/ROP")

file_list = [f for f in path1.iterdir() if f.is_file()]

for file in file_list:
    shutil.copy(Path("E:/Houdini_Example/example/rop/example.hip"), Path(f"E:/Houdini_Example/example/rop/{file.stem}.hip"))

