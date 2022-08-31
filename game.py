import random

comp_guess = random.randint (1,10)

limit = 0
score = 0

#0,1,2....

while limit < 3:
     try:
        user_guess = int(input("Guess a number b/w 1-10;"))
        if(user_guess>10 or user_guess<0):
            print("wrong input")
            limit=limit
      
     except:
         print("Please give correct input")

     if(comp_guess == user_guess):
         if(limit==0):
            score+=15
            break
         if(limit==1):  
            score+=10
            break
         if(limit==2):
            score+=5
            break
         else:
            score=score
     elif(comp_guess>user_guess):
         print("your guess no is lower than my number") 
     else:
         print("your guess no is upper than my number")
     limit+=1
if(limit>2):
     print("you tries many times")
     print("My number was{}".format(comp_guess))
else:
     print("congo! Your score is{}".format(score))

            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  


      