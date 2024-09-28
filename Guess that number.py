import random

computer_random = random.randint(1,100)

while True:
    player_input = input('Guess the Number (1-100): ')
    if not player_input.isdigit():
        print('Invalid')
        continue
    g = int(player_input)
    if g == computer_random:
        print('You guess it')
        break
    elif g > computer_random:
        print('Too high')
    else:
        print('Too low')
