

grade1 = float(input("Enter grade: "))
unit1 = int(input("Enter number of units: "))

grade2 = float(input("Enter grade: "))
unit2 = int(input("Enter number of units: "))

grade3 = float(input("Enter grade: "))
unit3 = int(input("Enter number of units: "))

grade4 = float(input("Enter grade: "))
unit4 = int(input("Enter number of units: "))

grade5 = float(input("Enter grade: "))
unit5 = int(input("Enter number of units: "))

gradeAdd = (grade1 + grade2 + grade3 + grade4 + grade5)

gwa = gradeAdd/5

print("Your GWA is: ", gwa)

if grade1 == 5.00 or grade2 == 5.00 or grade3 == 5.00 or grade4  == 5.00 or grade5 == 5.00:
    print("you have a grade of 5 which disqualifies you from getting latin honors")

else:
    if gwa <= 1.20:
        print("Summa Cum Laude")
    elif gwa <= 1.45 and gwa > 1.20:
        print("Magna Cum Laude")
    elif  gwa <= 1.75 and gwa > 1.45:
        print("Cum Laude")


