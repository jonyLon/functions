import random
mines = 5
size = 10
board = [[0 for i in range(size)] for i in range(size)]
flags = [[False for i in range(size)] for i in range(size)]
# letters = "abcdefghij"
numbers = range(0, 10)


def printBoard():
    print("\t", end="   ")
    for el in numbers:
        print(" ", el, end=" ", sep="")
    print()
    for i in numbers:
        if i == size:
            print("\t", end="")
            print(i, end="|")
        else:
            print("\t", end="")
            print(i, end=" |")
        for n in range(size):
            if not flags[i][n]:
                print(" . ", end="")
            else:
                if board[i][n] == 0:
                    print(" ", board[i][n], sep="", end=" ")
                elif board[i][n] == 1:
                    print(' \033[34m', board[i][n], '\033[0m', sep="", end=" ")
                elif board[i][n] == 2:
                    print(' \033[32m', board[i][n], '\033[0m', sep="", end=" ")
                elif board[i][n] == 3:
                    print(' \033[35m', board[i][n], '\033[0m', sep="", end=" ")
                elif board[i][n] == 4:
                    print(' \033[36m', board[i][n], '\033[0m', sep="", end=" ")
                elif board[i][n] == 5:
                    print(' \033[33m', board[i][n], '\033[0m', sep="", end=" ")
                else:
                    print(' \033[31m', board[i][n], '\033[0m', sep="", end=" ")
        print()


def placeMines():
    count = 0
    while count < mines:
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        if board[x][y] != "*":
            board[x][y] = "*"
            count += 1


def countMines(x, y):
    count = 0
    if x > 0 and board[x-1][y] == "*":
        count += 1
    if x < size-1 and board[x+1][y] == "*":
        count += 1
    if y > 0 and board[x][y-1] == "*":
        count += 1
    if y < size - 1 and board[x][y+1] == "*":
        count += 1
    if y > 0 and x > 0 and board[x-1][y-1] == "*":
        count += 1
    if y < size - 1 and x < size - 1 and board[x+1][y+1] == "*":
        count += 1
    if x > 0 and y < size - 1 and board[x-1][y+1] == "*":
        count += 1
    if x < size - 1 and y > 0 and board[x+1][y-1] == "*":
        count += 1
    return count


def showFlags(x, y):
    if board[x][y] == "*":
        print("Game over")
        flags[x][y] = True
        return False
    if not flags[x][y]:
        board[x][y] = countMines(x, y)
        flags[x][y] = True
        if board[x][y] == 0:
            if x > 0 and board[x-1][y] != '*':
                showFlags(x-1, y)
            if x < size-1 and board[x+1][y] != "*":
                showFlags(x+1, y)
            if y > 0 and board[x][y-1] != "*":
                showFlags(x, y-1)
            if y < size - 1 and board[x][y+1] != "*":
                showFlags(x, y+1)
            if x > 0 and y > 0 and board[x-1][y-1] != "*":
                showFlags(x-1, y-1)
            if x < size-1 and y < size - 1 and board[x+1][y+1] != "*":
                showFlags(x+1, y+1)
            if x > 0 and y < size - 1 and board[x-1][y+1] != "*":
                showFlags(x-1, y+1)
            if x < size - 1 and y > 0 and board[x+1][y-1] != "*":
                showFlags(x+1, y-1)


def check():
    counter = 0
    for i in flags:
        counter += i.count(True)
    return counter == size*size - mines


def game():
    placeMines()
    while True:
        printBoard()
        if check():
            print("Congratulation!")
            break
        x, y = list(map(int, input().split()))
        print(x, y)
        res = showFlags(x, y)
        if res == False:
            break
    printBoard()


game()
