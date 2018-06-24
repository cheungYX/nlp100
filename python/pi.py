target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

res = []

words = target.split(" ")

for word in words:
	res.append(len(word) - word.count(',') - word.count('.'))

print(res)