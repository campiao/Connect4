import time

from ai_players import *
from board_methods import *
from connect import ConnectState
from mcts import MCTS
import board_config
from testing import *

moves_time = []
game_moves = []
nodes_pruned = []


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
                resultado = "Jogador 1 ganhou"
                break
            start_time = time.time()
            move, value, nodespruned = minimax(board, 5, True, -1, 2)
            nodes_pruned.append(nodespruned)
            game_moves.append(move+1)
            end_time = time.time()-start_time
            end_time = round(end_time,3)
            moves_time.append(end_time)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                resultado = "Jogador 2 ganhou"
                break
        else:
            start_time = time.time()
            move, value,nodespruned = minimax(board, 5, True, 1, 1)
            nodes_pruned.append(nodespruned)
            game_moves.append(move+1)
            end_time = time.time()-start_time
            end_time = round(end_time,3)
            moves_time.append(end_time)
            do_move(board, move, 1)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                resultado = "Jogador 1 ganhou"
                break

            while not jogada_pY(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                resultado = "Jogador 2 ganhou"
                break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")
        resultado = "Empate"

    if board_config.Testing:
        print_game_stats(game_moves,moves_time,nodes_pruned,"Minimax",ai_player_num,resultado)

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
                resultado = "Jogador 1 ganhou"
                break

            start_time = time.time()
            move, value,nodespruned = alpha_beta(board, 8, True, -math.inf, math.inf, -1, 2)
            nodes_pruned.append(nodespruned)
            game_moves.append(move+1)
            end_time = time.time()-start_time
            end_time = round(end_time,3)
            moves_time.append(end_time)
            print(value)
            do_move(board, move, 2)
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                resultado = "Jogador 2 ganhou"
                break
        else:
            start_time = time.time()
            move, value, nodespruned = alpha_beta(board, 8, True, -math.inf, math.inf, 1, 1)
            game_moves.append(move+1)
            nodes_pruned.append(nodespruned)
            end_time = time.time()-start_time
            end_time = round(end_time,3)
            moves_time.append(end_time)
            do_move(board, move, 1)
            imprimir_tabuleiro(board)
            if verificar_vencedor(board):
                print("JOGADOR X GANHOU \n")
                resultado = "Jogador 1 ganhou"
                break

            while not jogada_pY(int(input("Jogada: ")), board):
                imprimir_tabuleiro(board)
                print("Movimento inválido\n")
            imprimir_tabuleiro(board)

            if verificar_vencedor(board):
                print("JOGADOR O GANHOU \n")
                resultado = "Jogador 2 ganhou"
                break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")
        resultado="Empate"

    if board_config.Testing:
        print_game_stats(game_moves,moves_time,nodes_pruned,"Alpha-Beta",ai_player_num,resultado)

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
                resultado="Jogador 1 ganhou"
                break

            start_time = time.time()
            mcts.search(3)
            end_time = time.time()-start_time
            end_time = round(end_time,3)
            moves_time.append(end_time)
            move = mcts.best_move()
            game_moves.append(move+1)

            state.move(move)
            mcts.move(move)
            nodes_pruned.append(mcts.num_rollouts)

            #print("Tempo: %d segundos  ||   Rollouts: %d"%(mcts.run_time,mcts.num_rollouts))

            state.print()

            if state.game_over():
                print("JOGADOR O GANHOU \n")
                resultado="Jogador 2 ganhou"  
                break
    else:

        state = ConnectState()
        mcts = MCTS(state)

        state.print()

        while not state.game_over():
            start_time = time.time()
            mcts.search(3)
            move = mcts.best_move()
            end_time = time.time()-start_time
            end_time = round(end_time, 3)
            moves_time.append(end_time)
            game_moves.append(move+1)
            state.move(move)
            mcts.move(move)
            nodes_pruned.append(mcts.num_rollouts)
            
            #print("Tempo: %d segundos  ||   Rollouts: %d"%(mcts.run_time,mcts.num_rollouts))

            state.print()

            if state.game_over():
                print("JOGADOR X GANHOU \n")
                resultado=" Jogador 1 ganhou"
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
                resultado="Jogador 2 ganhou"  
                break

    if board_config.Testing:
        print_game_stats(game_moves,moves_time,nodes_pruned,"MCTS",ai_player_num,resultado)


