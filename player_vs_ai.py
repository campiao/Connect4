from ai_players import *


def play_vs_minimax(board, ai_player_num):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):
        if ai_player_num == 2:

            while not jogada_pX(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            move, value = minimax(board, 4, True, -1, 2)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break
        else:
            move, value = minimax(board, 4, True, 1, 1)
            do_move(board, move, 1)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            while not jogada_pY(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")

def play_vs_alpha_beta(board, ai_player_num):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):
        if ai_player_num == 2:

            while not jogada_pX(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            move, value = alpha_beta(board, 4, True, -math.inf, math.inf, -1, 2)
            print(value)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break
        else:
            move, value = alpha_beta(board, 4, True, -math.inf, math.inf, 1, 1)
            do_move(board, move, 1)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            while not jogada_pY(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")


def play_vs_MCTS(board, ai_player_num):
    imprimir_tabuleiro(board)
    while vericar_board_vazia(board):
        if ai_player_num == 2:

            while not jogada_pX(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            value = MONTE_CARLO_TREE_SEARCH(board, 20000)
            do_move(board, value, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break
        else:
            move = MONTE_CARLO_TREE_SEARCH(board, 20000)
            do_move(board, move, 1)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                break

            while not jogada_pY(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")