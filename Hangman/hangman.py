import random

def check(fruit, show, guess):
    show = list(show)
    for i in range(min(len(fruit), len(guess))):
        if guess[i] == fruit[i] and show[i] == '_':
            show[i] = guess[i]
    return ''.join(show)


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'lemon',
          'mango', 'orange', 'peach', 'watermelon', 'melon']

fruit = random.choice(fruits)
show = fruit[0] + (len(fruit)-2)*'_' + fruit[-1]
cnt_guess = 5
cnt = 0
while cnt < cnt_guess:
    print(show)
    guess = input("Enter your guess: ")
    cnt += 1
    show = check(fruit, show, guess)
    if show == guess:
        print('You Won')
        break
    if cnt == cnt_guess:
        print('You Lose')
        break
