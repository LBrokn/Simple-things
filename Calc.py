#Test Calc
number1 = int(input("1st number:"))
number2 = int(input("2nd number:"))
print("Plus : +")
print("Minus: -")
print("Times: *")
print("Divided by: /")
calc= input("Which operation do u want to use on this calc?: ")
result= 0
#If zone
if (calc == "+"):
    result = number1 + number2
elif (calc == "-"):
    result = number1 - number2
elif (calc == "*"):
    result = number1 * number2
elif (calc == "/"):
    result = number1 / number2
else:
    print(":There is some error o//. Reboot the program.")

print(number1, calc, number2, "=",result)
