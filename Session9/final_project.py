

print("🏋️‍♂️ Weight Loss Challenge 💪")
print("📢 Every month, the gym rewards the participant with the highest weight loss! ")
print("🏆 Are you ready to break the record and win?! 😍  ")

def find_winner(user_dic):
    max_loss = 0
    winner_name = ""
    for name in user_dic:
        weight = user_dic[name]
        final_lose_weight = weight[0] - weight[1]
        if final_lose_weight > max_loss:
            max_loss = final_lose_weight
            winner_name = name
    print(user_dic[winner_name])
    print(f"🏆 **Current Leader:** {winner_name}   \n"
          f"⚖️ Initial weight (kg): {user_dic[winner_name][0]} and 📉 Current weight (kg): {user_dic[winner_name][1]} \n "
          f" with **{max_loss} kg lost!** 🎉 " )


user_information = {}
should_continue = True
while should_continue :
    user_name = input("👤 Enter your name:")
    initial_weight = int(input("⚖️ Initial weight (kg):"))
    current_weight = int(input("📉 Current weight (kg):"))

    user_information[user_name] = initial_weight, current_weight  #user_information = { 'mali': (56, 43) , 'pari': (57, 50)}
    other_user =  input("Are there any other participants? Type 'yes' or 'no'.\n")
    if other_user == "yes":
        print("\n" * 50 )
    else:
        should_continue = False
        find_winner(user_information)













