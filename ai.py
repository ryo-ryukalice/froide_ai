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

    print("AI: ななこが、あなたの就職に関するお悩みを、な～んでも聞くよ！")

    while True:
        user_input = input("あなた: ")
        if user_input == "": continue
        if user_input == "ありがとう": break

        # ユーザー入力をインポートテキストに追記する
        if (re.match("覚えて: ", user_input)):
            import_text.add(user_input.replace("覚えて: ", ""))
            print("AI: 覚えたよ！")
            continue

        # ユーザー入力を形態素解析
        user_morphemes = morpheme_analyzer.analyze(user_input)

        # 定型文から回答を取得
        text = fixed_phrase.answer(user_input)

        # 定型文の回答がなければマルコフ連鎖で回答
        if text == "":text = markov.answer(user_morphemes)

        print("AI: " + text)

    print("AI: こちらこそありがとう☆　またお話しようね♪")
