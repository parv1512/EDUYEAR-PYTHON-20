# part -1 [input : n = 16 ]
n = int(input("Enter the number : "))
def rec(n):
    if n == -4:
        print(-4)
    else:
        print(n)
        rec(n-5)
        print(n)
rec(n)


# part - 2 [input : n = 10 ]
n = int(input("Enter the number : "))
def rec(n):
    if n == 0:
        print(0)
    else:
        print(n)
        rec(n-5)
        print(n)
rec(n)