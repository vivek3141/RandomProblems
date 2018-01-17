#A student wishes to create an application to store student first name and telephone
#numbers into lists. Create that application with 2 menu options. One that accepts the
#name and telephone number and the other that performs the search. Create 2 lists, one
#for the name and the other for the numbers
lno= []
lname = []
    
print("\n"*30)
while(True):
    print("""\t\tTelephone Directory
    \n1.Add number
    \n2.Search
    \nS.Show Records
    \n3.Exit""")
    opt = input("\nEnter your option")
    
    if(opt == "1"):
        while(True):
            name = input("\nEnter your name:")
            if name.find(" ") != -1:
                print("Appending...")
                
                lname.append(name)
                break
                
            else:
                print("Invalid Input due to no space")
        while(True):
            phno = input("\nEnter your number:")
            if len(phno) == 10:
                lno.append(phno)
                break
            else:
                print("Invalid Input.The length should be 10 mo.s")
        input("Succesfully added. Press any key to continue:")
        print("\n"*30)
                

    if(opt == "2"):
        name = input("\nEnter your name:")
        c = False
        print(lname)
        a = 0
        for i in lname:
            if(name == i):
                
                print("\n",lname[a],"'s telephone no. is",lno[a])
                input("Press any key to continue:")
                print("\n"*30)
                c = True
            a = a+1
        if(c == False):
            print("Not found")
    if(opt == "3"):
        break
    if(opt == "S"):
        print("\n"*30)
        b = 0
        print("Name"," "*8,"Telephone No.")     
        for i in lname:
            
                
            print("\n",lname[b]," "*8,lno[b])
                
            b = b + 1
        input("Press any key to continue:")
        print("\n"*30)
    else:
        input("Invalid Input.Press any key to continue")
        print("\n"*30)
        
        
