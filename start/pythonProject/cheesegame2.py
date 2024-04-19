SIZE = 8
board = []
game_finish = False
Chess = ['●', '○']


def initBoard():
    global board
    for i in range(SIZE):
        board.append([])
        for j in range(SIZE):
            board[i].append('+')


def drawBoard():
    global board
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=' ')
            if j == (SIZE - 1):
                print('%1d' % (i + 1), end='')
        print()
        if i == (SIZE - 1):
            for k in range(SIZE):
                print('%-2d' % (k + 1), end='')

    print()


def gameStart():
    global game_finish
    game_round = 0
    while not game_finish:
        if game_round % 2 == 0:
            if not playChess(Chess[0]):
                continue
            game_finish = checkWin(Chess[0])
            if game_finish:
                print('Black win')
        else:
            if not playChess(Chess[1]):
                continue
            game_finish = checkWin(Chess[1])
            if game_finish:
                print('White win')
        game_round += 1
    print('Finish')


def playChess(chess):
    global game_finish
    global board
    flag = False
    if chess == Chess[0]:
        print('Black Turn!')
    else:
        print('White Turn!')
    print('input X:', end='')
    x = eval(input())
    print('input Y:', end='')
    y = eval(input())

    if (x or y) == -1:
        game_finish = True
    elif (x or y) >= SIZE or (x or y) < -1:
        return False

    if board[y - 1][x - 1] == '+':
        board[y - 1][x - 1] = chess
        flag = True
    else:
        flag = False
    drawBoard()
    return flag


def checkWin(chess):
    global board
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == chess:
                try:
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == board[i][j + 4]:
                        return True
                    elif board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == board[i + 4][j]:
                        return True
                    elif board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == \
                            board[i + 4][j + 4]:
                        return True
                    elif board[i][j] == board[i - 1][j - 1] == board[i - 2][j - 2] == board[i - 3][j - 3] == \
                            board[i - 4][j - 4]:
                        return True
                except:
                    print()
    return False


initBoard()

drawBoard()

gameStart()