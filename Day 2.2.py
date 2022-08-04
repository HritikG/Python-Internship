#Code By : Hritik Garg <4921852>
# Reversing a alphabetic string.
# Ignoring Numeric And Alphanumeric String.

#Take input as a list define a Function return the values as return x[::-1].

#Method 1

inputstr = input("Enter the String : ")
print ("Entered String is : " + inputstr)
#Syntax :- inputstr[start:end:step]

if inputstr.isnumeric():
    print ("Nothing") 
else:
    print(inputstr[-1::-1])



# Method 2

str = input("Enter the string ---> ") ; "Ooops!! Can't reverse 'cause the string contains numeric values" if str.isnumeric() else str[::-1]
