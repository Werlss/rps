import random
import os 

how_many_games_played=0 
how_many_games_won=0
game_choices = ["rock", "paper", "scissors"]

while True:
  comp_choice = random.choice(game_choices)
  os.system("clear")
  print("New Game Starting")
  print("number of games played:")
  print(how_many_games_played)
  print("number of games won:")
  print(how_many_games_won)

  how_many_games_played = how_many_games_played +1

  user_choice = input("Enter a choice (rock, paper, scissors):" )

  if user_choice == "rock" and comp_choice == "paper":
    print("You Lost")
    input("Press enter to continue.")
  elif user_choice == "rock" and comp_choice == "scissors":
    print("You Won!") 
    how_many_games_won = how_many_games_won +1 #<--- Put it on its own line every time.
    input("Press enter to continue.")
  elif user_choice == "rock" and comp_choice == "rock":
    print("Tie")
    input("Press enter to continue.")
  elif user_choice == "paper" and comp_choice == "rock":
    print("You Won")
    how_many_games_won = how_many_games_won +1
    input("Press enter to continue.")
  elif user_choice == "paper" and comp_choice == "scissors":
    print("You Lost")
    input("Press enter to continue.")
  elif user_choice == "paper" and comp_choice == "paper":
    print("Tie")
    input("Press enter to continue.")
  elif user_choice == "scissors" and comp_choice == "rock":
    print("You Lost")
    input("Press enter to continue.")
  elif user_choice == "scissors" and comp_choice == "paper":
    print("You Won") 
    how_many_games_won = how_many_games_won +1
    input("Press enter to continue.")
  elif user_choice == "scissors" and comp_choice == "scissors":
    print("Tie")
    input("Press enter to continue.")

    
    
    
    
    
    
    #Here is your To Do List:
#1. Finish the other conditions and print statements. Don't forget there can be a tie.
#2. You made variables for games played and games won. Increment them based on which condition is met. You might want a games lost too.
#That should pretty much finish it.
#Good? 


# one question? Do i still continue to but elif or is that it.
# You need more elif statements. you need to account for every possible combination.
#rock-rock
#rock-scissors
#paper-rock
#paper-scissors
#scissors-paper
#scissors-rock
#And the tie, which is always:
#user_choice == comp_choice
#that accounts for
#paper-paper
#rock-rock
#scissors-scissors
#Understand?
#Of course.

#can I get a hint on how I can add +1 after every match

# You do something like: variable = variable + 1
# So for instance:
# how_many_games_won = how_many_games_won + 1

#ohhho