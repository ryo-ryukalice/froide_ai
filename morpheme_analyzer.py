import MeCab

class MorphemeAnalyzer:
    # 形態素解析
    def analyze(self, text):
        return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")

    # 名詞のみ抽出
    def extract_noun(self, text):
        nouns = []
        for chunk in MeCab.Tagger().parse(text).splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            if feature.startswith('名詞'):
                nouns.append(surface)
        return nouns
