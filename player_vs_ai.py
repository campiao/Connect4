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

from connect import ConnectState
from mcts import MCTS

def play_vs_MCTS():
    state = ConnectState()
    mcts = MCTS(state)

    while not state.game_over():
        print("Current state:")
        state.print()

        user_move = int(input("Enter a move: "))
        while user_move not in state.get_legal_moves():
            print("Illegal move")
            user_move = int(input("Enter a move: "))

        state.move(user_move)
        mcts.move(user_move)

        state.print()

        if state.game_over():
            print("Player one won!")
            break

        print("Thinking...")

        mcts.search(8)
        num_rollouts, run_time = mcts.statistics()
        print("Statistics: ", num_rollouts, "rollouts in", run_time, "seconds")
        move = mcts.best_move()

        print("MCTS chose move: ", move)

        state.move(move)
        mcts.move(move)

        if state.game_over():
            print("Player two won!")
            break
