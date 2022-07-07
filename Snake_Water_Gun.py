import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

print("comp chose: snake(1), water(2) or gun(3)?")
randomNo=random.randint(1,3)
if randomNo==1:
    comp="s"
elif randomNo==2:
    comp="w"
elif randomNo==3:
    comp="g"

you=input("Enter your choice: ")
a=gameWin(comp,you)

print(f"comp choice {comp}")
print(f"your choice {you}")

if a==None:
    print("It's a tie")
elif a:
    print("You win!")
else:
    print("You lost")

