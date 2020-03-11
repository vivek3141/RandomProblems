class TicTacToe:
    def __init__(self):
        self.board = [[" " for i in range(3)] for i in range(3)]
    def play(self, pos, p):
        if self.board[int(pos/3)][pos%3] == " ":
            self.board[int(pos/3)][pos%3] = p
            return True
    def check(self):
        for i in range(3):
            if self._check(self.board[i]): return True
            if self._check([self.board[i][x] for x in range(3)]): return True
        if self._check([self.board[i][i] for i in range(3)]): return True
        if self._check([self.board[i][2-i] for i in range(3)]): return True
        if self.board == [[" " for i in range(3)] for i in range(3)]: print("Tie!"); return True
    def _check(self, x):
        if set(x) == {"O"} or set(x) == {"X"}:
            print(f"{set(x).pop()} won!")
            return True
    def print(self):
        print("-"*13)
        for i in self.board:
            print("|", end="")
            for x in i:
                print(f" {x} |", end="")
            print()
            print("-"*13)

t = TicTacToe()
curr = "X"
while(True):
    t.print()
    pos = input("Play: ")
    if t.play(int(pos)-1, curr):
        curr = "O" if curr == "X" else "X"
    print()
    if t.check(): t.print(); break
