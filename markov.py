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
