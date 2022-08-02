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

#Method2
result1 = (x+y) ** 2

#Printing the result variable to get the desired answer.

print (result)
print (result1)