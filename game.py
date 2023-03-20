LINHAS = 6
COLUNAS = 7

board_inicial = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
board_teste =   [[0,1,2,1,2,0,0],[0,0,1,2,1,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]



def imprimir_tabuleiro(board):
    print("\n| 1 || 2 || 3 || 4 || 5 || 6 || 7 |")
    #print("|   ||   ||   ||   ||   ||   ||   |")
    print("|---------------------------------|")
    for linha in reversed(range(LINHAS)):
        for coluna in range(COLUNAS):
            if  board[linha][coluna] == 1:
                print("| X |", end="")

            if  board[linha][coluna] == 2:
                print("| O |", end="")

            if board[linha][coluna] == 0:
                print("|   |", end="")
        print("\n|---------------------------------|")
    print("\n")


def jogada_pX(x, board):
    if(1 <= x <= 7):
        for i in range(LINHAS):
            if board[i][x-1] == 0 and board[LINHAS-1][x-1]==0:
                board[i][x-1] = 1
                return True
        return False
    else: return False

def jogada_pY(x, board):
    if(1 <= x <= 7):
        for i in range(LINHAS):
            if board[i][x-1] == 0 and board[LINHAS-1][x-1]==0:
                board[i][x-1] = 2
                return True
        return False
    else: return False


def vericar_board_vazia(board):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if(board[i][j]==0):
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
        if j1>6:
            break
        if board[i][j1] == board[linha][coluna]:
            count1+=1
        else:
            break
        j1 += 1

    j2 = coluna
    for i in range(linha, 6):
        if j2>6:
            break
        if board[i][j2] == board[linha][coluna]:
            count2+=1
        else:
            break
        j2 -= 1

    if count1 >= 4 or count2 >= 4:
        fourinAROW = True

    return fourinAROW


def verificar_vencedor(board):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if(board[i][j]!= 0):

                if verificar_horizontal(board,i,j):
                    return True
                if verificar_vertical(board,i,j):
                    return True
                if verificar_diagonal(board,i,j):
                    return True
    return False




def play_px_py(board):

    while  vericar_board_vazia(board):

        imprimir_tabuleiro(board)

        while(jogada_pX(int(input("Jogada: ")),board)==False):
            imprimir_tabuleiro(board)
            print("Movimento inválido\n")
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        while(jogada_pY(int(input("Jogada: ")),board)==False):
            imprimir_tabuleiro(board)
            print("Movimento inválido\n")
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if(not vericar_board_vazia(board) and not verificar_vencedor(board)):
        print("JOGO EMPATADO\n")



play_px_py(board_inicial)