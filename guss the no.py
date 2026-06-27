print("I am thinking of a number between 1 and 200")
print("You have 10 tries to guess the number")

import random
number = random.randrange (1,200)


number_input = int (input("entar your number "))
tries= 10


while tries >= 1:
    try:
        if number_input==number:
            print ("you win")
            break

        elif number_input < number:
            print ("your number is small")
    
        elif number_input > number:
            print ("your number is big")

    
    
        tries -= 1
    
        if tries==0:
            print ("you loss")
            break
    
        print (f"you have only {tries} tries" )
        number_input = int (input("try agen "))
    except:
        print("you can enter only number")
print (f"the corect answer is {number}")
