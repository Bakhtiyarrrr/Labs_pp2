import random
random_number = int(random.choice(range(1,21)))
print("Hello, What is your name?")
x = input()
print()
print(f"Well, {x}, I am thinking of a number between 1 and 20.")
counter = 0
print("Take a guess.")
n = 0
while True:
    counter += 1
    n = int(input())
    print()
    if n == random_number:
        print(f"Good job, {x}! You guessed my number in {counter} guesses!")
        break
    else:
        print("Your guess is too low.")
        print("Take a guess.")
