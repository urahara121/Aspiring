
'''
snake=1
gun=-1
water=0
'''
import random
computer=random.choice([-1,0,1])
you=input("Enter option(s/w/g): ")  #enter snack as s ,water as w ,gun as g
youDic={"s":1,"g":-1,"w":0}
newDic={1:"snake",-1:"gun",0:"water"}
choice=youDic[you]

print(f"Your choice is: {newDic[choice]}\nComputers choice is: {newDic[computer]}")

if (computer==choice):
        print("Its a Draw")

else:
    if computer==1 and choice==-1:
        print("You Win")
    elif computer==1 and  choice==0:
        print("You Loose")
    elif computer==-1 and choice==1:
        print("You Loose")
    elif computer==-1 and choice==0:
        print("You Win")
    elif computer==0 and choice==-1:
        print("You Loose")
    elif computer==0 and choice==1:
        print("You Win")
   
  



   
    
    

   

            



