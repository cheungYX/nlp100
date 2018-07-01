# encoding: UTF-8
import random

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

res = []

words = target.split(" ")

for word in words:
    if len(word) <= 4:
        res.append(word)
    else:
        chr_list = list(word[1:-1])
        random.shuffle(chr_list)
        result.append(word[0] + ''.join(chr_list) + word[-1])

print(' '.join(result))

