### Part Two -- your code goes here. 
import random 

numbertobeguessed = random.randint(1,100)
numberguess = 0

while (numberguess != numbertobeguessed):
    numberguess = int(input("What is your guess for the number between 1 and 100."))


print(f"The number was: {numbertobeguessed}.")