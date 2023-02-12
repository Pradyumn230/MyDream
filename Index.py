# Tax calculator
import sys

# Promot user to input the filling status

status = eval(input(
    "(0-Single filer, 1 marked jointly, \n)"+
    "Enter the filling status:"))


# promot the user to input the flexible income

income = eval(input("Enter the txable income:"))

# Compute tax
tax = 0

if status == 0:
    if income <= 8350:
        tax = income*0.10
    elif income <= 33950:
        tax = 8350*0.10 + (income - 8350)*0.15
    elif income <= 82250:
        tax = 8350*0.10 + (33950 - 8350)*0.15 + (income - 33950)*.25
    elif income <= 171550:
        tax = 8350*0.10 + (33950 - 8350)*0.15 +(82250-33950)*0.25 + (income - 82250)*0.28
    elif income <= 372950:
        tax = 8350*0.10 + (33950 - 8350)*0.15 +(82250-33950)*0.25 + (income - 82250)*0.28 + \
        (income - 171550)*0.33
    else:
        tax = 8350*0.10 + (33950 - 8350)*0.15 +(82250-33950)*0.25 + (income - 82250)*0.28 + \
        (income - 171550)*0.33  + (income - 372950)*0.28;
elif status == 1:
    print("Left as exercise:")    
elif status == 2:
    print("Left as exercise:")
elif status == 3:
    print("Left as exercise:")
else:
    print("Error: invalid status")
    sys.exit()

print("Tax is", format(tax, ".2f"))