class ImportText:
    FILE_NAME = "import.txt"

    def read(self):
        return open(self.FILE_NAME, "r").read()

    def add(self, text):
        open(self.FILE_NAME, "a").write(text + "\n")
