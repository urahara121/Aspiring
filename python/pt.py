def calculator():
    

    select=input("Enter operation you want(*,+,-,/): ")

    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))

    if select=='*':
        print("The result is: ",x*y)

    
    elif select=='+':
        print("The result is: ",x+y)

    
    elif select=='-':
        print("The result is: ",x-y)

    
    elif select=='/':
        print("The result is: ",x/y)

    else:
         print("Please enter a valid choice")

calculator()

    



   

    