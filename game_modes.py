from board_methods import *
from ai_players import *
from player_vs_ai import *

def jogador_vs_jogador(board):
    while vericar_board_vazia(board):

        imprimir_tabuleiro(board)

        while not jogada_pX(int(input("Jogada: ")), board):
            imprimir_tabuleiro(board)
            print("Movimento inválido\n")
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


ai_choices = {1: "Minimax Algorithm", 2: "Alpha-Beta Pruning", 3: "Monte Carlo tree search",
              4: "quit"}


def jogador_vs_computador():
    player_num = pick_player_num()
    while player_num < 1 or player_num > 3:
        print("Escolha uma opcao valida...")
        player_num = pick_player_num()
    ai_player = 0
    match player_num:
        case 1:
            ai_player = 2
        case 2:
            ai_player = 1
        case 3:
            quit()
    ai_choice = pick_ai_adversarie(ai_player)
    while ai_choice < 1 or ai_choice > 4:
        print("Escolha uma opcao valida...")
        ai_choice = pick_ai_adversarie(ai_player)
    print(f"Opçao escolhida: {ai_choices[ai_choice]}")
    match ai_choice:
        case 1:
            play_vs_minimax(board_inicial)
        case 2:
            alpha_beta_pruning()
        case 3:
            monte_carlo_tree_search()
        case 4:
            quit()


def computador_vs_computador():
    ai_player1 = pick_ai_adversarie(1)
    while ai_player1 < 1 or ai_player1 > 4:
        print("Escolha uma opcao valida...")
        ai_player1 = pick_ai_adversarie(1)
    print(f"Opçao escolhida: {ai_choices[ai_player1]}")
    if ai_player1 == 4:
        quit()

    ai_player2 = pick_ai_adversarie(2)
    while ai_player2 < 1 or ai_player2 > 4:
        print("Escolha uma opcao valida...")
        ai_player2 = pick_ai_adversarie(2)
    print(f"Opçao escolhida: {ai_choices[ai_player2]}")
    if ai_player2 == 4:
        quit()

def pick_ai_adversarie(player_num):
    print(f"Escolha a AI do jogador {player_num}:\n"
          "\t1 - Minimax Algorithm\n"
          "\t2 - Alpha-Beta Pruning\n"
          "\t3 - Monte Carlo tree search\n"
          "\t4 - quit")
    return int(input())

def pick_player_num():
    print("Escolhe com que peças queres jogar\n"
          "\t1 - comecas em primeiro com as pecas X\n"
          "\t2 - comecas em segundo com as pecas O\n"
          "\t3 - quit")
    return int(input())
