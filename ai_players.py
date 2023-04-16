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
            if alpha >= beta:
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
            if alpha >= beta:
                break
        return final_move, value


##MONTECARLO TREE SEARCH

def MONTE_CARLO_TREE_SEARCH(state, num_iter):
    # state,action,visits,wins,children,parent
    tree = [state, None, 0, 0, [], None]
    flag = True
    for i in range(num_iter):
        if not tree[4]:  # Verifica se tree[4] é uma lista vazia
            EXPAND(tree, True)  # Adiciona um novo nó filho
            flag = False
        leaf = SELECT(tree)
        if leaf is None:
            continue
        child = EXPAND(leaf, flag)
        flag = True
        if child is None:
            continue
        result = SIMULATE(child)
        BACK_PROPAGATE(result, child)
    best_child = max(tree[4], key=lambda x: x[3] / x[2])
    return best_child[1]


def UCT(node):
    # calculate the UCT value of a node
    if node[2] == 0:
        return math.inf
    exploration = math.sqrt(math.log(node[5][2]) / node[2])
    return node[3] / node[2] + 2 * exploration


def EXPAND(node, flag):
    # add a new child node to the tree
    legal_actions = get_valid_moves(node[0])
    if not legal_actions:
        return None
    chosen_action = random.choice(legal_actions)
    new_state = [row[:] for row in node[0]]
    if flag:
        do_move(new_state, chosen_action, 2)
    else:
        do_move(new_state, chosen_action, 1)
    new_node = [new_state, chosen_action, 0, 0, [], node]
    node[4].append(new_node)
    return new_node


def SELECT(node):
    # select the most promising child of a node based on UCT value
    while len(node[4]) > 0:
        # skip over nodes with no children
        child_nodes = [child for child in node[4] if child is not None]
        if not child_nodes:
            return None
        child_scores = [(UCT(child), child) for child in child_nodes]
        node = max(child_scores, key=lambda x: x[0])[1]
        if node[0] is None:
            return None
    return node


def SIMULATE(node):
    state = node[0]
    flag = True
    while not terminal_test(state):
        legal_actions = get_valid_moves(state)
        if not legal_actions:
            return 0  # game ended in a tie
        action = random.choice(legal_actions)
        if flag:
            do_move(state, action, 2)
            flag = False
        else:
            do_move(state, action, 1)
            flag = True
    return get_result(state)


def BACK_PROPAGATE(result, node):
    # update the win and visit count of each node along the path from the given node to the root
    while node is not None:
        node[2] += 1
        if result == 1:
            node[3] += 1
        node = node[5]
