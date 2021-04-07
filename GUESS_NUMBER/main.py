
#A MINI GAME IN PYTHON, WHERE WE HAVE TO GUESS A NUMBER BETWEEN 1 AND 10.


#first we have to import the random library.
import random

#create a function guess for generate the random number.
def guess(x):
    
    random_number = random.randint(1, x)   # defining the range of the random_number. 
    
    guess = 0      #geting a valor for the guess.
    
    while guess != random_number:        # using the while loop to still running the prog at the user guess correctly( when the guess == random_number loop stop) .
        
        guess= int(input(f'Guess a number between 1 and {x}:\n'))
        if guess < random_number:
            print ('Sorry, guess again. Too low.')      # tip.
        elif guess > random_number:
             print('sorry, guess again. Too high')      #tip.
    print(f'congrats, you have guessed the number')     #the end game.

guess(10)  # limit.
