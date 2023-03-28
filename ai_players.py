import math
import random

from board_methods import *


def minimax(board, depth, maximazingPlayer, playernum, ai_player_num):
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
                        return None, -512
                    return None, 512
                if ai_player_num == 1:
                    return None, 512
                return None, -512
            return None, 0
        return None, evaluation_segment(board, ai_player_num)
    if maximazingPlayer:
        value = -math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, ai_player_num)
            new_score = minimax(child, depth - 1, False, playernum * -1, ai_player_num)[1]
            if new_score > value:
                value = new_score
                final_move = move
        return final_move, value
    else:
        value = math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, player_piece)
            new_score = minimax(child, depth - 1, True, playernum * -1, ai_player_num)[1]
            if new_score < value:
                value = new_score
                final_move = move
        return final_move, value


def alpha_beta(board, depth, maximazingPlayer, alpha, beta, playernum, ai_player_num):
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
                        return None, -512
                    return None, 512
                if ai_player_num == 1:
                    return None, 512
                return None, -512
            return None, 0
        return None, evaluation_segment(board, ai_player_num)
    if maximazingPlayer:
        value = -math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, ai_player_num)
            new_score = alpha_beta(child, depth - 1, False, alpha, beta, playernum * -1, ai_player_num)[1]
            if new_score > value:
                value = new_score
                final_move = move
            alpha = max(alpha, value)
            if alpha>=beta:
                break
        return final_move, value
    else:
        value = math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, player_piece)
            new_score = alpha_beta(child, depth - 1, True, alpha, beta, playernum * -1, ai_player_num)[1]
            if new_score < value:
                value = new_score
                final_move = move
            beta = min(beta, value)
            if alpha>=beta:
                break
        return final_move, value

