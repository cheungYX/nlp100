# encoding: UTF-8
target = "stressed"

def reverse(target):
    if len(target) == 0 or target is None:
        return
    res = ""

    for i in range(len(target) - 1, -1, -1):
      res += target[i]

    print(res)

reverse(target)
