#Code By : Hritik Garg <4921852>

# Reversing a alphabetic string.
# Ignoring Numeric And Alphanumeric String.

#Method 0
string = input("Enter the String : ")
print ("Entered String : " + string)
print(string.reverse())

#Method 1
def reverse(str):
  print(''.join(reversed(str)));
reverse('Hello World');

#Method 2
def reverse(str):
  reversed = '';
  for char in str:
    reversed = char + reversed;
  print(reversed);
reverse('Hello World');

#Method 3
def reverse(str):
    new_strings = []
    index = len(str)
    while index:
        index -= 1                       
        new_strings.append(str[index])
    print(''.join(new_strings))
reverse('Hello World');

#Method 4
def reverse(str):
  print(str[::-1]);
reverse('Hello World');
