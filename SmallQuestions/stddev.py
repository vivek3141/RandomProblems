def listStdDev(li):
    s = 0
    mean = listAvg(li)
    for i in li:
        s = s + (i - mean) ** 2
    return (s / listCount(li)) ** 0.5


def listCount(li):
    s = 0
    for i in li:
        s = s + 1
    return s


def listAvg(li):
    n = listCount(li)
    s = 0
    for i in li:
        s = s + i
    return s / n


