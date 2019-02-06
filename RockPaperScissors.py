# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:21:29 2019

@author: Micah
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:35:44 2019

@author: Micah
"""

from random import randint

#get name of player
playerName = input("Let's play 'Rock, Paper, Scissors'; best of 5! What's your name? ")

#set player score and computer score
playerScore = 0
computerScore = 0

#set loop that will run until player or computer wins 3 rounds
while playerScore < 3 and computerScore < 3:
    #get players choice, convert to lowercase to ensure it matches computer pick
    player = input("Ok, %s, choose one - rock, paper, or scissors: " % playerName).lower()

    #setting computer pick
    randnumb = randint(1,3)
    
    if randnumb == 1:
        computerpick = "rock"
    elif randnumb == 2:
        computerpick = "paper"
    else:
        computerpick = "scissors"

    #check to make sure player enters a valid choice
    if player == "rock" or player == "paper" or player == "scissors":
        #prints the two picks
        print("You chose %s, the computer chose %s" % (player, computerpick))
    
        #determins who wins the round, and adds a point to the correct score
        if player == computerpick:
            print("It's a draw.")
    
        elif player == "rock" and computerpick == "paper":
            print("You lose this round..")
            computerScore += 1
    
        elif player == "rock" and computerpick == "scissors":
            print("You win this round!")
            playerScore += 1
    
        elif player == "paper" and computerpick == "rock":
            print("You win this round!")
            playerScore += 1
        
        elif player == "paper" and computerpick == "scissors":
            print("You lose this round..")
            computerScore += 1
        
        elif player == "scissors" and computerpick == "rock":
            print("You lose this round..")
            computerScore += 1
        
        elif player == "scissors" and computerpick == "paper":
            print("You win this round!")
            playerScore += 1
            
        #prints the score after each round, if one player reaches 3, game over
        if playerScore > computerScore and playerScore != 3 and computerScore != 3:
            print("You're winning %s games to %s!" % (playerScore, computerScore))
        elif playerScore < computerScore and playerScore != 3 and computerScore != 3:
            print("You're losing %s games to %s.." % (computerScore, playerScore))
        elif playerScore == computerScore:
            print("It's tied, %s games to %s.." % (computerScore, playerScore))
        else:
            print("GAME OVER")
    #message to retry if input is not valid
    else:
        print("That's an invalid pick - please choose rock, paper, or scissors.")
        
#prints a message and the final score
else:        
    if playerScore > computerScore:
        print("Congrats %s! You beat the computer %s games to %s!" % (playerName, playerScore, computerScore))
    elif playerScore < computerScore:
        print("Sorry %s.. The computer beat you %s games to %s.." % (playerName, computerScore, playerScore))
