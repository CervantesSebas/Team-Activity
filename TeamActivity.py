#Sebastian Cervantes 
#Aibek Abasov
#October 29, 2024 
#This program will take a number (input) from the user and guess a randomly generated number.

import random

number = int(input("Please guess number 1-10; "))
answer = random.randrange(1,10)
while number > answer:
    print (f"Please guess lower")
    number = int(input("Please guess number 1-10; "))
while number < answer:
    print (f"Please guess higher")
    number = int(input("Please guess number 1-10; "))
    
if number == answer:
    print ("Well done you guessed it right ")
  
