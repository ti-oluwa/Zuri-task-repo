import random

msg1 = 'CONGRATS YOU WIN!'

msg2 = 'CPU WON, YOU LOST! TRY AGAIN'
moves = {
    'R': "Rock",
    'P': "Paper",
    'S': "Scissors",
    }


def decision(user_choice, computer_choice):
    plays = [user_choice, computer_choice]
    if plays[0] == plays[1]:
        print_moves(user_choice, computer_choice)
        print('A TIE!')
        print('\n')
        play_again()

    elif plays[0] == 'R' and plays[1] == 'S':
        print_moves(user_choice, computer_choice)
        print(msg1)

    elif plays[1] == 'R' and plays[0] == 'S':
        print_moves(user_choice, computer_choice)
        print(msg2)

    elif plays[0] == 'P' and plays[1] == 'R':
        print_moves(user_choice, computer_choice)
        print(msg1)

    elif plays[1] == 'P' and plays[0] == 'R':
        print_moves(user_choice, computer_choice)
        print(msg2)

    elif plays[0] == 'S' and plays[1] == 'P':
        print_moves(user_choice, computer_choice)
        print(msg1)

    elif plays[1] == 'S' and plays[0] == 'P':
        print_moves(user_choice, computer_choice)
        print(msg2)


def print_moves(users_move, computers_move):
    x = moves[users_move]
    y = moves[computers_move]
    print(f"Player({x}) : CPU({y})")


def game():
    print('This is a game of rock, paper, scissors')
    print("Enter:")
    print('R for rock', 'P for paper', 'S for scissors', sep="\n")
    options = ['R', 'P', 'S']
    user_choice = str(input('Make your choice: \n')).upper()
    computer_choice = random.choice(options)

    is_valid = False
    x = 0
    for items in options:
        if user_choice == items:
            is_valid = True
            decision(user_choice, computer_choice)
            break

        elif user_choice != items:
            is_valid = False
            x += 1

        elif x == len(options):
            break

    if is_valid is False:
        print('WRONG ENTRY!\n')
        game()


def play_again():
    ans = ['yes', 'no']
    response = input("Would you like to play again?(Yes or No) ")
    if response.lower() in ans:
        game()

    else:
        print('Invalid Response!')
        play_again()


game()


