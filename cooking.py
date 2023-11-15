''''
This cood will figer out how long it will take to cook your turcky useing what type of cooking and how heavy your turky is
'''
#ask what type of cooking
typeOfCook=input("How do you what to cook your turcky (oven roasted or boilled, grilled, smoked or fryed): ")
#ask how may pound the turky is
pound=float(input("How heavy is your turck(in pounds): "))
# lets the user do it agen
while True:
    #breaks off the user to the two forms of cooking that the program lest
    if typeOfCook == "oven roasted":
        # the 14 is the avegr cooking time per pound
        pound=pound*14
        print("it will take"+ str(pound)+ "minets")

    #this is for boilled
    elif typeOfCook == "boilled":
        #takes ruffly 3.75 minnets per pound of bird
        pound=pound*3.75
        print("when the oil is ready it will take"+str(pound)+"minets")

    elif typeOfCook == "grilled":
        #takes ruffly 12 minnets per pound of bird
        pound=pound*12
        print("when the grille is ready it will take"+str(pound)+"minets")


    elif typeOfCook == "smoked":
        #takes ruffly 35 minets per pound of bird
        pound=pound*35
        print("when the smoker is ready it will take"+str(pound)+"minets")


    elif typeOfCook == "fryed":
        #takes ruffly 3.5 minnets per pound of bird
        pound=pound*3.5
        print("when the fryer is ready it will take"+str(pound)+"minets")


    #lets the user to use a differt type of cooking
    else:
        print("I do not know how to cook a turcky like that. sorry")
        
        #ask the user if you need stop or continu
        fin=input("Are you done or not")
        if fin == "yes":
            break
        #ask the question agen
        typeOfCook=input("How do you what to cook your turcky (oven roasted or boilled): ")
        pound=float(input("How heavy is your turck(in pounds): "))

    #this asks them if they need a timer or not    
    timer=input("Do you need a timer for the turcky(yess,no): ")
    if timer=="yes":
        print("chhc")
    else:
        break
print("have a happy thanksgiving :)")
print("if you missed up or the program did you can relod the page")