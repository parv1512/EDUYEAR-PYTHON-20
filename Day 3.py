# part - 1 [AGE CALCULATOR : calculate Age of a person]
year = int(input("Enter the year of birth : "))
current_year = 2021
age = current_year-year
print(age)


# part - 2 [Simple Calculator]
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("Addition : {} + {} = {} \n".format(a, b, a + b))
print("Subtraction : {} - {} = {} \n".format(a, b, a - b))
print("Multiplication : {} * {} = {} \n".format(a, b, a * b))
print("Decimal Division : {} / {} = {} \n".format(a, b, a / b))
print("Floor Division : {} // {} = {} \n".format(a, b, a // b))
print("Remainder : {} % {} = {} \n".format(a, b, a % b))
print("Power : {} ** {} = {} \n".format(a, b, a ** b)) 


# part - 3 [use string functions to count the occurrence of 'y' in a word given by user ]
word = str(input("Enter the word : "))
count = word.count('y')
print(count)

# part - 4 [take input of a string and print it's even indexed characters]
string = str(input("Enter the string : "))
print(string[1::2])