#Menu of WW Food
cost = 0
items = ""
i = 0
while(i<3):

    password = input("Enter password:")
    if(password == "WW Food"):
        print("Correct password")
        break
    else:
        print("Wrong password")
        i = i+1

if(password != "WW Food"):
        
        
        exit()
    

while(True):
    print("\t\t WW Food")
    print("\n\nAppitizers")
    print("\t1.Bruschetta salad............120 Rs")
    print("\t2.Greek salad.................150 Rs")
    print("\t3.Garlic Bread................120 Rs")
    print("\t4.Ravioli.....................150 Rs")
    print("\n\nMain Course")
    print("\t5.Margharita pizza............200 Rs")
    print("\t6.Country Feast(pizza)........250 Rs")
    print("\t7.Veggie burger...............220 Rs")
    print("\n\nDessert")
    print("\t8.ice-cream...................10 Rs")
    print("\n\n9.Exit, display your cart and order")   
    opt = input("\n\nEnter your selection:")
    if(opt == "1"):
        cost = cost + 120
        items = items+"\nBruschetta salad.....120 Rs"
        print("You have chosen Bruschetta salad")
    elif(opt == "2"):
        cost = cost + 150
        items = items+"\nGreek salad..........150 Rs"
        print("You have chosen Greek salad")
    elif(opt == "3"):
        cost = cost + 120
        items = items+"\nGarlic bread.........120 Rs"
        print("You have chosen Garlic bread")
    elif(opt == "4"):
        cost = cost + 150
        items = items+"\nRavioli..............150 Rs"
        print("You have chosen Ravioli")
    elif(opt == "5"):
        cost = cost + 200
        items = items+"\nMargharita pizza.....200 Rs"
        print("You have chosen Margharita pizza")
    elif(opt == "6"):
        cost = cost + 250
        items = items+"\nCountry feast........250 Rs"
        print("You have chosen Country feast")
    elif(opt == "7"):
        cost = cost + 220
        items = items+"\nVeggie burger........220 Rs"
        print("You have chosen Veggie burger")
    elif(opt == "8"):
        cost = cost + 10
        items = items+"\nice cream............10 Rs" 
        print("You have chosen classic ice cream")
    elif(opt == "9"):
        break
    else:
    
        print("Invalid input")
    input("\nPress any key to continue:")
    print("\n"*30)
print("\n"*35)
print("Cart")
print(items)
print("The total cost is ",cost,"Rs")
while(True):
    opt = input("\n\n\nHow would you like to pay (Cash or Card)?")
    if(opt == "Card"):
       
        while(True):
            b = 0
           
            cno = input("\nEnter your card no.(Please enter in this  format ****************):")
            
            cno.replace(" ","",0)
            for i in cno:
                b = b + 1
                
            if b  == 16:
                break
            else:
                print("Invalid Input")
        while(True):
            b = 0 
            try:
                sno = input("\nEnter your security number(Please enter in this format ***):")
                
            except TypeError:
                print("Invalid Input")
            sno.replace(" ","",0)
            for i in sno:
                b = b + 1
            if b == 3:
                break
            else:
                print("Invald Input")
        
        print("\nSucessfully Paid. Your order will come soon!")
        input("Press any key to continue")
        break
    if(opt == "Cash"):
        print("\nIf you are ordering on the ipads in our shop, then please go to the conter and pay or if you are taking the option COD then please pay when we come")
        input("Press any key to continue:")
        break
    else:
         print("Invalid Input")
              
    
    
        
     
    
    
