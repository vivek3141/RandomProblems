count = 0
zombie = 0
x = 0
y = 0

with open("data.txt", "r") as f:
    field = f.read().split("\n")

for i in range(0, len(field), 1):
    for j in range(0, 40, 1):
        if field[i][j] == "Z":
            x = j
            y = i


def spread(f, xpos, ypos):
    li = []
    try:
        if f[xpos + 1][ypos] == ".":
            temp = list(f[xpos + 1])
            temp[ypos] = "Z"
            temp = "".join(temp)
            f[xpos + 1] = temp
            li.append([xpos + 1, ypos])
        if f[xpos - 1][ypos] == ".":
            temp = list(f[xpos - 1])
            temp[ypos] = "Z"
            temp = "".join(temp)
            f[xpos - 1] = temp
            li.append([xpos - 1, ypos])
        if f[xpos][ypos - 1] == ".":
            temp = list(f[xpos])
            temp[ypos - 1] = "Z"
            temp = "".join(temp)
            f[xpos] = temp
            li.append([xpos, ypos - 1])
        if f[xpos][ypos + 1] == ".":
            temp = list(f[xpos])
            temp[ypos + 1] = "Z"
            temp = "".join(temp)
            f[xpos] = temp
            li.append([xpos, ypos + 1])
    except IndexError:
        pass
    for k in li:
        f = spread(f, k[0], k[1])
    return f


# field = spread_right(field, y, x)
field = spread(field, y, x)
for i in range(0, len(field), 1):
    print(field[i])
