#Code By : Hritik Garg <4921852>

##To Find Square of a number.

#Taking Input From User
#Converting it into Int data type.
#Storing in variables x,y.

x = int(input("Enter the Value of x :- "))
y = int(input("Enter the Value of y :- "))

#New variable declared named result which stores the equation.

#Method1
result = (x + y) *(x + y)
#Printing the result
print (result)

#Method2
result1 = (x+y) ** 2
#Printing the result
print (result1)

#Method3
from math import pow
# input a number
digit = int(input("Enter an integer number: "))
# calculate square
square = int(pow(digit, 2))
# print
print(f"Square of {digit} is {square}")

