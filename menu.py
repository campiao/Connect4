from game_modes import *
import board_config

game_modes = {1: "jogador vs jogador", 2: "jogador vs computador", 3: "quit",
              4: "toggle mode de teste"}


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
            quit()
        case 4:
            if board_config.Testing:
                board_config.Testing = False
            else:
                board_config.Testing = True
            menu()


def welcome_screen():
    print("Bem vindo ao jogo Connect4!\n"
          "Escolhe uma opção de jogo:\n"
          "\t1 - jogador vs jogador\n"
          "\t2 - jogador vs computador\n"
          "\t3 - quit\n\n\n"
          f"\t4 - modo de teste (toque para alterar): {board_config.Testing}\n")
    return int(input())
