#A student wishes to create an application to store student first name and telephone
#numbers into lists. Create that application with 2 menu options. One that accepts the
#name and telephone number and the other that performs the search. Create 2 lists, one
#for the name and the other for the numbers
import filereader

flname = "c:\\000\\File.txt"
filereader.write_line("",flname)

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
                
                
                break
                
            else:
                print("Invalid Input, Please enter full name")
              
        while(True):
            phno = input("\nEnter your number:")
            if len(phno) == 10:
                
                break
            else:
                print("Invalid Input.The length should be 10 no.s")
        filereader.append_line("\n"+name+"\t"+phno,flname)          
                
        input("Succesfully added. Press any key to continue:")
        print("\n"*30)
                

    elif(opt == "2"):
        name = input("\nEnter your name:")
        c = False
        b = 0
        a = 0
        d = 0
        list = ["",""]
   
        f = open("c:\\000\\File.txt")
        for i in f:
            a = i.split("\t")
            list.extend(a)
       
        for i in list:
            if(name == i):
                print(name,"'s phone no. is",list[d+1])
                c = True
                break
            d = d + 1
        f.close()
       
            
            
                
                
       
        
        
        if(c == False):
            print("Not found")
        input("Press any key to continue:")
        print("\n"*30)    
  
    elif(opt.upper() == "S"):
        print("\n"*30)
        filereader.readall(flname)
        input("Press any key to continue:")
        print("\n"*30)
    else:
        input("Press any key to continue")
        print("\n"*30)
        
        
