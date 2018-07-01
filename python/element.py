# encoding: UTF-8
target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
li = [1, 5, 6, 7, 8, 9, 15, 16, 19]

res = {}
words = target.split(" ")

for idx, word in enumerate(words):
	if idx in li:
		es[idx + 1] = word[0]
	else:
		res[idx + 1] = word[0:2]

print(res)