import random
 
# def loopInput(playerChoice):
#     while(playerChoice != "R" and playerChoice != "P" and playerChoice != "S"):
#         playerChoice = input("Choose an option [R, P, S]: ")
 
#         if(playerChoice != "R" and playerChoice != "P" and playerChoice != "S"):
#             print("Invalid option! Try again!")
 
playerChoice = ""
computerChoiceFull = ""
playerChoiceFull = ""
 
while(playerChoice != "R" and playerChoice != "P" and playerChoice != "S"):
    # chose inputs
    playerChoice = input("Choose an option [R, P, S]: ")
    computerChoice = random.sample(["R", "P", "S"], 1)
 
    # if invalid
    if(playerChoice != "R" and playerChoice != "P" and playerChoice != "S"):
        print("Invalid option! Try again!")
 
    # Convert to words
    if(playerChoice == "R"):
        playerChoiceFull = "Rock"
 
    if(computerChoice[0] == "R"):
        computerChoiceFull = "Rock"
 
    if(playerChoice == "P"):
        playerChoiceFull = "Paper"
 
    if(computerChoice[0] == "P"):
        computerChoiceFull = "Paper"
 
    if(playerChoice == "S"):
        computerChoiceFull = "Scissors"
 
    if(computerChoice[0] == "S"):
        computerChoiceFull = "Scissors"
 
    # print outcome
    print("\n\nPlayer : (", playerChoiceFull, ") CPU : (", computerChoiceFull, ")\n\n")
 
    # Compare the inputs
    if(playerChoice == computerChoice[0]):
        print("Its a tie!")
        playerChoice = ""
 
    elif(playerChoice == "R" and computerChoice[0] == "S"):
        print("You Won!")
 
    elif(playerChoice == "P" and computerChoice[0] == "R"):
        print("You Won!")
       
    elif(playerChoice == "S" and computerChoice[0] == "P"):
        print("You Won!")
 
    elif(playerChoice == "S" and computerChoice[0] == "R"):
        print("You Lost!")
        playerChoice = ""
 
    elif(playerChoice == "R" and computerChoice[0] == "P"):
        print("You Lost!")
        playerChoice = ""
       
    elif(playerChoice == "P" and computerChoice[0] == "S"):
        print("You Lost!")
        playerChoice = ""
 
    else:
        print("You Lost")
        playerChoice = ""