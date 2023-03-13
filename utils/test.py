import nltk
from pathlib import Path
# sentence = ""

# print(tokens)


def get(base, s="_"):
    path = Path(base)
    files = [f.stem for f in path.iterdir() if f.is_file()]

    for name in files:
        tokens = nltk.word_tokenize(name)
        print(tokens)
get("D:/web_code/note/houdini/vec/内置函数/CHOP")










