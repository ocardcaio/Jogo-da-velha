tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def exibir_tabuleiro(tabuleiro):
    print(' ' + tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('---+---+---')
    print(' ' + tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('---+---+---')
    print(' ' + tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8])

def verificar_vencedor(tabuleiro, jogador):
    comb_ganhadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]  # diagonais
    ]
    for comb in comb_ganhadoras:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

def jogada_jogador(tabuleiro):
    while True:
        jogada = input('Digite a posição para jogar (1-9): ')
        if jogada.isdigit():
            jogada = int(jogada) - 1
            if 0 <= jogada < 9 and tabuleiro[jogada] == ' ':
                return jogada
        print('Jogada inválida. Tente novamente.')

def jogada_ia(tabuleiro):
    for i in range(9):
        if tabuleiro[i] == ' ':
            return i

def jogar():
    tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogador_atual == 'X':
            jogada = jogada_jogador(tabuleiro)
        else:
            jogada = jogada_ia(tabuleiro)

        tabuleiro[jogada] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print('O jogador', jogador_atual, 'venceu!')
            break

        if ' ' not in tabuleiro:
            exibir_tabuleiro(tabuleiro)
            print('Empate!')
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar()

