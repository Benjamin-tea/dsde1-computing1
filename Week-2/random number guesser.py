import random as r

print('Guess a number between 1 and 10?')

usr_guess = input()

ran_no = r.randint(1,10)

def numbertest(): 
    try:
        val = int(usr_guess)
    except ValueError:
        print('Please enter a valid number')
        usr_guess = input()
        numbertest()

while usr_guess.isdigit():
    usr_guess = int(usr_guess)
    if ran_no==int(usr_guess):
        print('Congratulations! The number you guessed was correct')    
    else:
        print('Bad luck, the number you guessed was wrong! Try again please')

