# part - 1 [Take a number from user and check whether it is prime or not]
def find_pm():
    user_number = int(input("Enter the number : "))
    count = 0
    for i in range(2, user_number+1):
        if user_number % i == 0:
            count += 1
            break
    if count == 0:
        print('Prime Number')
    else:
        print('Not a Prime Number')
find_pm()

# part -2 [Write a function to print n factorial.]
def factorial():
    n=int(input("Enter a number : "))
    factorial = 1
    a = 1
    while a <= n:
        factorial = factorial * a
        a = a + 1
    print(factorial)
factorial()