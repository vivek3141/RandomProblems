def printNice(a, b):
    part1 = ""
    part2 = ""
    sign = ""
    if a != 0:
        part1 = str(a) + "x"
    if a == -1:
        part1 = "-x"
    if a == 1:
        part1 = "x"
    if b != 0:
        if b > 0:
            part2 = str(b)
            sign = " + "
        else:
            part2 = str(b * -1)
            sign = " - "
    print(part1 + sign + part2)


def main():
    printNice(2, -7)  # sample test code - you can make your own...
    printNice(-1, 9)
    printNice(-14, 0)


main()