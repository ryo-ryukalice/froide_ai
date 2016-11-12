import re

from import_text import *
from markov import *
from morpheme_analyzer import *
from fixed_phrase import *

def output(text):
    print("ななこ: " + text)

if __name__ == "__main__":
    import_text = ImportText('import.txt')
    fixed_phrase = FixedPhrase('pattern.csv')
    morpheme_analyzer = MorphemeAnalyzer()
    markov = Markov(morpheme_analyzer.analyze(import_text.read()))

    output('ななこが、あなたの就職に関するお悩みを、な～んでも聞くよ！')
    output('ななこに言葉を覚えさせたいときは@から初めてね！')

    while True:
        user_input = input("あなた: ")
        if user_input == "": continue
        if user_input == "ありがとう": break

        # ユーザー入力をインポートテキストに追記する
        if (re.match('^@|^＠', user_input)):
            text = re.sub('^@|^＠', '', user_input)
            import_text.add(text)
            markov.add(morpheme_analyzer.analyze(text))
            output('覚えたよ！')
            continue

        # 定型文から回答を取得
        text = fixed_phrase.answer(user_input)

        # 定型文の回答がなければユーザー入力の名詞を起点にマルコフ連鎖で回答
        if text == "":
            nouns = morpheme_analyzer.extract_noun(user_input)
            text = markov.answer(nouns)

        if text == "":
            text = "ななこにも分かる言葉で言ってよぉ～☆"

        output(text)

    output("こちらこそありがとう☆　またお話しようね♪")
