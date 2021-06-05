"""
Criar um jogo da velha.
Aqui estão os requisitos:
- 2 jogadores devem poder jogar o jogo (ambos sentados no mesmo computador)
- O quadro deve ser impresso sempre que um jogador faz uma jogada
- Você deve ser capaz de aceitar a entrada da posição do jogador e, em seguida, colocar um símbolo na placa
"""

# pra limpar o terminal
import os

# tabuleiro
quadro_do_jogo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# exibindo o jogo (matriz)
def imprime_tabuleiro():
    """
    Função que imprime na tela o tabuleiro a cada jogada!
    """
    # pra limpar o terminal toda vez que a função for chamada:
    os.system('clear') or None

    # printando tabuleiro
    cont = 1
    print(f'\033[1;36mQUADRO DO JOGO\033[m')
    print('-' *11)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'{quadro_do_jogo[linha][coluna]}', end= ' | ')
            if cont % 3 == 0:
                print('\n')
                print('-' *11)
            
            cont += 1


# analisando se a jogada é possível ou não
def analisando_jogada(posicao_jogada, jogada):
    """
    Função que analisa se a jogada é válida ou não.
    Se uma casa já estiver preenchida, a mesma não recebe nova jogada.
    """
    if posicao_jogada == 1 and quadro_do_jogo[0][0] != 'X' and quadro_do_jogo[0][0] != 'O':
        quadro_do_jogo[0][0] = jogada

    elif posicao_jogada == 2 and quadro_do_jogo[0][1] != 'X' and quadro_do_jogo[0][1] != 'O':
        quadro_do_jogo[0][1] = jogada

    elif posicao_jogada == 3 and quadro_do_jogo[0][2] != 'X' and quadro_do_jogo[0][2] != 'O':
        quadro_do_jogo[0][2] = jogada

    elif posicao_jogada == 4 and quadro_do_jogo[1][0] != 'X' and quadro_do_jogo[1][0] != 'O':
        quadro_do_jogo[1][0] = jogada

    elif posicao_jogada == 5 and quadro_do_jogo[1][1] != 'X' and quadro_do_jogo[1][1] != 'O':
        quadro_do_jogo[1][1] = jogada

    elif posicao_jogada == 6 and quadro_do_jogo[1][2] != 'X' and quadro_do_jogo[1][2] != 'O':
        quadro_do_jogo[1][2] = jogada

    elif posicao_jogada == 7 and quadro_do_jogo[2][0] != 'X' and quadro_do_jogo[2][0] != 'O':
        quadro_do_jogo[2][0] = jogada

    elif posicao_jogada == 8 and quadro_do_jogo[2][1] != 'X' and quadro_do_jogo[2][1] != 'O':
        quadro_do_jogo[2][1] = jogada

    elif posicao_jogada == 9 and quadro_do_jogo[2][2] != 'X' and quadro_do_jogo[2][2] != 'O':
        quadro_do_jogo[2][2] = jogada


# analisando se o tabuleiro está completo
def analisando_tabuleiro():
    """
    Função que analisa se todo o tabuleiro já foi preenchido por "x" ou "o".
    Se nenhuma das opções de vitórias foram alcançadas, este função retornando True, quer dizer empate.
    """
    cont = 0
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if quadro_do_jogo[linha][coluna] == 'X' or quadro_do_jogo[linha][coluna] == 'O':
                cont += 1
            
    # igual a 9 diz respeito se todas as casas foram preenchidas. Retornando True ou False
    if cont == 9:
        mensagem_final_jogo('EMPATE')
        return True
    else:
        return False


# printando mensagem do vencedor ou de empate.
def mensagem_final_jogo(jogador):
    """
    Printando mensagem final do jogo.
    """
    print('=' * 30)
    if jogador == 'X' or jogador == 'O':
        print(f'\033[35m{jogador} VENCEU!!!!!! FIM DE JOGO =D\033[m')
    else:
        print(f'\033[35m{jogador}, TODAS AS CASAS FORAM PREENCHIDAS, NENHUM VENCEDOR. FIM DE JOGO!!!\033[m')
    print('=' * 30)


