def acceptno(msg):
 
       
        num = int(input(msg))

        
        
            
while(True):
    print("This is a calculator.It will keep repeating until you press exit")
    acceptno("Enter first number:")
    acceptno("Enter second number:")
    print("This is the menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. Modular arthemetic")
    print("7. exit")
    opt = int(input("What is your option?"))
    if(opt == 1):
        print("You have chosen to Add. The answer is:",num1+num2)
    elif(opt == 2):
        print("You have chosen to Subtract. The answer is:",num1 - num2)
    elif(opt == 3):
        print("You have chosen to Multiply. The answer is:",num1*num2)
    elif(opt == 4):
        print("You have chosen to Divide. The answer is:",num1/num2)
    elif(opt == 5):
        print("You have chosen to raise to the power of. The answer is:",num1**num2)
    elif(opt == 6):
        print("You have chosen to use modular arthemetic. The answer is:",num1%num2)
    elif(opt == 7):
        break
        print("You have chosen to exit. You are now exiting my great calculator.How bad of you!")
        exit()
    else:
        print("Invalid input")
