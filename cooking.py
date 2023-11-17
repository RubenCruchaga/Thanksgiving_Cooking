''''
This cood will figer out how long it will take to cook your turcky useing what type of cooking and how heavy your turky is
'''
while True:
    #this less use use a for loop
    turkyNum=int(input("How maney turckey are you cooking: "))
    for i in range (turkyNum):
        turcky=1
        #ask what type of cooking
        typeOfCook=input("How do you what to cook your turcky (oven roasted or boilled, grilled, smoked or fryed): ")
        #ask how may pound the turky is
        pound=float(input("How heavy is your turck(in pounds): "))
    # lets the user do it agen
        #breaks off the user to the two forms of cooking that the program lest
        if typeOfCook == "oven roasted":
            # the 14 is the avegr cooking time per pound
            pound=pound*14
            print("it will take "+ str(pound)+ " minets")
            
        #this is for boilled
        elif typeOfCook == "boilled":
            #takes ruffly 3.75 minnets per pound of bird
            pound=pound*3.75

        elif typeOfCook == "grilled":
            #takes ruffly 12 minnets per pound of bird
            pound=pound*12

        elif typeOfCook == "smoked":
            #takes ruffly 35 minets per pound of bird
            pound=pound*35

        elif typeOfCook == "fryed":
            #takes ruffly 3.5 minnets per pound of bird
            pound=pound*3.5

        print(str(pound)+" minets, for your "+str(turcky)+ " turcky")
        #this keeps the  pound information
        totalPound=0
        totalPound=totalPound+pound
        turcky=turcky + 1
    print(str(totalPound)+" minets for your turckys")

    print("have a happy thanksgiving :)")
    agen=input("Do you what to do this agen(y,n)")
    if agen == "n":
        break
print("the program is over")
