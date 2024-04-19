import os
from turtle import down

board = [[0 for i in range(0,9)] for j in range(0,9)]
playerRow = 0
playerCol = 0
cpuRow = 0
cpuCol = 0

def showBoard():
    os.system('cls') # clear the input
    print('  1  2  3  4  5  6  7  8  9 ')
    for r in range(0, len(board)):
        data = str(r + 1)
        for c in range(0, len(board[r])):
            if board[r][c] == 0:
                data += ' + '
            elif board[r][c] == 1:
                data += ' ! '
            else:
                data += ' / '
        print(data)


def playerRound():
    global player_row
    global player_col
    player_input = input('Your turn, input the location')
    player_row = int(player_input[0]) - 1
    player_col = int(player_input[1]) - 1
    down(player_row, player_col, True)

    def isPlayerWin():
        global player_row
        global player_col
        count = 1
        for i in range (1, 5):
            if player_row + i < 9 and isBlack(player_row + i, player_col):
                count += 1
            else:
                break
        for i in range (-1, -5, -1):
            if player_row + i > 0 and isBlack(player_row + i, player_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if player_row + i > 0 and player_col + i > 0 and isBlack(player_row + i, player_col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):
            if player_row + i > 0 and player_col + i > 0 and isBlack(player_row + i, player_col):
                count += 1
            else:
                break
        for i in range(1, 5):
            if player_row + i < 9 and player_col + i < 9 and isBlack(player_row + i, player_col):


while True:
    showBoard()
    playeRround()
    if isPlayerWin():
        print('Congrat!')
        break
    cpuRound()
    if isCPUWin()
        print('You lose')
        break