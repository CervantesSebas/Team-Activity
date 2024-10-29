#Sebastian Cervantes 
#Aibek Abasov
#October 29, 2024 
number = float(input("Please guess number 1-10; "))
answer = int(6)
if number == answer:
    print ("Well done you guessed it right ")
elif number > answer :
    print ("Please guess lower")
elif number < answer:
    print ("Please guess higher")
  
