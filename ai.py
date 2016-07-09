import random
import MeCab

def morphological_analysis(text):
    return MeCab.Tagger("-Owakati").parse(text).rstrip(" \n").split(" ")

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

def generate_sentence(markov):
    count = 0
    sentence = ""
    w1, w2 = random.choice(list(markov.keys()))
    while count < len(words):
        tmp = random.choice(markov[(w1, w2)])
        sentence += tmp
        w1, w2 = w2, tmp
        count += 1
    return sentence

if __name__ == "__main__":
    words = morphological_analysis(open("import.txt", "r").read())
    markov = markov_chain(words)
    print(generate_sentence(markov))
