import time

x = 0
y = 0

with open("wwz.txt", "r") as f:
    field = []
    for line in f:
        field.append(list(line.strip()))
    # end for line in f
# end with open
for i in range(0, len(field), 1):
    for j in range(0, len(field[i]), 1):
        if field[i][j] == "Z":
            y = j
            x = i
        # end if feild
    # end for j in range


# end for i in range
def human(f):
    x = 0
    y = 0
    for i in range(0, len(f), 1):
        for j in range(0, len(f[i]), 1):
            if f[i][j] == "H":
                y = j
                x = i
        # end for j in range
    # end for i in range
    if f[x + 1][y] == "Z":
        print(x)
        f[x][y] = "Z"
        f.append([x, y])
        print("You have died")
        return
    # end for if f
    if f[x - 1][y] == "Z":
        f[x][y] = "Z"
        f.append([x - 1, y])
        print("You have died")
        return
    # end for if f
    if f[x][y + 1] == "Z":
        f[x][y] = "Z"
        f.append([x, y + 1])
        print("You have died")
        return
    # end for if f
    if f[x][y - 1] == "Z":
        f[x][y] = "Z"
        f.append([x, y - 1])
        print("You have died")
        return
    else:
        print("You lived")
        return
    # end for if f


# end def human
def breakWall(f):
    x = 4
    y = 7
    z = 0
    w = 0
    try:
        for i in range(0, len(f), 1):
            for j in range(0, len(f[i]), 1):
                if f[j] == "W":
                    print(f[j])
                    # end if f
            # end for j
        # end for i
    except IndexError:
        pass
    return


# end def breakWall
def spread(f, xpos, ypos):
    feild = []
    # try = tries what ever code is written after it for errors if error is encountered sends it to except
    # except = takes the error from try and tells code to skip any index error occured
    try:
        if f[xpos + 1][ypos] == ".":
            f[xpos + 1][ypos] = "Z"
            feild.append([xpos + 1, ypos])
            # end for if f
        if f[xpos - 1][ypos] == ".":
            f[xpos - 1][ypos] = "Z"
            feild.append([xpos - 1, ypos])
            # end for if f
        if f[xpos][ypos - 1] == ".":
            f[xpos][ypos - 1] = "Z"
            feild.append([xpos, ypos - 1])
            # end for if f
        if f[xpos][ypos + 1] == ".":
            f[xpos][ypos + 1] = "Z"
            feild.append([xpos, ypos + 1])
            # end for if f
    # end try
    except IndexError:
        pass
    # end except
    for k in feild:
        f = spread(f, k[0], k[1])
    # end for k in feild
    return f


# end def spread
field = spread(field, x, y)

for i in range(0, len(field), 1):
    print("".join(field[i]))
# End for i in range

human(field)
breakWall(field)
