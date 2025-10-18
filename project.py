import random
def number_guessing_game():
    print("Welcome to my number Guessing game")
    print("I am thinking of a number between 1 to 100")
    target=random.randint(1,100)
    attempts=0

    while True:
       user_target=input("enter your target or Quit:")
       attempts+=1
       if(user_target=="Quit"):
           break
       user_target=int(user_target)
       if(user_target==target):
           print("congratulations-correct guess! in",attempts,"attempts")
           break
       elif(user_target>target):
           print("your guess is big,Try again")
       elif(user_target<target):
           print("your guess is small,Try again")
           
       else:
           print("invalid interger,guess a number between the range ")    

    print("GAME OVER") 
number_guessing_game()               
