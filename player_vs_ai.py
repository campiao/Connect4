from board_methods import *
from ai_players import *

def play_vs_minimax(board):
    while vericar_board_vazia(board):

        imprimir_tabuleiro(board)

        while not jogada_pX(int(input("Jogada: ")), board):
            imprimir_tabuleiro(board)
            print("Movimento inválido\n")
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR X GANHOU \n")
            break

        move, value = minimax(board, 5, True)
        do_move(board, move, 2)
        imprimir_tabuleiro(board)

        if verificar_vencedor(board):
            print("JOGADOR O GANHOU \n")
            break

    if not vericar_board_vazia(board) and not verificar_vencedor(board):
        print("JOGO EMPATADO\n")