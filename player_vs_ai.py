from ai_players import *
from board_methods import *
from connect import ConnectState
from mcts import MCTS

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

            move, value = minimax(board, 5, True, -1, 2)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break
        else:
            move, value = minimax(board, 5, True, 1, 1)
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

            move, value = alpha_beta(board, 8, True, -math.inf, math.inf, -1, 2)
            print(value)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                break
        else:
            move, value = alpha_beta(board, 8, True, -math.inf, math.inf, 1, 1)
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

def play_vs_MCTS(ai_player_num):
    if ai_player_num == 2:
        state = ConnectState()
        mcts = MCTS(state)

        state.print()

        while not state.game_over():

            user_move = int(input())
            user_move -= 1
            while user_move not in state.get_legal_moves():
                print("Movimento invalido")
                user_move = int(input())
                user_move -= 1

            state.move(user_move)
            mcts.move(user_move)

            state.print()

            if state.game_over():
                print("JOGADOR X GANHOU \n")
                break

            mcts.search(3)
            move = mcts.best_move()

            state.move(move)
            mcts.move(move)
            print("Tempo: %d segundos  ||   Rollouts: %d"%(mcts.run_time,mcts.num_rollouts))

            state.print()

            if state.game_over():
                print("JOGADOR O GANHOU \n")
                break
    else:

        state = ConnectState()
        mcts = MCTS(state)

        state.print()

        while not state.game_over():
            mcts.search(3)
            move = mcts.best_move()
            state.move(move)
            mcts.move(move)
            print("Tempo: %d segundos  ||   Rollouts: %d"%(mcts.run_time,mcts.num_rollouts))

            state.print()

            if state.game_over():
                print("JOGADOR X GANHOU \n")
                break

            user_move = int(input())
            user_move -= 1
            while user_move not in state.get_legal_moves():
                print("Movimento invalido")
                user_move = int(input())
                user_move -= 1

            state.move(user_move)
            mcts.move(user_move)

            state.print()


            if state.game_over():
                print("JOGADOR O GANHOU \n")
                break


