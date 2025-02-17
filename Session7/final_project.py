import random

funny_comments = [
    "What the hell baba jan!! Guesset wrooooong bod! 😂",
    "Bro, are you even trying?!! 🤨",
    "In guess ghalat mahshariiii! To maghzet che khabare? 👀",
    "Man daram ghargh misham 😭 plzzzz guess right!",
    "Baba ye khoorde be khodet biya 😩",
    "Ajab badbakhtam man!!!! agha dige mishe guess dorost bezani?!! 😵‍💫"
]

word_list = ["octopus", "whale", "dolphin", "shark", "jellyfish"]
chosen_word = random.choice(word_list)
num_lives = 5
place_holder = "-" * len(chosen_word)
correct_letter = []

print("🐠 Maahi badbakhti ke bayad nejaat bedi! \n")
print(place_holder)

game_over = False
while not game_over:
    print("\n🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟🐟")
    print(f"🚨 You have {num_lives} / 5 lives left. Maahi dare zendegisho az dast mide! 😭")

    user_guess = input("🎯 Guess a letter: \n").lower()

    # 🤦‍♂️ Check if the letter was guessed before
    if user_guess in correct_letter:
        print(f"🤨 Baba in '{user_guess}' ro ghablan gofti!! Az badi right guess kon! 🙃")
        print("📢 Maahi: Boro dars bekhoon, ye harfo 2 bar nagu baba! 😒")
        continue  # Be round badi bere, na ye harf ro dobare check kone!

    # 🔍 Check if the guessed letter is in the word
    if user_guess in chosen_word:
        print("✅ Oooof boooos behet baba 🥳, dige be zoodi rahatam mikoni!\n")
        print("📢 Maahi: Aghaaaa damet garm! 🥳")
        correct_letter.append(user_guess)
    else:
        num_lives -= 1
        print(f"❌ {random.choice(funny_comments)}")
        print("📢 Maahi: Baba yaaroooo zoodtar nejatam bede digeee! 😭")

    # 🎭 Update the display word
    display = ""
    for lett in chosen_word:
        if lett in correct_letter:
            display += lett
        else:
            display += "-"

    print(f"🌊 Current Word: {display}")  # Be jaye aval, inja print shod

    # 🏆 Check for win condition
    if "-" not in display:
        game_over = True
        print(f"🎉 Yessss! You win! The word was {chosen_word}.")
        print("📢 Maahi: Baba man heyyy migam to ba hoshiiii, cleverrrrr! 😆")

    # 💀 Check for losing condition
    if num_lives == 0:
        game_over = True
        print(f"💀 Game Over! The word was {chosen_word}. Maahi raft be ... 😭")
        print("📢 Maahi: Man ke raftam! Vali bad bakht on fishe badi ke toooooo gharare nejatesh bedi?! 💀💀💀")
