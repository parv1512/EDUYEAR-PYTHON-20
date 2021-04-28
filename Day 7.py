courses = ['Python', 'Java', 'Compiler Design', 'React JS', 'Finearts', 'Machine learning', 'Ruby', 'Database managemnet systems', 'Swift programming', 'Flutter framework', 'Oracle SQL', 'Artificial Intelligence']

name = input('Enter your name: ')
email = input('Enter your email: ')

user = {
    'user_id': 101,
    'name': name,
    'email': email,
    'courses': []
}

while True:
    menu = ['All courses', 'My courses', 'Edit your profile']
    print('\n*** Main Menu ***')
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    print('0. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 0:
        print('\nThank you for visiting!!')
        exit(1)
    if choice == 1:
        curr_courses = list(set(courses) - set(user['courses']))
        print('\n*** All Courses ***')
        for i in range(len(curr_courses)):
            print(f"{i+1}. {curr_courses[i]}")
        ch = int(input('\nEnter your choice: '))
        user['courses'].append(curr_courses[ch-1])
        print(f'\nThanks for enrolling in {curr_courses[ch-1]}\nEnjoy learning!!')

    elif choice == 2:
        print('\n*** My Courses ***')
        c = user['courses']
        for i in range(len(c)):
            print(f"{i+1}. {c[i]}")

    elif choice == 3:
        name_n = input('Enter your new name: ')
        email_n = input('Enter your new email: ')

        user['name'] = name_n
        user['email'] = email_n

        print('\n*** Your details ***')
        print(f'User Name : {user["name"]}')
        print(f"User Email : {user['email']}")