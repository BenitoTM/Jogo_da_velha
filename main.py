from copy import deepcopy
from time import sleep


def mostra_tabuleiro(tabuleiro):
    print("   a   b   c")
    print("--------------") # Marca uma divisão entre telas para controle visual
    id_linha = 1
    for linha in tabuleiro:

        print(f"{id_linha}|", linha[0], "|", linha[1], "|", linha[2], "|")

        print("--------------") # Marca uma divisão entre telas para controle visual
        id_linha+=1
def verifica_vitoria(tabuleiro, jogador):

    # Vamos verificar possibilidade de vitória por sequência horizontal
    for i in range(0,3):

        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:

            return True

    # Vamos verificar possibilidade de vitória por sequência vertical
    for i in range(0,3):

        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:

            return True

    # Vamos verificar possibilidade de vitória na diagonal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:

        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:

        return True

    return False

def jogo_finalizado(tabuleiro) -> bool:
    if verifica_vitoria(tabuleiro, "X") or verifica_vitoria(tabuleiro, "O") or empate(tabuleiro):
        return True
    else: return False

def empate(tabuleiro) -> bool:
    # se ainda houver possiveis jogadas, retornara False
    # se o jogo ja tiver finalizado, retornara True
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def avaliar(tabuleiro) -> int:
    #funcao para avaliar o resultado
    #-1 = derrota | 0 = empate | 1 = vitoria
    if verifica_vitoria(tabuleiro, "O"):
        return 1
    elif verifica_vitoria(tabuleiro, "X"):
        return -1
    return 0

def minimax(tabuleiro, maximizacao=False):
    #maximizacao: para alterar entre o bot e o humano
    #na simulacao do bot, ele deve ganhar, do humano, perder

    if jogo_finalizado(tabuleiro):
        return avaliar(tabuleiro)

    if maximizacao:
        value = float('-inf')

        for jogada in jogada_bot(tabuleiro, "O"):
            value = max(value, minimax(jogada, False))
    else:
        value = float('+inf')

        for jogada in jogada_bot(tabuleiro, "X"):
            value = min(value, minimax(jogada, True))

    return value

def jogada_bot(tabuleiro, jogador): #funcao foi substituida
    possibilidades = []
    for x in range(0,3):
      for y in range(0,3):
          if tabuleiro[x][y] == " ":
              jogada = deepcopy(tabuleiro)
              jogada[x][y] = jogador
              possibilidades.append(jogada)
    return possibilidades

def start_jogo():

    # Criação da lista que gera o tabuleiro
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    # Jogadores existentes
    jogadores = ["X","O"]

    # Define o marcador que inicia o jogo
    jogador_atual = jogadores[0]

    # Printa o tabuleiro na tela
    mostra_tabuleiro(tabuleiro)

    # Definindo o posicionamento dos marcadores
    for i in range(1,10):
        if jogador_atual == "X":
            linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
            coluna = str(input(f"Jogador {jogador_atual} escolha uma coluna a b c: "))
            coluna = ord(coluna.lower()) - 97 #na tabela ascii, a = 97, b=98, c = 99.

            # Verificando se a posicao escolhida e valida
            if tabuleiro[linha][coluna] != " ":

                print("Posição ocupada.\nEscolha outra opção.")
                linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
                coluna = str(input(f"Jogador {jogador_atual} escolha uma coluna a b c: "))
                coluna = ord(coluna.lower()) - 97

            tabuleiro[linha][coluna] = jogador_atual
            mostra_tabuleiro(tabuleiro)

            if jogo_finalizado(tabuleiro):
                break

        jogador_atual = jogadores[i % 2] #mudanca de jogador

        if jogador_atual == "O": #se for o bot
            #chama funcao minimax, que retorna a posicao que ele jogara
            possiveis_jogadas = jogada_bot(tabuleiro, "O")
            tabuleiro = max(possiveis_jogadas, key=minimax)
            sleep(1)
            mostra_tabuleiro(tabuleiro)

            if jogo_finalizado(tabuleiro):
                break

    if verifica_vitoria(tabuleiro, jogador_atual):
        avaliar(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!!!")
        return

    # Caso nenhuma das condições de vitória sejam encontradas, devemos considerar o resultado de empate
    if empate(tabuleiro):
        print("O jogo terminou empatado.")
        avaliar(tabuleiro)

start_jogo()