
print("Welcome to 🚗 Driving Test.")
print("Will You Get Your License? 🚦")

test_1 = input("1️⃣ You are behind the wheel. The traffic light turns yellow. What do you do? (Wait\Speed up)").lower()
if test_1 == "wait" :
    print("(You slow down and stop) ✅ Ready for next Question:")
    test_2 = input("2️⃣ You approach an intersection. A pedestrian is crossing the street. What do you do? (Stop\Keep going)").lower()
    if test_2 == "Stop" :
        print(" (You let them pass) ✅")
        test_3 = input("3️⃣ At the end of the test, On a slippery road, how much distance should you keep from the car ahead?(More than usual\Same as usual) ").lower()
        if test_3 == "More than usual" :
            print("✅ You passed the test! 🎉")
            print("you get your driving license! 🚗💨")
        else:
            print("❌ Failed! 😢")
    else:
        print(" (You don’t stop) ❌ Failed")
else:
    print("(You rush through) ❌ Failed")


