# part - 1 [From range n to m, print all the numbers divisible by 5 and 7 both]
n = int(input("Enter the first number for the range : "))
m = int(input("Enter the second number for the range : "))
for i in range(n, m , 1):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=' ')


# part - 2  [Find the sum of the series 2 +22 + 222 + 2222 + .. n terms]
number_of_terms = 5
x = 1
total = 0
for i in range(number_of_terms):
#    print('2'*x, end=' ')
    a = int('2'*x)
    x = x + 1
    total = total + a
    print(total) 


# part - 3  [Take integer inputs from user until he/she presses q. Print the sum of all numbers.] 
total = 0
while True:
    user_input=str(input('Enter the number or press q to quit : ')) 
    if user_input == 'q':
        break
    total += int(a) 
print("Total : ",total)


# part - 4 [Write a loop to find the factorial of any number]
number = int(input("Enter the number for the factorial : "))
factorial = 1
a = 1
while a <= number:
	factorial = factorial * a
	a = a + 1
print("Factorial :",factorial)