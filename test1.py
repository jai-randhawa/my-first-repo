import random


#Function for RockPaperScissors
def RockPaperScissors():
  print("Starting Rock Paper Scissors: \n")
  gamesuserwon=0
  gamescomputerwon=0
    
  while True:
    
    userchoice = int(input("1.Rock 2.Paper 3.scissors: "))
    computerchoice = random.randint(1,3)

    if userchoice == computerchoice:
      print("TIE GAME")
    elif userchoice==1 and ( computerchoice==3):
      print("YOU WIN")
      gamesuserwon=gamesuserwon + 1
    elif userchoice==1 and ( computerchoice==2):
      print("YOU LOST")
      gamescomputerwon =gamescomputerwon + 1
    elif userchoice==2 and ( computerchoice==3):
      print("YOU LOST")
      gamescomputerwon =gamescomputerwon + 1
    elif userchoice==2 and ( computerchoice==1):
      print("YOU WIN")
      gamesuserwon=gamesuserwon + 1
    elif userchoice==3 and ( computerchoice==1):
      print("YOU LOST")
      gamescomputerwon =gamescomputerwon + 1
    elif userchoice==3 and ( computerchoice==2):
      print("YOU WIN")
      gamesuserwon=gamesuserwon + 1
    else:
      print("Invalid number")

    if gamesuserwon == 3:
      print(f"Good bye from Tic Tac Toe: You won {gamesuserwon} computer won {gamescomputerwon}")
      exit()
    elif gamescomputerwon ==3:
      print(f"Good bye from Tic Tac Toe: You won {gamesuserwon} computer won {gamescomputerwon}")
      exit()

    

print("\n ROCK PAPER SCISSORS, FIRST ONE TO 3 WINS, WINS \n")
RockPaperScissors()

  
