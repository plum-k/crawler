from pathlib import Path

path = Path("E:/note/houdini/node/SideFXLabs")
files = [f for f in path.iterdir() if f.is_file()]
dirs = [f for f in path.iterdir() if f.is_dir()]
# dirs = [Path("E:/note/houdini/node/ROP")]


def f2():
    file = Path("./out/" + 'test.md')
    text = ""
    for m_dir in files:
        print(m_dir.stem)
        text += "## " + m_dir.stem + '/n'
        text += "[%s](/houdini/node/VOP NetWork/%s.md)" % (m_dir.stem,m_dir.stem) + "/n"
    file.write_text(text, encoding='UTF-8')

def f1():
    for m_dir in dirs:
        file = Path("./out/" + m_dir.stem + '.md')
        file.touch(exist_ok=True)
        print(file)
        stems = [f.stem for f in m_dir.iterdir() if f.is_file()]
        text = ""

        for stem in stems:
            text += "## " + stem + '\n'
            text += "[%s](/houdini/node/SideFXLabs/%s/%s.md)" % (stem,m_dir.stem, stem) + "\n"
        file.write_text(text, encoding='UTF-8')


f1()
# f2()
