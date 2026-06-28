import random 

# this is a function ------------------------------------------
def get_choices():
  print()
  print()
  print()
  print()
  print("Enter a choice..")
  print()
  player_choice = input("~~~~ rock, paper, or scissors ? ~~~~")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
# -------------------------------------------------------------


# this is another function with an 'if' statement -------------
def check_win(player, computer):
  print()
  print()
  print()
  print()
  print(f"You chose {player}, computer chose {computer}")
  print()
  if player == computer:
    return "It's a tie !"
  
# 'if', 'else', 'elif' statements -----------------------------
  elif player == "rock":
      if computer == "scissors":
          return "Rock smashes scissors ! .... You win ! ;)"
      else:
          return "Paper covers rock ! Womp Womp you lose ....."
    
  elif player == "paper":
        if computer == "rock":
          return "Paper defeats rock ! .... You win ! ;)"
        else:
          return "Scissors and paper aren't friends ! Womp Womp you lose ....."
   
  elif player == "scissors":
        if computer == "paper":
          return "Scissors cuts paper ! .... You win ! ;)"
        else:
          return "Rock smashes scissors. Womp Womp you lose ....."
 # -------------------------------------------------------------


 # function call -----------------------------------------------
choices = get_choices()
result = check_win(choices["player"], choices ["computer"])
print(result)
# -------------------------------------------------------------






     
# elif statement inside this same function --------------------
  #elif player == "rock" and computer == "scissors": # if this is 'true' the output will be the return statement
    #return "Rock smashes scissors ! You win ! ;)"
  
  #elif player == "rock" and computer == "paper":
    #return "You really let a computer beat you !? Try again .."
# -------------------------------------------------------------

# this is a function 'call' ------------------------------------
  #check_win("rock", "paper")
# -------------------------------------------------------------




# the program wont run until it is 'called'

# f string ( (short for "formatted string literal") is a concise and readable way to embed variables and expressions directly into a string in Python )
 # example: age = 25
 #          print(f"Jim is {age} years old.")

  
