Connect4

COMO CORRER?

Começar por usar ( $ pip3 install -r requirements.txt) para instalar as bibliotecas necessárias.

1.Abrir o terminal e ir até ao diretório onde o jogo se encontra.

1.1 
 1.1.1 correr o ficheiro __init__.py e seguir as indicações no menu.


Descrição do menu:

    Menu Inicial:
        1.Modo teste (default:desativado): Modo que imprime as estatisticas de cada jogo e ainda as adiciona a um ficheiro.
        2.Modo jogador vs jogador: Modo de jogo local sem nenhum algoritmo:
        3.Modo de jogo jogador vs computador: jogo com intervenção dos algoritmos num dos players.
        4.quit

    Se escolher o modo 3: 
        
        Menu peças:
            1.Começas em primeiro com as peças X
            2.Começas em Segundo com as peças O
            3.quit

        Menu algoritmo
            1.Minimax algorithm
            2.Alpha-Beta Pruning
            3.Monte Carlo tree search
            4.quit

        

                     
Testado em Python com a versão 3.10.11 Windows 11 Home 22H2.

Utilizamos ainda as bibliotecas:numpy.