import sys
import re

from import_text import *
from markov import *
from morpheme_analyzer import *
from fixed_phrase import *

if __name__ == "__main__":
    import_text = ImportText()
    morpheme_analyzer = MorphemeAnalyzer()
    fixed_phrase = FixedPhrase()
    markov = Markov(morpheme_analyzer.analyze(import_text.read()))

    name = 'ななこ'

    print("%s: %sが、あなたの就職に関するお悩みを、な～んでも聞くよ！" % (name, name)

    while True:
        user_input = input("あなた: ")
        if user_input == "": continue
        if user_input == "ありがとう": break

        # ユーザー入力をインポートテキストに追記する
        if (re.match("覚えて: ", user_input)):
            text = user_input.replace("覚えて: ", "")
            import_text.add(text)
            markov.add(morpheme_analyzer.analyze(text))
            print("%s: 覚えたよ！" % name)
            continue

        # 定型文から回答を取得
        text = fixed_phrase.answer(user_input)

        # 定型文の回答がなければユーザー入力の名詞を起点にマルコフ連鎖で回答
        if text == "":
            nouns = morpheme_analyzer.extract_noun(user_input)
            text = markov.answer(nouns)

        print("%s: " % name + text)

    print("%s: こちらこそありがとう☆　またお話しようね♪" % name)