# analisando status do jogo em si
def analisando_jogo(jogada):
    """
    VERIFICANDO FINAL DO JOGO
    GANHA QUEM COMPLETAR UMA RETA (LINHA OU COLUNA) COM 'X' OU 'O'
    OPÇÕES DE VITÓRIA NA MATRIZ:
        -> Verificando linhas
        - 1, 2, 3 == [0, 0], [0, 1], [0, 2]
        - 4, 5, 6 == [1, 0], [1, 1], [1, 2]
        - 7, 8, 9 == [2, 0], [2, 1], [2, 2]

        -> Verificando colunas
        - 1, 4, 7 == [0, 0], [1, 0], [2, 0]
        - 2, 5, 8 == [0, 1], [1, 1], [2, 1]
        - 3, 6, 9 == [0, 2], [1, 2], [2, 2]

        -> Verificando diagonais
        - 1, 5, 9 == [0, 0], [1, 1], [2, 2]
        - 3, 5, 7 == [0, 2], [1, 1], [2, 0]
    """

    # verificações de vitórias possíveis de "X" ou "O":
    if quadro_do_jogo[0][0] == jogada and quadro_do_jogo[0][1] == jogada and quadro_do_jogo[0][2] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[1][0] == jogada and quadro_do_jogo[1][1] == jogada and quadro_do_jogo[1][2] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[2][0] == jogada and quadro_do_jogo[2][1] == jogada and quadro_do_jogo[2][2] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[0][0] == jogada and quadro_do_jogo[1][0] == jogada and quadro_do_jogo[2][0] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[0][1] == jogada and quadro_do_jogo[1][1] == jogada and quadro_do_jogo[2][1] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[0][2] == jogada and quadro_do_jogo[1][2] == jogada and quadro_do_jogo[2][2] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[0][0] == jogada and quadro_do_jogo[1][1] == jogada and quadro_do_jogo[2][2] == jogada:
        mensagem_final_jogo(jogada)
        return True

    elif quadro_do_jogo[0][2] == jogada and quadro_do_jogo[1][1] == jogada and quadro_do_jogo[2][0] == jogada:
        mensagem_final_jogo(jogada)
        return True


# alimentando matriz e jogando o jogo
def inicio_jogo():
    """
    Função que inicializa o jogo chamando funções de:
        - imprimir o tabuleiro
        - já validando a posição de jogada (1 a 9) e a jogada ("x" ou "o")
        - chamando funções de analisando a jogada, o jogo e o tabuleiro
    """
    while True:
        imprime_tabuleiro()

        while True:
            # ANALISANDO JOGADA SOMENTE ENTRE 1 E 9
            try:
                posicao_jogada = int(input('\n \033[1;33mQuer jogar em qual posição?\033[m '))
                if posicao_jogada >= 1 and posicao_jogada <= 9:
                    break
                print(f'\033[1;31mOpção apenas entre 1 e 9!\033[m')
            except Exception as error:
                print(f'Erro: {error.__class__}, descrição: {error}.')

        while True:
            # ANALISANDO OPÇÃO SOMENTE "X" OU "O"
            try:
                jogada = str(input(' \033[1;33mX ou O?\033[m ')).strip().upper()[0]
                if jogada in 'XO':
                    break
                print(f'\033[1;31mEscolha somente "X" ou "O"!\033[m')
            except Exception as error:
                print(f'Erro: {error.__class__}, descrição: {error}.')

        
        # analisando se a jogada é possível
        analisando_jogada(posicao_jogada, jogada)

        # analisando se alguém ganhou
        if analisando_jogo(jogada):
            break

        #vendo se todas os valores da matriz foram preenchidos. Se for True, quer dizer empate
        elif analisando_tabuleiro():
            break
