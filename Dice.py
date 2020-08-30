import random

val = int(input("Welcome players!\nWhat do you want to toss today:\n1. Dice\n2. Coin\n"))
if val == 1:
    print("You have chosen to roll a Dice, type any letter and enter when you want to stop.")
else:
    print("You have chosen to roll a Coin, type type any letter and enter when you want to stop.")
print("Press enter to gain the next value.")
loop = True
x = random.randint(1, 6)
num = 1
ran = ''
while loop:
    if val == 1:
        print(" " * len(str(num)) + "    -----")
        print(f"[{num}]: | {x} |")
        print(" " * len(str(num)) + "    -----")
    else:
        if x % 2 == 1:
            print(f"[{num}]: Heads")
        else:
            print(f"[{num}]: Tails")
    num += 1
    x = random.randint(1, 6)
    ran = input()
    if ran != '':
        break
print("Have a nice day!!!")