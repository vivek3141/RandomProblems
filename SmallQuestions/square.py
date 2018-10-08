def addUpSquaresAndCubes(n):
    s = 0
    c = 0
    for i in range(1, n + 1):
        s = s + i ** 2
        c = c + i ** 3
    return s, c


def sumOfSquares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def sumOfCubes(n):
    return (n ** 2 * ((n + 1) ** 2)) / 4


def main():
    N = int(input("Enter a number:"))
    squares, cubes = addUpSquaresAndCubes(N)
    print("The sum of Squares is", squares)
    print("The sum of Cubes   is", cubes)
    print("The explicit sum of Squares is", sumOfSquares(N))
    print("The explicit sum of Cubes   is", sumOfCubes(N))


if __name__ == "_main_":
    main()
