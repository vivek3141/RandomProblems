"""Project ChipRider
Using Lists and Classes
Mobile Phone Application
You have been asked to develop a system for a transport company. They are thinking
of introducing an electronic system for students who travel to school by bus.
The new system will be known as ‘ChipRider’. It has been invented to allow mobile
phone users to buy credit that is stored within a mobile phone application. This can be
used to buy tickets on buses. It means the students do not need to carry money to buy
their tickets.
The student can buy credit that is stored on the phone. When they get on a bus they
can use their phone to buy the on-screen ticket. The student gives their phone to the
driver. The driver types a code into the student’s phone. The code takes credits from
the stored balance on the phone.
The application can store a maximum of 30 credits to buy tickets.
There are two types of ticket:
Single – for a single journey from one place to another. This will cost 3 credits.
Return – for a journey from one place to another and a journey back to where they
came from. This will cost 5 credits.
The phone produces a ‘ticket’ on the screen that can be shown to an inspector if a
ticket needs to be checked.
When there is not enough credit on the phone, the student can buy credits to add to
their balance. This is done by the driver entering a special code that only he/she will
know.
The system must be able to perform all of the actions described in the situations
below
1. Buy a ticket (one person)
1. Allow the phone to accept a code that the driver types in
2. If the ticket is a single, deduct 3 credits from the balance
3. If the ticket is a return deduct 5 credits from the balance
4. If there is not enough credits on the phone, allow the student to top-up (see 3
below)
5. Generate a ticket for the journey on the screen (see 4 below)
2. Buy a ticket (more than one person – single journey only)
1. Allow the phone to accept a code that the driver types in.
2. Deduct 3 credits from the balance for each person travelling. So for three
people travelling, the cost would be 3 credits * 3 people = 9 credits.
3. If there is not enough credits on the phone, allow the student to top-up (see 3
below)
4. Generate a single on-screen ticket that would cover each of the travelers for
that journey (see 4 below)
3. Top-up the phone with travel credits
1. Allow the phone to accept a code that the driver types in
2. Allow the phone to be fully topped up to 30 credits in one transaction
3. Allow the phone to be partially topped up to any number of credits below 30.
4. Display a ticket
Allow the person to display a ticket for a driver or inspector to check.
The ticket should display the following information:
 Type of journey – Single or Return
 Number of students the ticket will cover for the journey
 Date and Time the ticket was paid for
 The amount paid for the ticket

5. Protect your credits from misuse by other people.
A parent of a student who has been asked to test this system is concerned that
someone who steals a mobile phone could use the ‘Chip Rider’ credit to make
free journeys on the bus.
You need to think of a way that could prevent this from happening.
Design and build a system that provides this functionality  so that credit stored
in the ‘ChipRider’ system is protected if the phone is stolen.
CONSIDERATIONS:
1. Use lists for the number of passengers.
2. Use classes and objects for tickets. Single and Double tickets could be created from a class."""


def ticket1(ticket):
    print("\n" * 30)
    print("---------------------------------------------------------")
    print("\n")
    print("\t\tTransport System")
    print("\n")
    print("---------------------------------------------------------")
    print("\n")
    print("\tThis is a,", ticket, " ticket.")
    print("\tPlease show this to your driver")
    print("\tThis is a", ticket, " ticket to NPS HSR")
    print("\n")
    print("---------------------------------------------------------")


credits = 0
ticket = []
for i in range(20):
    credits = credits + 1
print("\n" * 30)

while True:
    print("""Transportation menu
    1.Top up credits
    2.Buy loose credits
    3.Buy Tickets
    C.Show Credits
    T.Show Tickets
    E.Exit""")

    try:
        opt = input("Enter your option:")
    except ValueError:
        print("Please enter a valid opt")

    if (opt == "1"):
        if (credits == 30):
            input("You cannot enter any more credits.Press any key to continue:")
            print("\n" * 30)
        else:
            print("You have ", credits, " credits and can add ", 30 - credits, "more. Would you like to do so?(y/n)")
            while (True):
                try:
                    opt1 = input()
                except ValueError:
                    print("Please enter a valid opt")
                if (opt1 == "y"):
                    for i in range(30 - credits):
                        credits = credits + 1
                    print("You have ", credits, " credits")
                    input("Press any key to continue")
                    print("\n" * 30)
                    break
                elif (opt1 == "n"):

                    print("\n" * 30)
                    break
                else:
                    print("Please enter a valid opt")


    elif (opt == "2"):
        if (credits == 30):
            input("You cannot enter any more credits.Press any key to continue:")
            print("\n" * 30)
        else:
            while (True):
                print("You can buy a maximum of ", 30 - credits,
                      " credts. How much would you like to add?(By the way, if you add negetive credits, you lose credits and that's your problem)")
                try:
                    cre = int(input())
                except ValueError:
                    print("Please enter a valid integer:")
                if (cre <= 30 - credits):
                    input("This transaction is going to cost you " + str(cre * 5) + "Rs. Press any key to continue")
                    print("\n" * 30)
                    break
                else:
                    print("Please enter a valid addition of credits")
            credits = credits + cre
    elif (opt == "3"):
        print("(i)Single")
        print("(ii)Return")
        print("(iii)Go back")
        while (True):
            try:
                opt = input("Enter your option:")
            except ValueError:
                print("Please enter a valid opt")
            if (opt.upper() == "I"):
                if (credits < 3):
                    input("You cannot buy this ticket. Press any key to continue:")
                input("This ticket will cost 3 credits which is 15 Rs.Press any key to continue")
                ticket1("single")
                ticket.append("single")
                credits = credits - 3
                input("Press any key to continue")
                break
                print("\n" * 30)
            if (opt.upper() == "II"):
                if (credits < 5):
                    input("You cannot buy this ticket. Press any key to continue:")
                input("This ticket will cost 5 credits which is 25 Rs.Press any key to continue")
                ticket1("return")
                ticket.append("return")
                credits = credits - 5
                input("Press any key to continue")
                break
                print("\n" * 30)
            if opt.upper() == "III":
                input("Press any key to continue")
                break
                print("\n" * 30)

            else:
                print("Please enter a valid opt")

    elif (opt.capitalize() == "C"):
        print("You have ", credits, " credits")
        input("Press any key to continue")
        print("\n" * 30)
    elif (opt.capitalize() == "T"):
        for i in range(ticket.count("single")):
            ticket1("single")
            print("\n\n")

        for i in range(ticket.count("return")):
            ticket1("return")
            print("\n\n")
        input("Press any key to continue")
        print("\n" * 30)
    elif (opt.capitalize() == "E"):
        break
    else:
        print("Please enter a valid no.")
        input("Press any key to continue")
        print("\n" * 30)
