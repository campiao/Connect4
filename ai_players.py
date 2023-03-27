import math
import random

from board_methods import *


def minimax(board, depth, maximazingPlayer):
    moves = get_valid_moves(board)
    if depth == 0 or game_over(board):
        if game_over(board):
            return None, 1
        print(board)
        return None, evaluation_segment(board)
    if maximazingPlayer:
        value = -math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, 2)
            new_score = minimax(child, depth-1, False)[1]
            if new_score>value:
                value = new_score
                final_move = move
        return final_move, value
    else:
        value = math.inf
        final_move = random.choice(moves)
        for move in moves:
            child = [row[:] for row in board]
            do_move(child, move, 1)
            new_score = minimax(child, depth-1, True)[1]
            if new_score < value:
                value = new_score
                final_move = move
        return final_move, value
