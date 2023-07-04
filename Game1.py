import random

i = 1
c = 0
p = 0
while(i<=10):
    lst  = ["Snake","Water","Gun"]
    cmp = random.choice(lst)

    n = input("Select from Snake,Water and Gun: \n")
    plyer = n.capitalize()
    if plyer == "Snake":
        if cmp==plyer:
            print("Its a draw")
        elif cmp == "Water":
            print("Player wins")
            p = p+1
        elif cmp == "Gun":
            print("computer wins")
            c = c+1
    elif plyer == "Water":
        if cmp==plyer:
            print("Its a draw")
        elif cmp == "Snake":
            print("Computer wins")
            c = c +1
        elif cmp == "Gun":
            print("player wins")
            p = p + 1
    elif plyer == "Gun":
        if cmp==plyer:
            print("Its a draw")
        elif cmp == "Water":
            print("Computer wins")
            c = c+1
        elif cmp == "Snake":
            print("player wins")
            p = p +1
    else:
        print("Enter a valid value")

    print("Chances Left: ",10 - i)
    print("Player points: ",p,"Computer points:",c)

    if i ==10:
        if c>p:
            print("Computer wins")
        elif p>c:
            print("Player Wins")
        else:
            print("Its a draw")
    i = i+1







