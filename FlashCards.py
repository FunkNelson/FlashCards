import random
import os

cardStack = {
    'Golden Signals': 'Latency, Traffic, Error Rates, Saturation',
    'Latency': 'Time it takes for a request to travel from the client to the server and back'
}


keys_list = list(cardStack.keys())
random_card = random.choice(keys_list)

terminal_width = os.get_terminal_size().columns


def displayCard(card):
    print('\n')
    print(f" ------------------------------------------------- ".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(card.center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f"|                                                 |".center(terminal_width))
    print(f" ------------------------------------------------- ".center(terminal_width))
    print('\n')
    input('Press Enter to flip the card'.center(terminal_width))


def printAnswer(card):
    print('\n')
    print(cardStack[card])
    print('\n')


displayCard(random_card)
printAnswer(random_card)
