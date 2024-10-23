### Part Four -- your code goes here. 
import random

list = []

for i in range(10):
    list.append(random.randint(1,100))
    
# Creates a copy of the list (can be used in iterating while removing items) from Python Engineer: https://www.python-engineer.com/posts/remove-elements-in-list-while-iterating/
# The syntax is {list name}[:]
for number in list[:]:
    while number % 2 == 0 and number in list:
        list.pop(list.index(number))
print(f"The output list of odd numbers is: {str(list)}.")