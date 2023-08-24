import random
import sys

def theBigger(l : list ) -> int:
    big = 0
    for i in l :
        if i > l[big] :
            big = l.index(i)
    return big

def roll() -> int:
    return random.randint(1,6)

def checkIfEnd(l : list , max : int ) -> bool :
    i = 0
    while i <= len(l) -1 :
        if l[i] >= max  :
            return True
        i +=1
    return False


def throw(l : list , current : int ) -> bool :
    print("Thronwing the Dice ...")
    x= roll()
    print(f"You Got {x}")
    if x == 1 :
        print("Better luck next time !")
        l[current] = 1
        return False
    else :
        l[current] += x
        return True
    

def risk(still : bool ) -> bool :
        if still :
            while True :
                rep = input("take the risk and throw again ?  \n(reply by y/n) : ").capitalize()
                if rep == "Y" :
                    return True 
                elif rep == "N" :
                    return False
                else :
                    print("enter a valid enswear pls !") 
        else :
            return False
    

print("this is the Pig game .....") #complete the game explnation 




while True:
    try:
        playersnum = input("enter the number of the players : ")
        playersnum = int(playersnum)  
        break  
    except ValueError:
        print("Invalid input. Please enter an integer.")


while True:
    try:
        max = input("enter the winning value : ")
        max = int(max)  
        break  
    except ValueError:
        print("Invalid input. Please enter an integer.")

#unfinished idea
while True:
    try:
        max2 = input("enter the max number of rounds you want to play : ")
        max2 = int(max2)  
        break  
    except ValueError:
        print("Invalid input. Please enter an integer.")

players = [0 for _ in range(playersnum)]  #more pythonic

# i = 0
# while i < playersnum :
#     players.append(0)
#     i += 1

i = 0
round = 0

while True and round < max2:
    if i >= playersnum :
        i = 0
        round += 1

    print(f"player {i+1} Turn...")

    
    still = throw(players,i)

    if checkIfEnd(players,max) :
        print(f"PLAYER {i+1} WON")
        sys.exit()
        
    

    agree =risk(still)

    while still and agree :
        still = throw(players,i)
        if checkIfEnd(players,max) :
            print(f"PLAYER {i} WON")
            sys.exit()
        if still :
            agree = risk(still)

    i += 1
    


winner = theBigger(players)
print(f"Player {winner + 1} Won".capitalize())

