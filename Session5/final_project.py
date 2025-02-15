import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['£','^','?','!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Username 😎 Generator!\n")
num_letters = int(input("How many letters would you like in your username?\n"))
num_symbols = int(input("How many symbols would you like in your username?\n"))
num_numbers = int(input("How many numbers would you like in your username?\n"))

"""

user_name = ""
for l in range(0,num_letters):
    user_name += random.choice(letters)

for n in range(0, num_numbers):
    user_name += random.choice(numbers)

for s in range(0, num_symbols):
    user_name += random.choice(symbols)

print(user_name)

"""

user_name = []
for l in range(0,num_letters):
    user_name.append(random.choice(letters))

for n in range(0, num_numbers):
    user_name.append(random.choice(numbers))

for s in range(0, num_symbols):
    user_name.append(random.choice(symbols))




random.shuffle(user_name)

# convert list to string

#final_username = "".join(user_name)
final_username = ""
for element in user_name:
    final_username += element


print(f"Your generated username is:  {final_username}")



