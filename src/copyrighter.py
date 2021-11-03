from os.path import splitext
from glob import glob
from tqdm import tqdm

def prepend(filename, new_content):
    f = open(filename, mode='r+')
    content = f.read()
    f.seek(0)
    f.write(new_content + content)

class coPyRighter:
    def __init__(self, folder : str = ''):
        self._folder = folder
        self._files = glob(folder+"/**/*.*", recursive = True)
        self._cpp = open("/Users/NicolasLepetit/coPyRight/copyrights/cpp.txt", mode='r').read()
        self._py = open("/Users/NicolasLepetit/coPyRight/copyrights/py.txt", mode='r').read()

    def do(self):
        for f in tqdm(self._files):
            ext = splitext(f)[1]
            if ext == ".py":
                prepend(f, self._py)
            elif ext == ".cpp":
                prepend(f, self._cpp)
            else:
                print("currently unsupported file format. Please add it to copyrights")

