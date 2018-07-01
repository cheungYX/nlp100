# encoding: UTF-8
target = "I am an NLPer"

def n_gram(target, n = 1):
    res = []
    for i in range(0, len(target) - n + 1):
        res.append(target[i:i + n])
    return res

words = target.split(" ")
print(n_gram(words,))