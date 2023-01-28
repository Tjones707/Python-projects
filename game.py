import random
def play():
    options = ['rock','paper','scissors']
    #play input
    val = random.choice(options).lower()
    user_1 = input("pick rock paper or scissors\n").lower()
    print ("you chose "+ user_1 + "\nthe computer chose "+val)
    #game breakdown
    if user_1 == "Rock" and val == "Rock":
        print("tie")
    elif user_1 == "rock" and val == "scissors":
        print("you win!")
    elif user_1 == "rock" and val == "paper":
        print("you lose!")
    elif user_1 == "paper" and val == "paper":
         print("tie")
    elif user_1 == "paper" and val == "scissors":
        print("you lose!")
    elif user_1 == "paper" and val == "rock":
        print("you win!")
    elif user_1 == "scissors" and val == "scisssors":
        print("tie")
    elif user_1 == "scissors" and val == "rock":
        print("you lose")
    elif user_1 == "scissors" and val == "paper":
        print("you win")
    #end game 
def main():
    play()
    while True:
        txt = input("wanna play again y/n\n")
        if txt =="y": 
            play()
        else:
            break
main()
 