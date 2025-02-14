import random


print("Welcome to 🦁 Fun Animal Challenge 🐱")
#List of animals
animal_name = ["lion","cat","mouse"]

computer_choice = random.randint(0 , 2)
user_choice = int(input(f"Choose your animal: Type 0 for Lion🦁 , 1 for Cat🐱 or type 2 for Mouse🐭 "))

if computer_choice == user_choice :
    print(f"It's a Draw! You both chose {animal_name[computer_choice]}")
elif user_choice == 0  and computer_choice == 1 :
    print(f"You Win! Your {user_choice} 🦁 beats the computer's  {computer_choice} 🐱 ")
    if user_choice == 0 and computer_choice == 2:
        print(f"You Win! Your {user_choice} 🦁 beats the computer's  {computer_choice} 🐭 ")
elif user_choice == 1 and  computer_choice == 0 :
    print(f"You Lose! The computer's {computer_choice} 🦁 beats your {user_choice} 🐱 ")
    if user_choice == 1 and  computer_choice == 2 :
        print(f"You Win! Your {user_choice} 🐱 beats the computer's  {computer_choice} 🐭 ")
elif user_choice == 2 and  computer_choice == 0 :
    print(f"You Lose! The computer's {computer_choice} 🦁 beats your {user_choice} 🐭 ")
    if user_choice == 2 and  computer_choice == 1 :
        print(f"You Lose! The computer's {computer_choice} 🐱 beats your {user_choice} 🐭 ")




