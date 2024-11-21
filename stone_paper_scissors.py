import random 

choices = ["Scissor", "Paper","Stone"]

remaining_guess = 0

user_win = False

while user_win == False and remaining_guess < 3:

    cpu_choices = random.choice(choices)
    userchoice = input("Enter a choice : ")
    player = userchoice.capitalize()
    
    if player == "Stone" or cpu_choices == "Paper":
        print("cpu won")

    elif player == "Stone" and cpu_choices == "Scissor":
        print("player win")
        user_win = True
        remaining_guess = 0

    elif player== "Stone" and cpu_choices == "Stone":
        print("draw")      



    elif player == "Paper" and cpu_choices == "Paper":
        print("Draw")
        
    elif player == "Paper" and cpu_choices == "Stone":
        print("You won")
        user_win = True
        remaining_guess = 0

    elif player == "Paper" and cpu_choices == "Scissor":
        print("Cpu won")


    
    elif player == "Scissor" and cpu_choices == "Paper":
        print("You won")
        user_win = True
        remaining_guess = 0

    elif player == "Scissor" and cpu_choices == "Stone":
        print("cpu won")

    elif player == "Scissor" and cpu_choices == "Scissor":
        print("draw") 
    
    else:
        print("enter a valid choice")     
    print(cpu_choices)
    remaining_guess = remaining_guess + 1
    print(remaining_guess)
    