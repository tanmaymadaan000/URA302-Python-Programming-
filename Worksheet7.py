def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_winner(board, player):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False

def check_tie(board):
    return " " not in board

def get_player_input(player, board):
    while True:
        move = input("Player " + player + ", choose position (1-9): ")
        if not move.isdigit():
            print("Enter a number between 1 and 9.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Number must be between 1 and 9.")
            continue
        if board[move - 1] != " ":
            print("That spot is already taken.")
            continue
        return move - 1

def play_game():
    while True:
        board = [" "] * 9
        current_player = "X"
        while True:
            print_board(board)
            move = get_player_input(current_player, board)
            board[move] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print("Player " + current_player + " wins!")
                break
            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

play_game()
