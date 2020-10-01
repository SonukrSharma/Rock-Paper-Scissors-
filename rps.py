from random import *
#Just basic programme { no gui:( }

print("Welcome to the Rock Paper Scissors game")
p = input("Enter your Name: ")
c = input("Enter your Favourite Character Name: ")
print(p + " you are going to face the biggest challenge of your life . "
          "You are up against " + c + " who has challenged you in a Rock Paper Scissors game.")
print("You better win to show how cool you are. ")

print(" For Rock enter 1")
print("For Paper enter 2")
print("For Scissor enter 3")
game = True
pc = 0
uc = 0
while game:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("You choose Rock ")
    elif ch == 2:
        print("You choose Paper ")
    elif ch == 3:
        print("You choose Scissor ")
    else:
        print("Invalid Input!!!")
        break

    u = randint(1, 3)
    if u == 1:
        print(c + " choose Rock .")
    elif u == 2:
        print(c + " choose Paper .")
    else:
        print(c + " choose Scissors .")

#satyajit was here
#hello

    if ch == u:
        print("Its a draw!!!")
    elif (ch == 1 and u == 3) or (ch == 2 and u == 1) or (ch == 3 and u == 2):
        print("You Win!!!")
        pc += 1
    else:
        print("You Lose!!!")
        uc += 1
    f = int(input("If you wish to play again enter any number or for exit enter 0"))
    if f == 0:
        game = False

print("Thank You")
print("Final score against " + c + " in the battle of Rock paper Scissors: ")
print(p + " = " + str(pc))
print(c + " = " + str(uc))
if pc > uc:
    print("You Won!!")
elif pc == uc:
    print("You nearly beat " + c + " .It was a Draw . Good Game. ")
else:
    print("You Lose!!")
