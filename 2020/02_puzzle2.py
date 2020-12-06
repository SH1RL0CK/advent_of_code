with open('02_input.txt', 'r') as file:
    passwords = file.readlines()

valid_passwords = 0

for password_elements in passwords:
    password_elements = password_elements.split('-')
    position1 = int(password_elements[0]) -1
    password_elements = password_elements[1].split(' ')
    position2 = int(password_elements[0]) -1
    letter = password_elements[1][0]
    password = password_elements[2].replace('\n', '')
    if (password[position1] == letter) != (password[position2] == letter):
        valid_passwords += 1

print(valid_passwords)