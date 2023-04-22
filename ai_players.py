import math
import random

from board_methods import *


def minimax(board, depth, maximazingPlayer, playernum, ai_player_num, counter=0):
    if ai_player_num == 2:
        player_piece = 1
    else:
        player_piece = 2
    moves = get_valid_moves(board)
    if depth == 0 or game_over(board):
        if game_over(board):
            if verificar_vencedor(board):
                if playernum == 1:
                    if ai_player_num == 1:
                        return None, -512, counter+1
                    return None, 512, counter+1
                if ai_player_num == 1:
                    return None, 512, counter+1
                return None, -512, counter+1
            return None, 0, counter+1
        return None, evaluation_segment(board, ai_player_num), counter+1
    if maximazingPlayer:
        value = -math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, ai_player_num)
            new_move, new_score, counter = minimax(child, depth - 1, False, playernum * -1, ai_player_num, counter+1)
            if new_score > value:
                value = new_score
                final_move = move
        return final_move, value, counter
    else:
        value = math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, player_piece)
            new_move, new_score, counter = minimax(child, depth - 1, True, playernum * -1, ai_player_num, counter+1)
            if new_score < value:
                value = new_score
                final_move = move
        return final_move, value, counter



def alpha_beta(board, depth, maximizingPlayer, alpha, beta, player_num, ai_player_num):
    if ai_player_num == 2:
        player_piece = 1
    else:
        player_piece = 2
    moves = get_valid_moves(board)
    counter = 1  # Inicializa com 1 para contar a raiz da árvore de busca
    if depth == 0 or game_over(board):
        if game_over(board):
            if verificar_vencedor(board):
                if player_num == 1:
                    if ai_player_num == 1:
                        return None, -512, counter
                    return None, 512, counter
                if ai_player_num == 1:
                    return None, 512, counter
                return None, -512, counter
            return None, 0, counter
        return None, evaluation_segment(board, ai_player_num), counter
    if maximizingPlayer:
        value = -math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, ai_player_num)
            _, new_score, nodes_visited = alpha_beta(child, depth - 1, False, alpha, beta, player_num * -1, ai_player_num)
            counter += nodes_visited
            if new_score > value:
                value = new_score
                final_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return final_move, value, counter
    else:
        value = math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, player_piece)
            _, new_score, nodes_visited = alpha_beta(child, depth - 1, True, alpha, beta, player_num * -1, ai_player_num)
            counter += nodes_visited
            if new_score < value:
                value = new_score
                final_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return final_move, value, counter
