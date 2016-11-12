import csv
import re

class FixedPhrase:
    def __init__(self, fpath):
        self.fpath = fpath


    # ユーザー入力文が IN 列の文字列パターンにマッチしたら定型文を返す
    def answer(self, user_input):
        self.reader = csv.reader(open(self.fpath, "r"))
        next(self.reader)

        for row in self.reader:
            while row.count("") > 0:
                row.remove("")

            for w in row[1:]:
                if (re.match(w, user_input)):
                    return row[0].replace("{IN}", w)
        return ""
