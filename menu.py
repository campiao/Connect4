from game_modes import *

game_modes = {1: "jogador vs jogador", 2: "jogador vs computador", 3: "computador vs computador",
              4: "quit"}
def menu():
    choice = welcome_screen()
    while choice < 1 or choice > 4:
        print("Escolha uma opcao valida...")
        choice = welcome_screen()
    print(f"Opçao escolhida: {game_modes[choice]}")
    match choice:
        case 1:
            jogador_vs_jogador(board_inicial)
        case 2:
            jogador_vs_computador()
        case 3:
            computador_vs_computador()
        case 4:
            quit()

def welcome_screen():
    print("Bem vindo ao jogo Connect4!\n"
          "Escolhe uma opção de jogo:\n"
          "\t1 - jogador vs jogador\n"
          "\t2 - jogador vs computador\n"
          "\t3 - computador vs computador\n"
          "\t4 - quit")
    return int(input())