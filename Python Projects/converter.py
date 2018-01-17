    #This is a converter
import f_conv
    #Importing f_conv which contians functions for converting
def mainmenu():
    print("\t\t\t\tUnit Converter")
    print("\n\t\t\t1.Distance")
    print("\n\t\t\t2.Weights")
    print("\n\t\t\t3.Temperature")
    print("\n\t\t\t4.exit")
    #Creating a function for the main menu so that it is easier
def dismenu():
    print("\n\t\t\t\tDistance")
    print("\n\t\t\t1. M to Feet, Yard, Mile")
    print("\t\t\t2. Feet to M, Yard, Mile")
    print("\t\t\t3. Mile to Yard, M, Feet")
    print("\t\t\t4. Yard to Feet, M, Mile")
    print("\t\t\t5. Go Back")
    #Creating a function for the distance menu so that it is easier

def weimenu():
    print("\n\t\tWeights") 
    print("\n1. Kg to Ounce, Pounds")
    print("2. Ounce to Kg, Pounds")
    print("3. Pounds to Kg, Ounce")
    print("4. Go Back")
    #Creating a function for the weights menu so that it is easier

def temenu():
    print("\n\t\tTemperature")
    print("\n1. Degrees C to Degrees F, Kelvin")
    print("2. F to C, Kelvin")
    print("3. Kelvin to C, F")
    print("4. Go Back")
   #Creating a function for the temperature menu so that it is easier

def printreport(whatstr, what, firststr, first, secondstr, second, thirdstr, third):
    print(what, whatstr, "has been converted into")
    print(first,firststr)
    print(second,secondstr)
    if(thirdstr != "None"):
        print(third,thirdstr)
    input("Press any key to continue:")
    print("\n"*30)
    
def acceptno(msg):
    print("\n")
    while(True):
        try:
            num = int(input(msg))
            
            return num
        except ValueError:
            print("Invalid input")
            continue
        

while(True):
    mainmenu()
    opt = input("\n\t\tEnter your selection:")
    #Asking for which measurement
    if(opt == "1"):
        while(True):
            dismenu()
            #Printing the distance menu if Distance is selected
            opt1 = input("\n\t\tEnter your selection:")
            #Asking for which unit
            if(opt1 == "1"):
                met = acceptno("Enter no. of metres:")
                f = f_conv.m2feet(met)
                mil = f_conv.m2mile(met)
                yar = f_conv.m2yard(met)
                #Using the functions in the module to convert
                printreport("meter", met, ' feet', f, ' miles', mil, ' yards', yar)
                #Printing a report if the unit given is metres
            elif(opt1 == "2"):
                f = acceptno("\nEnter no. of feet:")
                met = f_conv.f2metre(f)
                mil = f_conv.f2mile(f)
                yar = f_conv.f2yard(f)
                #Using the functions in the module to convert
                printreport("feet", f, ' meter', met, ' miles', mil, ' yards', yar)
                #Printing a report if the unit given is feet
            elif(opt1 == "3"):
                mil = acceptno("\nEnter no. of miles:")
                met = f_conv.mil2metre(mil)
                f = f_conv.mil2feet(mil)
                yar = f_conv.mil2yard(mil)
                #Using the functions in the module to convert
                printreport("miles", mil, ' meter', met, ' feet', f, ' yards', yar)
                #Printing a report if the unit given is miles
            elif(opt1 == "4"):
                yar = acceptno("\nEnter no. of feet:")
                met = f_conv.yartometre(yar)
                f = f_conv.yartofeet(yar)
                mil = f_conv.yartomile(yar)
                printreport('yard(s)', yar, 'metre(s)',met, 'feet', f, 'mile(s)', mil)
            elif(opt1 == "5"):
                break
                print("\n"*30)
            else:
                print("Invalid input")
                print("\n"*30)
    elif(opt == "2"):
        while(True):
            weimenu()
            #Printing the given menu using the f(x) created before for the weights menu
            opt3 = input("\n\t\tEnter your selection:")
            #Asking for which unit
            if(opt3 == "1"):
                kg = acceptno("\nEnter no. of kilograms:")
                #Asking for no. of kg
                poun = f_conv.kgtopound(kg)
                oun = f_conv.kgtoounce(kg)
                #Using the functions is f_conv to convert
                printreport('kilograms(s)', kg, 'pound(s)',poun, 'ounce(s)', oun, 'None', 0)
                #Printing a report for the unit kilograms
            elif(opt3 == "2"):
                oun = acceptno("\nEnter no. of ounces:")
                #Asking no. of oz
                poun = f_conv.ountopound(oun)
                kg = f_conv.ountokg(oun)
                #Using the functions in f_conv to convert
                printreport('ounce(s)', oun, 'pound(s)',poun, 'kilograms(s)', kg, 'None', 0)
                #Printing a report if the given unit oz

            elif(opt3 == "3"):
                poun = acceptno("\nEnter no. of pounds:")
                #Asking for no. of pounds                
                kg = f_conv.pountokg(poun)
                oun = f_conv.pountoonce(poun)
                #Using the functions in f_conv to convert
                printreport('pound(s)', poun, 'ounce(s)',oun, 'kilograms(s)', kg, 'None', 0)
                #Printing the report if the given unit is pounds

            elif(opt2 == "4"):
                break
                print("\n"*30)
            else:9
                print("Invalid input")
                print("\n"*30)
    elif(opt == "3"):
        while(True):
            temenu()
            opt2 = input("\n\t\tEnter your selection:")
            if(opt2 == "1"):
                C = acceptno("Enter no. degree celcius:")
                K = f_conv.CtoK(C)
                F = f_conv.CtoF(C)
                printreport('Degree Celcius',C , 'Degree Farenheit', F,'Degree Kelvin',K , 'None', 0)
            elif(opt2 == "2"):
                F = acceptno("Enter no. of degree Farienheit:")
                C = f_conv.FtoC(F)
                K = f_conv.FtoK(F)
                printreport('Degree Farenheit',F , 'Degree Celcius', C,'Degree Kelvin',K , 'None', 0)
            elif(opt2 == "3"):
                K = acceptno("Enter no. of degree Kelvin:")
                F = f_conv.KtoF(K)
                C = f_conv.KtoC(K)
                printreport('Degree Kelvin',K , 'Degree Farenheit', F,'Degree Celcius',C , 'None', 0)
               
            elif(opt2 == "4"):
                break
                print("\n"*30)
            else:
                print("Invalid input")
                print("\n"*30)
    elif(opt == "4"):
        exit()
    else:
        print("Invalid Input")


            
                
            














            
        
        
        
                   
        
    
    
    
