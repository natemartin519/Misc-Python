from sys import argv

def load_player(file):
    player = file.readline().strip()
    return player


def load_game_board(file):
    board_rows = list(file.read().splitlines())
    game_board = []

    for row in board_rows:
        board_col = list(row.upper())
        game_board.append(board_col)

    return game_board


def did_player_win(game_board, player):
    # row and col check
    for i in range(0, 3):
        if game_board[i][0] == player and game_board[i][1] == player and game_board[i][2] == player:
            return True

        if game_board[0][i] == player and game_board[1][i] == player and game_board[2][i] == player:
            return True

    # diagnal chack
    if game_board[1][1] == player:
        if game_board[0][0] == player and game_board[2][2] == player:
            return True

        if game_board[0][2] == player and game_board[2][0] == player:
            return True

    return False


def find_winning_move(game_board, player):
    for x in range(0, 3):
        for y in range(0, 3):
            if game_board[x][y] == '-':
                game_board[x][y] = player

                if did_player_win(game_board, player):
                    return True

                game_board[x][y] = '-'

    return False


def display_game_board(game_board):
    print ('\n'.join([''.join([square for square in row]) for row in game_board]))



script, filename = argv
current_file = open(filename)

player = load_player(current_file)
game_board = load_game_board(current_file)

if find_winning_move(game_board, player):
    display_game_board(game_board)
else:
    print ('No Winning Move!')