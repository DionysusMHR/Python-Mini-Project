import random

def check(word, guess, show):
    show = list(show)
    for i in range(min(len(word), len(guess))):
        if word[i] == guess[i]:
            show[i] = guess[i]
    return ''.join(show)    


words_list = [
    'anime', 'computer', 'science', 'programing',
    'python', 'mathematics', 'game', 'philosophy',
    'hack', 'geek', 'stars', 'art', 'strawhat', 'linux',
    'history', 'music', 'cosmos', 'logic', 'sport',
    'problem', 'ai']

cnt_guessing = 5
word = random.choice(words_list)
show = '_' * len(word)

cnt = 0
while cnt < cnt_guessing:
    print(f'word : {show}')
    guess = input("Enter your guess:")
    cnt += 1
    show = check(word, guess, show)
    
    if guess == word:
        print("You Won")
        break
    if cnt == cnt_guessing:
        print("You Lose")
        break
