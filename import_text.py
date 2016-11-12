class ImportText:
    def __init__(self, fpath):
        self.fpath = fpath

    def read(self):
        return open(self.fpath, "r").read()

    def add(self, text):
        open(self.fpath, "a").write(text + "\n")
