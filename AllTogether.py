### Part Four -- your code goes here. 
import random

list = []
outputlist = []
for i in range(10):
    list.append(random.randint(1,100))
    

for number in list:
    while number % 2 == 1 and number not in list:
        outputlist.append(number)
                   
print(f"The output list of odd numbers is: {str(outputlist)}.")