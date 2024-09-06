logo = """

 __        __   __        __   __   __      __   ___       ___  __       ___  __   __  
|__)  /\  /__` /__` |  | /  \ |__) |  \    / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
|    /~~\ .__/ .__/ |/\| \__/ |  \ |__/    \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \ 


"""
print(logo)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']    

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Easy  letters+symbols+numbers
# hard  shuffle

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in you password?\n"))

password = ""
for char in range(1, nr_letters + 1):
    # random_char = random.choice(letters)
    # password += random_char
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)