import random as ra
op =["Stone", "Paper" , "Scissors"]
opi=["yes","no"]
do= " "
while do not in opi:
    do = input("Do u want to play the game??: ")
    do = do.lower()
    while do == "yes" or do=="yeah" or do== "yup" or do== "yupp" or do=="yea":
        pl=" "
        while pl not in op:
            pl=input("Enter your Sign: ")
            pl=pl.lower()
            pl=pl.capitalize()
            if pl in op:
                pc = ra.choice(op)
                print("Computer's Choice: " +pc)
                if pc == "Stone":
                    if pl=="Stone":
                        print("It's a tie")
                    elif pl=="Paper":
                        print("You win")
                    else:
                        print("Computer Wins")
                elif pc == "Paper":
                    if pl == "Paper":
                        print("It's a tie")
                    elif pl == "Scissors":
                        print("You win")
                    else:
                        print("Computer Wins")
                elif pc == "Scissors":
                    if pl=="Scissors":
                        print("It's a tie")
                    elif pl=="Stone":
                        print("You win")
                    else:
                        print("Computer Wins")
            else:
                print("Enter a correct Sign")
        print("------------------------------------------------")
        print("Do you want to play again??")
        o= input("Enter your opinion: ").lower()
        do=o
    while do =="no" or do=="nope" or do=="nah":
        print("Thanks for Visiting")
        exit(0)
    while do not in opi:
        print("Invalid Option")
        exit(0)

