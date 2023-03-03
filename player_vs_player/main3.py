def display(values):
    print(f"{values[0]:5} | {values[1]:>5}    | {values[2]:>5}")
    print('-------------------------')
    print(f"{values[3]:5} | {values[4]:>5}    | {values[5]:>5}")
    print('-------------------------')
    print(f"{values[6]:5} | {values[7]:>5}    | {values[8]:>5}")


def print_score_board(score_board):
    print("\t-------------------------------------------")
    print("\t          SCOREBOARD FOR TIC TAC TOE       ")
    print("\t-------------------------------------------")


    players = list(score_board.keys())
    print("\t    ", players[0], "\t  ", score_board[players[0]])
    print("\t    ", players[1], "\t  ", score_board[players[1]])

    print("\t-------------------------------------------")


def check_winner(player_position, current_player):
        
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [1, 4, 7], [2, 5, 8], [3, 6, 9],
                [1, 5, 9], [3, 5, 7]]
    
    for x in solution:
        if all(y in player_position[current_player] for y in x): 
            return True
    return False
    
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

def single_game(current_player):
    values = [' ' for x in range(9)]

    player_position = {'X': [], 'O': []}

    while True:
        display(values)

        try:
            print('Player ', current_player, " turn. Which Box? : ", end="")
            move = int(input())
        except ValueError:
            print("Invalid Input")
            continue

        if move < 1 or move > 9:
            print("Please choose the right number between 1 to 9")
            continue


        if values[move-1] != ' ':
            print("The place you have choosen ia already filled Try another position")
            continue

        values[move-1] = current_player

        player_position[current_player].append(move)

        if check_winner(player_position, current_player):
            display(values)
            print("Player ", current_player, " has won the game!!")
            print("\n")
            return current_player
        
        if check_draw(player_position):
            display(values)
            print("Game is a draw")
            print("\n")
            return 'D'
        
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == "__main__":

    print('Player One Details ')
    player1 = input("Enter your name: ")
    print("\n")

    print("Player Two Details")
    player2 = input("Enter your name: ")
    print("\n")
    
    current_player = player1

    player_choice = {'X' : "", 'O' : ""}

    options = ['X', 'O']

    score_board = {player1: 0, player2: 0}
    print_score_board(score_board)

    while True:
        print("Turn to choose for ", current_player)
        print("Enter 1 to choose X")
        print("Enter 2 to choose O")
        print("Enter 3 to Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Please enter an integer among 1 or 2 or 3")
            continue

        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            print_score_board(score_board)
            break

        else:
            print("Number should be 1 or 2 or 3")
            continue


        winner = single_game(options[choice-1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_score_board(score_board)
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
