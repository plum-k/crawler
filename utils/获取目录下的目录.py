from pathlib import Path

path = Path("C:/Program Files/Epic Games/UE_5.2/Engine/Plugins")
dirs = [f for f in path.iterdir() if f.is_dir()]


def f2():
    file = Path("./out/" + 'test.md')
    text = ""
    root = []
    for m_dir in dirs:
        node = {
            "name": m_dir.stem,
            "ch": []
        }
        path1 = Path("./out/" + m_dir.stem)
        path1.mkdir(parents=True, exist_ok=True)
        text += "# " + m_dir.stem + '\n'
        dirs1 = [f for f in Path(m_dir).iterdir() if f.is_dir()]
        for m_dir1 in dirs1:
            node["ch"].append(m_dir1.stem)
            text += "## " + m_dir1.stem + '\n'
            text += "[](/ue_c++/Code/Plugins/%s)" % (m_dir1.stem) + "\n"
            path2 = Path("./out/" + m_dir.stem + "/" + m_dir1.stem)
            path2.mkdir(parents=True, exist_ok=True)
            file = Path("./out/" + m_dir.stem + "/" + m_dir1.stem + "/" + "Index.md")
            file.touch(exist_ok=True)
        root.append(node)
    file = Path("./out/" + "name" + ".md")
    file.write_text(text, encoding='UTF-8')
    print(root)


f2()
