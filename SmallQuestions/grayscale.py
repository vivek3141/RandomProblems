# My Name:

# don't forget to import the math library...
import math


def eToX(x):
    term = 1
    sum = 1
    n = 2
    while term > 10E-12:
        f = 1
        for i in range(1,n + 1):
            f *= i
        term = (x ** n) / f
        sum += term
        print("")
        print("n: ", n, "\tterm: ", term, "\tsum: ", sum)
        n += 1
    print("my e^x: ", sum)
    print("real e^x: ", math.exp(n))
    return sum


def main():
    eToX(1.5)
    pass


if __name__ == "__main__":
    main()

