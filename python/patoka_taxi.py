# encoding: UTF-8
word1 = "パトカー"
word2 = "タクシー"

res = ""

for i,j in zip(range(0, len(word1)), range(0,len(word2))):
	res += word1[i]
	res += word2[j]

print(res)