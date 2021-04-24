x = [1, 2,  6, 7, 121, 242, 100, 563, 747, 356, 8, 9, 10, 11, 12, 13, 14, 15]
#x = [1, 2, 3, 2, 1] # for part - 3

# part - 1 [Count even numbers and odd numbers]
count_even, count_odd = 0, 0
for num in x:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Count of even number : ", count_even)
print("Count of odd number : ", count_odd)


#part - 2 [max and min of the list]
x.sort()
print("The minimum number is :", x[0])
print("The maximum number is :", x[-1])


# part - 3 [Check whether the whole list is palindrome or not]
y = None
y = x
y = y[::-1]
if len(x)%2 == 0: #palindroms are always ODD in number
    print("NO")
elif y == x: # checking whether the reversed list of x is equal to the simple one
    print("YES")
else: # if the no. of items in the list is odd but it is not a palindrom .i.e the reversed and the non-reversed list is not equal
    print("NO")


# part - 4 [Print the numbers which are palindrome inside the list]
for item in x:
    num = str(item)
    if ("".join(reversed(num))==num):
        print(item)