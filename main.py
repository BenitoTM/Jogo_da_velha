import time
def mostra_tabuleiro(tabuleiro):

    print("-------------") # Marca uma divisão entre telas para controle visual

    for linha in tabuleiro:

        print("|", linha[0], "|", linha[1], "|", linha[2], "|")

        print("-------------") # Marca uma divisão entre telas para controle visual

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


def jogada_bot(tabuleiro): #funcao foi substituida
  for coluna in range(0,3):
    for linha in range(0,3):
      if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = "O"
        time.sleep(1)
        mostra_tabuleiro(tabuleiro)
        if verifica_vitoria(tabuleiro, "O"):
            print(f"Jogador O venceu!!!")
            return
        return tabuleiro

def preencher_posicao(tabuleiro, linha, coluna, jogador):
  tabuleiro[linha][coluna] = "O"
  time.sleep(1)
  mostra_tabuleiro(tabuleiro)
  if verifica_vitoria(tabuleiro, "O"):
    print(f"Jogador O venceu!!!")
  return tabuleiro

def jogada_bot_melhor(tabuleiro):
  for coluna in range(0,3):
    for linha in range(0,3):

      if tabuleiro[linha][coluna] == "O":
        if tabuleiro[linha][coluna + 1 if coluna < 2 else 0] == " " or tabuleiro[linha][coluna + 1 if coluna < 2 else 0] == " ":
          if tabuleiro[linha][coluna - 1 if coluna > 0 else 2] ==  " " or tabuleiro[linha][coluna - 1 if coluna > 0 else 2] == "O":
            if tabuleiro[linha][coluna + 1 if coluna < 2 else 0] == " ":
              return preencher_posicao(tabuleiro, linha, coluna + 1 if coluna < 2 else 0, "O")
            else:
              return preencher_posicao(tabuleiro,linha, coluna - 1 if coluna > 0 else 2, "O")

      if tabuleiro[linha][coluna] == " ":


        return preencher_posicao(tabuleiro, linha, coluna, "O")

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
        if jogador_atual == "O":
            tabuleiro = jogada_bot_melhor(tabuleiro)#jogada_bot(tabuleiro)
            jogador_atual = jogadores[i % 2]
            continue
        linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
        coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna 1 - 3: ")) - 1

        # Verificando se a posicao escolhida e valida
        if tabuleiro[linha][coluna] != " ":

            print("Posição ocupada.\nEscolha outra opção.")
            linha = int(input(f"Jogador {jogador_atual} escolha uma linha 1 - 3: ")) - 1
            coluna = int(input(f"Jogador {jogador_atual} escolha uma coluna 1 - 3: ")) - 1

        tabuleiro[linha][coluna] = jogador_atual
        mostra_tabuleiro(tabuleiro)

        if verifica_vitoria(tabuleiro, jogador_atual):

            print(f"Jogador {jogador_atual} venceu!!!")
            return

        # Precisamos alterar entre os jogadores
        jogador_atual = jogadores[i % 2]

    # Caso nenhuma das condições de vitória sejam encontradas, devemos considerar o resultado de empate
    print("O jogo terminou empatado.")


start_jogo()