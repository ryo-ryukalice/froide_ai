import sys
import random
import MeCab

# 形態素解析
def split_morpheme(text):
    return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")

# マルコフ連鎖テーブル
def markov_chain(words):
    markov = {}
    w1 = ""
    w2 = ""
    for word in words:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word
    return markov

# ユーザー入力文からランダムに取得した形態素を起点に、マルコフ連鎖で回答文を生成
def answer(user_morphemes, markov):
    sentence = ""

    count = 0
    w1 = ''
    w2 = ''
    while True:
        count += 1
        keys = random.choice(list(markov.keys()))
        if keys[0] in user_morphemes:
            w1 = keys[0]
            w2 = keys[1]
            break
        if count > len(markov):
            return "AI: 質問の内容を理解できませんでした"

    count = 0
    while w2 not in ["。", "！", "？", "!", "?", "."]:
        tmp = random.choice(markov[(w1, w2)])
        sentence += tmp
        w1, w2 = w2, tmp
        count += 1
        if count > len(markov):break
    return "AI: " + sentence

if __name__ == "__main__":
    morphemes = split_morpheme(open("import.txt", "r").read())
    markov = markov_chain(morphemes)

    print("AI: 就職に関するお悩みをどうぞ")

    while True:
        user_input = input("あなた: ")
        if user_input == "": continue
        if user_input == "ありがとう": break

        # ユーザー入力を形態素解析してマルコフ連鎖テーブルに加える
        user_morphemes = split_morpheme(user_input)
        morphemes += split_morpheme(user_input)
        markov = markov_chain(morphemes)

        print(answer(user_morphemes, markov))

    print("AI: どういたしまして")
