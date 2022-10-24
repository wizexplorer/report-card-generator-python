def marks_entry():
    global eng,mat,sci,sst
    eng=int(input("Enter Marks of the student in English out of100\t\t: "))
    mat=int(input("Enter Marks of the student in Maths out of 100\t\t: "))
    sci=int(input("Enter Marks of the student in Science out of 100\t: "))
    sst=int(input("Enter Marks of the student in Social Science out of 100\t: "))
def grade():
    global total,percent,grade
    total=eng+mat+sci+sst
    percent=(total/4)
    if percent>85:
        grade = "A"
    elif percent < 85 and percent >= 75:
        grade = "B"
    elif percent < 75 and percent >= 50:
        grade = "C"
    elif percent > 30 and percent <= 50:
        grade = "D"
    elif percent <30:
        grade = "Reappear"
    print("Percentage and Grade has been calculated")
def report_card():
    print("\t\t   Report Card")
    print("-"*72)
    print("\t\n\t\tEnglish\t\t:",eng,"\n\t\tMaths\t\t:",mat,"\n\t\tScience\t\t:",sci,"\n\t\tSocial Science\t:",sst)
    print("\t\tPercentage\t:",percent)
    print("\t\tGrade\t\t:",grade)
print("|-------------------------EXPERIMENT NO.22-----------------------------|")
print("|            MENU DRIVEN PROGRAMME TO GET REPORT CARD                  |")
print("|----------------------------------------------------------------------|")
print("*"*72)
opti=int(input("1. Marks entry \n2.Calculate total and Grade \n3.Display report card \n4.EXIT\nYour Choice : "))
print("*"*72)
while opti!=4:
    if opti==1:
        marks_entry()
        print("*"*72)
        opti=int(input("1. Marks entry \n2.Calculate total and Grade \n3.Display report card \n4.EXIT\nYour Choice : "))
        print("*"*72)
        if opti==2:
            grade()
            print("*"*72)
            opti=int(input("1. Marks entry \n2.Calculate total and Grade \n3.Display report card \n4.EXIT\nYour Choice : "))
            print("-"*72)
            if opti==3:
                report_card()
            else:
                print("Calculate percentage and grade first")
        elif opti==3:
            print("Calculate grade and precentage first ")
        else:
            print("Not a valid option ")
    elif opti==2:
        print("Enter marks first")
    elif opti==3:
        print("Enter marks first")
    else:
        print("Not a valid option ")
    print("*"*72)
    opti=int(input("1. Marks entry \n2.Calculate total and Grade \n3.Display report card \n4.EXIT\nChoice:"))
    print("*"*80)
