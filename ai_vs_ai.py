from ai_players import *
from board_methods import *
from time import sleep


def ai_vs_ai(board, ai_player1, ai_player2):
    match ai_player1, ai_player2:
        case 1, 1:
            minimax_vs_minimax(board_inicial)
        case 1, 2:
            minimax_vs_alphabeta(board_inicial)
        case 1, 3:
            minimax_vs_MCTS(board_inicial)
        case 2, 1:
            alphabeta_vs_minimax(board_inicial)
        case 2, 2:
            alphabeta_vs_alphabeta(board_inicial)
        case 2, 3:
            alphabeta_vs_MCTS(board_inicial)


def minimax_vs_minimax(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = minimax(board, 4, True, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move, value = minimax(board, 4, True, -1, 2)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")

def minimax_vs_alphabeta(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = minimax(board, 4, True, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move, value = alpha_beta(board, 4, True, -math.inf, math.inf, -1, 2)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")

def minimax_vs_MCTS(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = minimax(board, 4, True, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move = MONTE_CARLO_TREE_SEARCH(board, 20000)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")


def alphabeta_vs_minimax(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = alpha_beta(board, 4, True, -math.inf, math.inf, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move, value = minimax(board, 4, True, -1, 2)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")

def alphabeta_vs_alphabeta(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = alpha_beta(board, 4, True, -math.inf, math.inf, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move, value = alpha_beta(board, 4, True,-math.inf, math.inf, -1, 2)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")

def alphabeta_vs_MCTS(board):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):

        move, value = alpha_beta(board, 4, True, -math.inf, math.inf, 1, 1)
        do_move(board, move, 1)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move = MONTE_CARLO_TREE_SEARCH(board, 20000)
        do_move(board, move, 2)
        sleep(1)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")
