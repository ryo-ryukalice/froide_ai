import MeCab

class MorphemeAnalyzer:
    # 形態素解析
    def analyze(self, text):
        return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")
