from copy import deepcopy


def is_win(board, player):
    # Verificando as Linhas do Tabuleiro
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # Verificando as Colunas do Tabuleiro
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # Verificando as Diagonais do Tabuleiro
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    return False


def esta_vazio(board): #esta vazio (empate)
    for line in board:
        if ' ' in line:
            return False

    return True


def esta_terminado(board): #(jogo_finalizado)
    if is_win(board, CPU_PLAYER) or is_win(board, HUMAN_PLAYER) or esta_vazio(board):
        return True

    return False


def print_board(board):
    print('\n')

    for i, line in enumerate(board):
        print(*line, sep=' | ')

        if i != len(line) - 1:
            print('--+---+--')

    print('\n')


def candidates(board, player):
    candidate_moves = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ' ':
                continue

            candidate = deepcopy(board)
            candidate[i][j] = player

            candidate_moves.append(candidate)

    return candidate_moves


def resultado(board): #+1 = vitoria / -1 = derrota / 0 = empate
    if is_win(board, CPU_PLAYER):
        return 1

    if is_win(board, HUMAN_PLAYER):
        return -1

    return 0


def minimax(board, maximizing=False):
    if esta_terminado(board): #se está finalizaod
        return resultado(board)

    if maximizing:
        value = float('-inf')

        for child in candidates(board, CPU_PLAYER):
            value = max(value, minimax(child, False))
    else:
        value = float('+inf')

        for child in candidates(board, HUMAN_PLAYER):
            value = min(value, minimax(child, True))

    return value


if __name__ == '__main__':
    CPU_PLAYER = 'X'
    HUMAN_PLAYER = 'O'

    human_play_first = input('Você deseja começar o jogo [s|n]: ') == 's'

    if human_play_first:
        HUMAN_PLAYER = 'X'
        CPU_PLAYER = 'O'

    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    while not esta_terminado(board):
        if human_play_first:
            print_board(board)

            position = int(input('Insira a posição da jogada [1-9]: '))

            i = (position - 1) // 3
            j = (position - 1) % 3

            board[i][j] = HUMAN_PLAYER

            if esta_terminado(board):
                break

        candidate_moves = candidates(board, CPU_PLAYER)
        board = max(candidate_moves, key=minimax)
        human_play_first = True

    print_board(board)

    if is_win(board, HUMAN_PLAYER):
        print('Você venceu!!')
    elif is_win(board, CPU_PLAYER):
        print('Você perdeu!!')
    else:
        print('Deu Empate!!')
