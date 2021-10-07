# Project Name: Faulty calculator

"""
It will incorrectly calculate following 3 calculations:
45*3 = 555
56+9 = 77
56/6 = 4
"""

num1 = int(input("Enter First number:: "))
num2 = int(input("Enter Second number:: "))
oper = input("Choose your operation from +,*,/:: ")

if oper == "+":
    print(num1+num2)
elif oper =="*":
    print(num1*num2)
elif oper =="/":
    print(num1/num2)
elif oper == "*" and num1 == 45 and num2 == 3:
    print("555")
elif oper == "+" and num1 == 56 and num2 == 9:
    print("77")
elif oper == "/" and num1 == 56 and num2 == 6:
    print("4")
