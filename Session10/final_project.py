def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "➕": add,
    "➖": subtract,
    "✖": multiply,
    "➗": divide,
}

def calculation():
    print("🧮 Welcome to the Calculator! 🧮")
    first_number = float(input("🔢 Enter the first number: "))
    continue_calculate = True
    while continue_calculate:
        print("\n📌 Available operations:")
        for operator in operations:
            print(operator, end="  ")
        print()
        user_operation = input("👉 Pick an operation: ")
        second_number = float(input("🔢 Enter the next number: "))
        result = round(operations[user_operation](first_number, second_number), 2)
        print(f"\n✅ Result: {first_number} {user_operation} {second_number} = {result} 🎉")
        should_continue = input(
            f"🔄 Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if should_continue == "y":
            first_number = result
        else:
            continue_calculate = False
            calculation()

calculation()

