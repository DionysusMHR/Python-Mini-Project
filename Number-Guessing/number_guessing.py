import random


n = random.randint(1,100)

cnt = 0
while cnt < 7:
    g = int(input("Enter your guess:"))
    if g == n:
        break
    elif g > n:
        print("Too High")
        cnt += 1
    else:
        print("Too Low")
        cnt += 1

if cnt < 7:
    print("You Won")
else:
    print("You Lose")
