
def cipher(target):
    res = ""
    for c in target:
        if c.islower():
            res += chr(219 - ord(c))
        else:
            res += c
    return res

print(cipher("hello world"))