import random
choices = ["rock", "paper", "scissors"]
user = input("Enter Rock, Paper or Scissors: ").lower()
computer = random.choice(choices)
print("You:", user)
print("Computer:", computer)
if user == computer:
    print("Match Draw!")

elif user == "rock" and computer == "scissors":
    print("You Win!")

elif user == "paper" and computer == "rock":
    print("You Win!")

elif user == "scissors" and computer == "paper":
    print("You Win!")

else:
    print("Computer Wins!")

# ###
# import random
# user_score==0
# computer_score==0
# user_score+=1
# computer_score+=1
# print("your score",user_score)
# print("computer score",computer_score)
# while true:
#     again=input("play again? (yes/no):").lower() 

python -m pip install streamlit

