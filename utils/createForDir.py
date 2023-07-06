from pathlib import Path


def f2(name):
    path = Path("E:/note/ue_c++/Code/" + name)
    dirs = [f for f in path.iterdir() if f.is_dir()]
    file = Path("./out/" + name + ".md")
    text = ""
    i = 20
    for m_dir in dirs:
        if i == 20:
            text += "# " '\n'
            i=0
        print(m_dir.stem)
        text += "## " + m_dir.stem + '\n'
        text += "[](/ue_c++/Code/%s/%s)" % (name, m_dir.stem) + "\n"
        i += 1
    file.write_text(text, encoding='UTF-8')

f2("Developer")
f2("Editor")
f2("Plugins")
f2("Runtime")
