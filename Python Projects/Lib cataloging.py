#Project 2 : Library Book Stocking System

#A library is in the process of updating its system and cataloguing all the books. The following
#coding scheme is followed. Code is a 5 digit number.
#Code starts with 1 – Magazine
#Code starts with 2 – Fiction
#Code starts with 3 – Non Fiction
#Code  starts with 4 – Reference
#Code starts with 5 – Regional, non English

#Accept the code number, and if code  does not start with 1-5 display invalid message and go
#back to accepting code. If code number is not 5 digits do the same.

#If the code number entered is 99999 stop accepting book codes.

#In the end print a report 

#  Report of Number of each type of book entered
#Number of Magazines: 34
#Number of Fiction books: 20
#Number of Non-Fiction books: 2
#Number of Reference books:0
#Number of Regional books:12

#Thank you for using our Book Stocking System

#author:Vivek Verma
#17.10.14
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
i = 0
while(True):
    print("A library is in the process of updating its system and cataloguing all the books. The following")
    print("coding scheme is followed. Code is a 5 digit number.")
    print("\t\nCode starts with 1 – Magazine")
    print("\tCode starts with 2 – Fiction")
    print("\tCode starts with 3 – Non Fiction")
    print("\tCode  starts with 4 – Reference")
    print("\tCode starts with 5 – Regional, non English")
    while(True):
        cde = int(input("Enter your code:"))
        if(cde == 99999):
            break
        cde = cde//10000
        if(cde == 1):
            a = input("Press any key to continiue:")
            h1 = h1 + 1
            break
            print("You have selected a book from the category-Magazines")
        elif(cde == 2):
            a = input("Press any key to continiue:")
            h2 = h2 + 1
            print("You have selected a book from the category-Fiction")
            break
        elif(cde == 3):
            a = input("Press any key to continiue:")
            h3 = h3 + 1
            print("You have selected a book from the category-Non-Fiction")
            break
        elif(cde == 4):
            a = input("Press any key to continiue:")
            h4 = h4 + 1
            print("You have selected a book from the category-Reference")
            break
        elif(cde == 5):
            a = input("Press any key to continiue:")
            h5 = h5 + 1
            print("You have selected a book from the category-Regional, non English")
            break
        else:
            print("Invalid Input")
            continue
    
print("\n"*30)
print("\nReport of Number of each type of book entered")
print("\tNumber of Magazines:",h1)
print("\tNumber of Fiction books:",h2)
print("\tNumber of Non-Fiction books:",h3)
print("\tNumber of Reference books:",h4)
print("\tNumber of Regional books:",h5)
