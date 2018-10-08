def tree(n):
    for i in range(1,n+1):
        print((n-i) * " " + "*"*(2*i-1))


def trunk(n):
    for i in range(3):
        print((n-2) * " " + "*"*3)


def drawTree(base):
    tree(base)
    trunk(base)


def main():
    h = int(input("Enter the height of the tree:"))
    drawTree(h)


if __name__ == "__main__":
    main()
