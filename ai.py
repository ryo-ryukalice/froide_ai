import sys
import random
import MeCab
import csv
import re
from markov import *

# 形態素解析
def split_morpheme(text):
    return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")

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

def fixed_answer(user_input):
    reader = csv.reader(open('pattern.csv', 'r'))
    next(reader)

    for row in reader:

        while row.count("") > 0:
            row.remove("")

        for w in row[1:]:
            if (re.match(w, user_input)):
                return row[0].replace('{IN}', w)
    return ""

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

        # 定型文から回答を取得
        text = fixed_answer(user_input)

        # 定型文の回答がなければマルコフ連鎖で回答
        if text == "":
            text = answer(user_morphemes, markov)

        print(text)

    print("AI: どういたしまして")
