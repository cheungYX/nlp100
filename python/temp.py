x = 12
y = "気温"
z = 22.4

def temp(x, y, z):
    # return str(x) + "時の" + y + "は" + str(z)
    return '{x}時の{y}は{z}'.format(x=x, y=y, z=z)

print(temp(x, y, z))
