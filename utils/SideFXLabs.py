# D:/houdini结合ue/SideFXLabs-19.5.544/otls

from pathlib import Path

path = Path("C:/Program Files/Adobe/Adobe Substance 3D Designer/resources/packages")
files = [f.stem for f in path.iterdir() if f.is_file()]
# print(files)
for i in files:
    url = "G:/note/substance designer/节点"
    file = Path(url+"/"+ i + ".md")
    file.touch(exist_ok=True)
    file.write_text("# " + i, encoding='UTF-8')
