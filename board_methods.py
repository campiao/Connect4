from board_config import *


def segment(board):
    segments = []
    # horizontal
    for linha in range(6):
        for coluna in range(7):
            segment = board[linha][coluna:4]
            segments.append(segment)
    # diagonal
    for linha in range(3):
        for coluna in range(4):
            segment = [board[linha+i][coluna+i] for i in range(4)]
            segments.append(segment)
    # vertical
    for coluna in range(7):
        for linha in range(3):
            segment = [board[linha+i][coluna] for i in range(4)]
            segments.append(segment)
    return segments


def count(p, seq):
    count = 0
    for num in seq:
        if num == p:
            count += 1
    return count


def evaluation_segment(board, ai):
    segments = segment(board)
    evaluation = 0
    for seq in segments:
        qX = count(1, seq)
        qO = count(2, seq)
        if qO == 2 and qX == 0: evaluation -= 10
        if qO == 3 and qX == 0: evaluation -= 50
        if qO == 1 and qX == 0: evaluation -= 1
        if qO == 0 and qX == 1: evaluation += 1
        if qO == 0 and qX == 2: evaluation += 10
        if qO == 0 and qX == 3: evaluation += 50
    if ai == 1:
        evaluation=evaluation*-1
    return evaluation

#board_inicial = [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#print(evaluation_segment(board_inicial))

def game_over(board):
    return (not vericar_board_vazia(board)) or verificar_vencedor(board)


def imprimir_tabuleiro(board):
    print("\n| 1 || 2 || 3 || 4 || 5 || 6 || 7 |")
    print("|---------------------------------|")
    for linha in reversed(range(LINHAS)):
        for coluna in range(COLUNAS):
            if board[linha][coluna] == 1:
                print("| X |", end="")

            if board[linha][coluna] == 2:
                print("| O |", end="")

            if board[linha][coluna] == 0:
                print("|   |", end="")
        print("\n|---------------------------------|")
    print("\n")


def jogada_pX(x, board):
    if (1 <= x <= 7):
        for i in range(LINHAS):
            if board[i][x - 1] == 0 and board[LINHAS - 1][x - 1] == 0:
                board[i][x - 1] = 1
                return True
        return False
    else:
        return False


def jogada_pY(x, board):
    if (1 <= x <= 7):
        for i in range(LINHAS):
            if board[i][x - 1] == 0 and board[LINHAS - 1][x - 1] == 0:
                board[i][x - 1] = 2
                return True
        return False
    else:
        return False


def vericar_board_vazia(board):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if (board[i][j] == 0):
                return True
    return False


def verificar_horizontal(board, linha, coluna):
    count = 0
    fourinAROW = False

    for j in range(coluna, 7):
        if board[linha][j] == board[linha][coluna]:
            count += 1
        else:
            break
    if count >= 4:
        fourinAROW = True

    return fourinAROW


def verificar_vertical(board, linha, coluna):
    count = 0
    fourinAROW = False

    for i in range(linha, 6):
        if board[i][coluna] == board[linha][coluna]:
            count += 1
        else:
            break
    if count >= 4:
        fourinAROW = True

    return fourinAROW


def verificar_diagonal(board, linha, coluna):
    count1 = 0
    count2 = 0
    fourinAROW = False

    j1 = coluna
    for i in range(linha, 6):
        if j1 > 6:
            break
        if board[i][j1] == board[linha][coluna]:
            count1 += 1
        else:
            break
        j1 += 1

    j2 = coluna
    for i in range(linha, 6):
        if j2 > 6:
            break
        if board[i][j2] == board[linha][coluna]:
            count2 += 1
        else:
            break
        j2 -= 1

    if count1 >= 4 or count2 >= 4:
        fourinAROW = True

    return fourinAROW


def verificar_vencedor(board):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if board[i][j] != 0:

                if verificar_horizontal(board, i, j):
                    return True
                if verificar_vertical(board, i, j):
                    return True
                if verificar_diagonal(board, i, j):
                    return True
    return False

def get_valid_moves(board):
    moves = []
    for col in range(COLUNAS):
        line = last_line(board, col)
        if line is not None:
            moves.append(col)
    return moves

def last_line(board, col):
    for i in range(5,-1,-1):
        if board[i][col]==0:
            return i
    return None

def do_move(board, move, playerNum):
    if move is None:
        return
    for i in range(LINHAS):
        if board[i][move] == 0 and board[LINHAS-1][move] == 0:
            board[i][move] = playerNum
            return