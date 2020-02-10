"""
DOCUMENTATION:
PYTHON SCRIPT FOR TIC-TAC-TOE GAME
It has all the required validations for the programme
"""
# OS library is used to clear the console after every input
import os


def valid_choice(choices_already_marked, index):
    """
    Function used to check the valid choice!!
    Choice should be a valid number between 1-9 and should not have been used earlier.
    :param choices_already_marked: list of choices already marked
    :param index: choice made by the user
    :return: boolean after validation
    """
    if index in choices_already_marked:
        print("Already marked! Enter other choice: ")
        return False
    elif index in list(range(1, 10)):
        return True
    else:
        print("Invalid choice!! Enter number between 1-9 : ")
        return False

def choice(arr, symbol_p1, symbol_p2):
    """
    Main logic function where the choices are entered
    :param arr: list of 9 elements
    :param symbol_p1: symbol for Player 1
    :param symbol_p2: symbol for player 2
    :return: nothing
    """
    turn = 1
    result = False
    choices_already_marked = []

    while turn < 10:
        # maximum turns can be 10 but program can end before also
        clear = lambda: os.system('clear')  # to clear the screen
        clear()

        print('Player 1 symbol: {}'.format(symbol_p1))
        print('Player 2 symbol: {}'.format(symbol_p2))

        print_table(arr)

        if turn % 2 != 0:
            print("Player 1 turn: ")
        else:
            print("Player 2 turn: ")

        symbol_choice = ''

        if turn % 2 != 0:
            symbol_choice = symbol_p1
        else:
            symbol_choice = symbol_p2

        # index validation logic

        while True:
            flag = False
            try:
                index = int(input('Enter choice between 1-9 : '))
                flag = valid_choice(choices_already_marked, index)
                choices_already_marked.append(index)
                # print(choices_already_marked)
            except:
                print('Enter valid choice between 1-9: ')

            if flag == True:
                break
            else:
                continue

        mark_choice(arr, index, symbol_choice)
        turn = turn + 1

        result = check_result(arr, symbol_choice)
        if result == True:
            print("Result found")

            break;
        else:
            continue


def check_result(arr, symbol_choice):
    if (arr[0] == arr[1] == arr[2] == symbol_choice) \
            or (arr[3] == arr[4] == arr[5] == symbol_choice) \
            or (arr[6] == arr[7] == arr[8] == symbol_choice) \
            or (arr[0] == arr[3] == arr[6] == symbol_choice) \
            or (arr[1] == arr[4] == arr[7] == symbol_choice) \
            or (arr[2] == arr[5] == arr[8] == symbol_choice) \
            or (arr[2] == arr[4] == arr[6] == symbol_choice) \
            or (arr[0] == arr[4] == arr[8] == symbol_choice):
        clear = lambda: os.system('clear')  # on Linux System
        clear()

        print("{} WON!!".format(symbol_choice))
        print_table(arr)

        return True


def mark_choice(arr, index, symbol):
    arr[index - 1] = symbol


def check_symbol(symbol):
    if symbol == 'X' or symbol == 'x' or symbol == '0':
        return True
    else:
        return False


def menu():
    clear = lambda: os.system('clear')  # on Linux System
    clear()

    print("WELCOME!!! TO TIC-TAC-TOE")
    flag = True

    while flag == True:
        symbol_p1 = input("PLAYER 1- CHOOSE YOUR SYMBOL- X OR 0 ?")
        if check_symbol(symbol_p1):
            print('PLAYER 1 symbol is ' + symbol_p1)
            flag = False
        else:
            continue

    if symbol_p1 == 'x' or symbol_p1 == 'X':
        symbol_p2 = '0'

    elif symbol_p1 == '0':
        symbol_p2 = 'X'

    print('PLAYER 2 symbol is ' + symbol_p2)

    choice(arr, symbol_p1, symbol_p2)


def print_table(arr):
    print(str(arr[0]) + '  | ' + str(arr[1]) + '  | ' + str(arr[2]))
    print('--- --- ---')
    print(str(arr[3]) + '  | ' + str(arr[4]) + '  | ' + str(arr[5]))
    print('--- --- ---')
    print(str(arr[6]) + '  | ' + str(arr[7]) + '  | ' + str(arr[8]))


# global variables
symbol_p1 = ''
symbol_p2 = ''

arr = list(range(1, 10))
menu()
