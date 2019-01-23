import random

#method to choose random item
def choose_item():
    items_list = ['Rock', 'Paper', 'Scissors']
    return random.choice(items_list)

#method to format user response or pick random item
def player_item(string):
    if string.upper() == 'ROCK':
        return 'Rock'
    elif string.upper() == 'PAPER':
        return 'Paper'
    elif string.upper() == 'SCISSORS':
        return 'Scissors'
    elif string.upper() == 'RANDOM':
        item = choose_item()
        return item

#method to figure out who won
def who_won(computer_item, user_item):
    if computer_item == user_item:
        print('Tie game!')
    elif computer_item == 'Rock' and user_item == 'Paper':
        print('You win! Paper covers Rock.')
    elif computer_item == 'Rock' and user_item == 'Scissors':
        print('You lose! Rock smashes Scissors.')
    elif computer_item == 'Paper' and user_item == 'Rock':
        print('You lose! Paper covers Rock.')
    elif computer_item == 'Paper' and user_item == 'Scissors':
        print('You win! Scissors cut Paper.')
    elif computer_item == 'Scissors' and user_item == 'Rock':
        print('You win! Rock smashes Scissors.')
    elif computer_item == 'Scissors' and user_item == 'Paper':
        print('You lose! Scissors cut Paper.')
    else:
        print('What is going on!?')

#main method
def main():
    play_again = 'Y'
    while play_again.upper() == 'Y':
        #get computer item
        computer_item = choose_item()
        #get user input
        user_input = input('Do you want rock, paper, scissors, or random? ')
        user_item = player_item(user_input)
        #print(computer_item, user_item)
        #figure out who won
        who_won(computer_item, user_item)
        #ask user if they want to play again
        play_again = input('Do you want to play again? (y or n) ')

    #thank player for playing
    print('Thanks for playing!')

main()