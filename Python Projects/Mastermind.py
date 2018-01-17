"""This assignment is worth 30 points (3% of the course grade) and is part of the computer science 
curriculum Computer Science Engineering - Second Year.
 
Assignment Overview
In this assignment, we are going to implement a simple number guessing game that is often
know as the game of Mastermind. This assignment will give you more experience on the use of: 
  
1. Strings
2. User input
3. If statements
4. While statements 
Task 
We create a secret number (typically by prompting a “game administrator”). We then prompt the 
“game player” to guess the number. Our program gives the player some feedback on their guess.
Based on that feedback, the player makes another guess. Guessing continues until the “secret”
number is guessed or until the maximum number of tries is reached.

Our responsibility in this program is to “host” the game, that our program will provide
interaction with the game administrator and the game player.  Ideally, these would be different
people; but for purposes of testing, you will be both the administrator and the player.
 
Program Specifications: 
1) Prompt the administrator for a secret number. The number should be 5 digits long and no
digit should be repeated in the number. 12345 is a good number, 55432 is not, nor is 444. 
If the administrator enters an ill-formed “number,” print an error diagnostic and reprompt
for a correctly formed secret number. When a correctly formed number is entered, print some blank lines so the game player won’t be able to see it.

2) Ask the player to provide a guess 5-digit number. If the player’s input is not a 5-digit
number (not all digits, not of length of 5), ask the player to provide another guess.  
3) Given a 5 digit guess by the player, report two results. 
a) First, report how many of the digits in the “secret number” also appear in the 
guess, independent of whether the guess digits are in the correct positions.
b) Second, we report how many of the guess digits are in the correct position.  
For example, imagine that the secret number is 12345 and that the player guesses 12567. 
Note that three digits in the secret number (the 1,3,5) are also in the guess. Moreover, two
of the digits (1 and 2) are in their correct positions.  Thus, your program should report the
number of correct digits as 3 and the number in the correct positions as 2.   
4) After each guess, report the player’s progress (number of guesses, their guess, number of
correct digits, number of digits in the correct positions). See the example. 
5) At the end, if the player successfully guesses the number, print out how many guesses the 
player has used. 
6) Set a maximum number of guesses (your choice, but report it when the game starts) for
the game. If the player exceeds this maximum, report that the player lost. 
 
7) During the process, allow the player to quit the game. If they quit, report that they lost
and what the number of guesses was. 
"""
def samedig(str1):
   
    for x in str1:
        cnt = str1.count(x)
  
        if(cnt > 1):
            return True
def same2dig(str1,str2):

    cnt = 0
    for x in str1:
        if(x in str2):
            cnt = cnt + 1
       

    return cnt
def sameposition(str1,str2):
    i = 0
    for x in str1:
        if(str1[i] == str2[i]):
            print(str1[i] ," is in correct position", i+1)
        i = i + 1
            
    
    
        
        
        
    
            
                
    
            
        
      
 
        
        
    
#This is the comment
print("Administrator please take over")
while(True):
    no = input("Please enter your number for the other player to guess(Enter 00000 to exit)5:")
    n = 0
    if(no == "00000"):
        exit()
    for i in no:
        n = n+1
    
    if(n != 5):
       
        print("Please enter a valid number")
    
        
    if(n == 5):
        a = samedig(no)
    
        
    if(no[0] == 0):
        print("Please enter a valid number")
        
        
    
    if(a):
        
        print("Please enter a valid number")
    else:
        break

print("\n"*100)
print("User please take over")
for i in range(5):
    while(True):
        guess = input("Please enter your number which you are guessing(Enter 00000 to exit):")
        n = 0
        if(no == "00000"):
            exit()
        for i in guess:
            n = n+1
        
        if(n != 5):
           
            print("Please enter a valid number")
        
        if(n == 5):
            a = samedig(guess)
            
        if(guess[0] == 0):
            print("Please enter a valid number")
        
            
       
        if(a):
            print("Please enter a valid number")
        else:
            break
    if(guess == no):
        print("Player has won the game")
        exit()
    b = same2dig(no,guess)
    print(b,"digits are correct")
    sameposition(no,guess)
print("Administrator has won the game")

        


            
    
    

