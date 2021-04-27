# part - 1 [Give all the index values of vowels.]
first_str = "Python-Programming"
temp = []
for vowels in range(len(first_str)):
    if first_str[vowels] in "aeiou":
        temp.append(vowels)
print(temp)


# part - 2 [Reverse the words of a string]
string = 'hello world happy birthday'
split_string = string.split(' ') 
reversed_string = reversed(split_string)
final_string = ' '.join(reversed_string) 
print(final_string)

# part - 3 [Remove duplicate elemnts without using set()] 
test_list = [1, 3, 5, 6, 3, 5, 6, 1, 9, 8, 6, 9]
temp = []
[temp.append(x) for x in test_list if x not in temp]
print (str(temp))