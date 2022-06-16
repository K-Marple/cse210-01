'''
Tic-Tac-Toe Game
By: Kayli Marple
'''

def main():
    # start the game with player x and make the board
    player = switch_player("")
    board = make_board()
    # continuously show the board while adding new moves made until there is a winner or a draw
    while not (winner(player, board) or draw(board)):
        show_board(board)
        moves(player, board)
        player = switch_player(player)
    show_board(board)


def make_board():
    # make a 2-D array
    board = []
    for move in range(9):
        board.append(move + 1)
    return board


def show_board(board):
    # print the board with bars and dashes to separate the slots
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def switch_player(current):
    # check who the current player is and switch to the other player
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


def moves(player, board):
    # ask the player what their move is and mark it on the board
    move = int(input(f"{player}'s turn. Enter number for desired square: "))
    board[move - 1] = player


def winner(player, board):
    # check if there is three in a row on the board and print the winner
    if player == "x":
        print("Congradulations! Player o won!")
    elif player == "o":
        print("Congradulations! Player x won!")
    return (board[0] == board[1] == board[2] or 
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw(board):
    # check if there is a draw and print related message
    for spot in range(9):
        if board[spot] != "x" and board[spot] != "o":
            return False
    print("Game Over... It's a draw.")
    return True


if __name__ == "__main__":
    main()