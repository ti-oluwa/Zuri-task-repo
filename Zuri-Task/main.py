import random

msg1 = 'CONGRATS YOU WIN!'

msg2 = 'YOU LOSE! TRY AGAIN'


def decision(user, computer):
    plays = [user.upper(), computer]

    if plays[0] == plays[1]:
        print('A TIE!')
        print('\n')
        play_again()

    elif plays[0] == 'R' and plays[1] == 'S':
        print(msg1)

    elif plays[1] == 'R' and plays[0] == 'S':
        print(msg2)

    elif plays[0] == 'P' and plays[1] == 'R':
        print(msg1)

    elif plays[1] == 'P' and plays[0] == 'R':
        print(msg2)

    elif plays[0] == 'S' and plays[1] == 'P':
        print(msg1)

    elif plays[1] == 'S' and plays[0] == 'P':
        print(msg2)


def game():
    print('This is a game of rock, paper, scissors')
    print("Enter:")
    print('R for rock', 'P for paper', 'S for scissors', sep="\n")
    options = ['R', 'P', 'S']
    user_choice = str(input('Make your choice: \n'))
    computer_choice = random.choice(options)
    is_valid = False

    while is_valid is False:
        for items in options:
            if user_choice == items:
                is_valid = True



    if is_valid is True:
        decision(user_choice.upper(), computer_choice)

    else:
        print('Wrong entry!\n')
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


