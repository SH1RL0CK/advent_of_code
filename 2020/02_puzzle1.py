with open('02_input.txt', 'r') as file:
    passwords = file.readlines()

valid_passwords = 0

for password_elements in passwords:
    password_elements = password_elements.split('-')
    min_times = int(password_elements[0])
    password_elements = password_elements[1].split(' ')
    max_times = int(password_elements[0])
    letter = password_elements[1][0]
    password = password_elements[2].replace('\n', '')
    number_of_letter = 0
    for l in password:
        if l == letter:
            number_of_letter += 1
    if number_of_letter >= min_times and number_of_letter <= max_times:
        valid_passwords += 1

print(valid_passwords)