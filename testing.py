ai_piece = {1: "X", 2: "O"}


def print_game_stats(moves_list, moves_time, nodes_pruned, ai, ai_player, resultado):
    print(moves_list)
    print(moves_time)
    print(nodes_pruned)

    stats_file = open("statistics", "at")
    stats_file.write(f"Jogo contra {ai}, {ai} tinhas as pecas {ai_piece[ai_player]},"
                     f" resultado: {resultado}\n"
                     f"Movimentos: {moves_list}\n"
                     f"Tempo de cada movimento: {moves_time}\n"
                     f"Nodes prunned(Num de rollouts no MCTS) por movimento: {nodes_pruned}")

    stats_file.write("\n\n")
