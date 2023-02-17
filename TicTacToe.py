def board_game(board):
    blank_board = """
 _______________________
|       |       |       |    
|   7   |   8   |   9   |
|_______|_______|_______|
|       |       |       |
|   4   |   5   |   6   |
|_______|_______|_______|
|       |       |       |
|   1   |   2   |   3   |
|_______|_______|_______|
"""
    for i in range(1,10):
        if (board[i]=='O' or board[i]=='X'):
            blank_board = blank_board.replace(str(i), board[i])
        else:
            blank_board = blank_board.replace(str(i), ' ')
    print(blank_board)

def input_player():
    player_1 = input("Choose 'X' or 'O': ")
    while True:
        if player_1.upper() == 'X':
            player_2 = 'O'
            print("You choosen "+player_1+" so second player play "+player_2)
            return player_1.upper(),player_2
        elif player_1.upper() == 'O':
            player_2 = 'X'
            print("You choosen "+player_1+" so second player play "+player_2)
            return player_1.upper(),player_2
        else:
            player_1 = input("Choose 'X' or 'O': ")
            
def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board,position):
    return board[position] == '#'

def board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board,marker):
    if board[1] == board[2] == board[3] == marker:
        return True
    if board[4] == board[5] == board[6] == marker:
        return True
    if board[7] == board[8] == board[9] == marker:
        return True
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    if board[3] == board[6] == board[9] == marker:
        return True
    if board[1] == board[5] == board[9] == marker:
        return True
    if board[3] == board[5] == board[7] == marker:
        return True
    return False

def choice_player(board):
    choice = input("Choice empty place between 1 and 9: ")
    while not space_check(board, int(choice)):
        choice = input("This place isn't empty, please choose free place between 1 and 9: ")
    return choice

def again():
    again_play = input("Do you want to play again? ('y'/'n') ")
    if again_play.lower() == 'y':
        return True
    if again_play == 'n':
        return False
    

if __name__ == "__main__":
    print("Welcome to TICTACTOE GAME!")
    i = 1
    players = input_player()
    board = ['#']*10
    while True:
        game_on = board_check(board)
        while not game_on:
            
            position = choice_player(board)
            
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
                
            place_marker(board, marker, int(position))
            
            board_game(board)
            i += 1
            if win_check(board, marker):
                print("You WIN!")
                break
            game_on = board_check(board)
        if not again():
            break
        else:
            i = 1
            players = input_player()
            board = ['#']*10
    