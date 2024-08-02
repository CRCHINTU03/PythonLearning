import random


def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input("Enter a number: "))
        if guess < randomNumber:
            print("It's is not the correct guess . you choice is TOO LOW")
        elif guess > randomNumber:
            print("It's is not a correct choice . you're choice is TOO High")
    
    print(f"you choice is correct as guess number is equal to {randomNumber}")


guess(100)
