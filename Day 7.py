name = str(input("Enter your name : "))
email = str(input("Enter your email : "))

courses = ['Python', 'Java', 'Compiler Design', 'React JS', 'Finearts', 'Machine learning', 'Ruby', 'Database managemnet systems', 'Swift programming', 'Flutter framework', 'Oracle SQL', 'Artificial Intelligence']
for i in range(len(courses)):
    print('{}. {}'.format(i, courses[i]))
my_courses = int(input("Enter the course you want(number): "))
user_details = {
  'User_ID': 101,
  'Name': name,
  'Email': email,
  'My Courses': [courses[my_courses]]
}
print(user_details)
new_course = int(input("Enter the other course you want to enroll for(number): "))
user_details['My Courses'].append(courses[new_course])
print(user_details)
edit = input("Do you want to edit you profile (y/n): ")
if edit == 'n':
    print("You have enrolled for {}".format(user_details['My Courses']))
    exit()
elif edit == 'y':
    new_name = input("Enter your new name : ")
    user_details['Name'] = new_name 
    new_email = input("Enter your new email : ")
    user_details['Email'] = new_email 
    print(user_details)