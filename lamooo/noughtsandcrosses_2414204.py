import random
import os.path
import json
random.seed()

def draw_board(board):
    print('-----------')
    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + '|') #Row 1
    print('-----------')
    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + '|') #Row 2
    print('-----------')
    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + '|') #Row 3
    print('-----------')

def welcome(board):
    print("Welcome to a simple tic tac toe game in python \n The board layout is shown below:")
    draw_board(board) #Calling the function.
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

def get_player_move(board):
    while True:
        pm= input(" 1 2 3 \n 4 5 6 \n 7 8 9 \n choose your square:")
        if pm in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pm = int(pm) - 1
            if board[int(pm / 3)][pm % 3] == ' ':
                return int(pm / 3), pm % 3
            else:
                print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return i, j


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
            (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
            (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
            (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    initialise_board(board)
    while True:
        pm = get_player_move(board)
        if pm != None:
            board[pm[0]][pm[1]] = "X"
            draw_board(board)
            if check_for_win(board, "X"):
                return 1
            elif check_for_draw(board):
                return 0
            cm = choose_computer_move(board)
            board[cm[0]][cm[1]] = "O"
            print("Computer made a choice")
            draw_board(board)
            if check_for_win(board, "O"):
                return -1
            elif check_for_draw(board):
                return 0
            else:
                continue


def menu():
        choice = input(
            "1. Play game\n2. Save score\n3. Leaderboard \n4. Quit\nEnter your choice: ")
        # check if choice is a valid data which is (1 to play game, 2, 3, 4);
        if choice in ['1', '2', '3', '4']:
            # if choice is valid it is returned.
            return choice
        else:
            # if choice is not valid loop run continuously.
            print("Invalid input. Please enter a valid choice.")

def load_scores():
    """
    Loads the leaderboard from a .txt file and returns it as a dictionary
    """
    try:
        # open the file in read mode
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    except:
        # if the file doesn't exist, create a new dictionary
        leaderboard = {}

    return leaderboard

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name: ")
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except:
        data = {}
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)



def display_leaderboard(leaders):
    # develop code to display the leaderboard scores-++++
    # passed in the Python dictionary parameter leader
    print("Name: Score")
    for name, score in leaders.items():
        print(f"{name}: {score}")