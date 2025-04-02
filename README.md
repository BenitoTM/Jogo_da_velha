# Jogo da Velha

## Descrição
Este é um simples jogo da velha (tic-tac-toe) implementado em Python. O jogo pode ser jogado no terminal e permite que dois jogadores se enfrentem alternando suas jogadas.

## Tecnologias Utilizadas
- Python 3

## Como Executar

1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Clone este repositório:
   ```sh
   git clone https://github.com/BenitoTM/Jogo_da_velha.git
   ```
3. Navegue até o diretório do projeto:
   ```sh
   cd Jogo_da_velha
   ```
4. Execute o script principal:
   ```sh
   python jogo_da_velha.py
   ```

## Como Jogar
- O jogo é para dois jogadores.
- O tabuleiro é representado por uma grade 3x3.
- Cada jogador faz uma jogada por vez, escolhendo uma posição vazia para colocar seu símbolo ('X' ou 'O').
- O jogo termina quando um jogador completa uma linha, coluna ou diagonal com seu símbolo, ou quando todas as casas estão preenchidas (empate).

## Exemplo de Execução
```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Jogador X, escolha um número: 5

 1 | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 

Jogador O, escolha um número: 1

 O | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 
```

## Melhorias Futuras
- Implementar uma interface gráfica.
- Adicionar modo contra IA.
- Melhorar a validação de entrada do usuário.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
