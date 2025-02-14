import random


print("Welcome to 🦁 Fun Animal Challenge 🐱")
#List of animals
animal_name = ["lion","cat","mouse"]

computer_choice = random.choice(animal_name)

user_choice = input(f"Choose your animal: {animal_name}").lower()

if computer_choice == user_choice :
    print(f"It's a Draw! You both chose {computer_choice}")
elif user_choice == animal_name[0] and computer_choice == animal_name[1] :
    print(f"You Win! Your {user_choice} 🦁 beats the computer's  {computer_choice} 🐱 ")
    if user_choice == animal_name[0] and computer_choice == animal_name[2]:
        print(f"You Win! Your {user_choice} 🦁 beats the computer's  {computer_choice} 🐭 ")
elif user_choice == animal_name[1] and  computer_choice == animal_name[0] :
    print(f"You Lose! The computer's {computer_choice} 🦁 beats your {user_choice} 🐱 ")
    if user_choice == animal_name[1] and  computer_choice == animal_name[2] :
        print(f"You Win! Your {user_choice} 🐱 beats the computer's  {computer_choice} 🐭 ")
elif user_choice == animal_name[2] and  computer_choice == animal_name[0] :
    print(f"You Lose! The computer's {computer_choice} 🦁 beats your {user_choice} 🐭 ")
    if user_choice == animal_name[2] and  computer_choice == animal_name[1] :
        print(f"You Lose! The computer's {computer_choice} 🐱 beats your {user_choice} 🐭 ")




