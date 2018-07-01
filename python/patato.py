# encoding: UTF-8
target = "パタトクカシーー"
# print(target[::2])
res = ""

for i in range(1, len(target) - 1, 2):
	res += target[i]

print(res)
