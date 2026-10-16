while True:
    print("=== CLI CALCULATOR ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    action = input("Enter your choice (1-5):")
    if action not in ["1", "2", "3", "4", "5"]:
        print("Invalid Action!!!")
        continue
        
    if action == "5":
        print("Goodbye!!!")
        break
    
    try:
        first = float(input("Enter first number:"))
        second = float(input("Enter second number"))
    except ValueError:
        print("Enter a valid number!!!")
        continue

    if action == "1":
        print(first + second)

    elif action == "2":
        print(first - second)

    elif action == "3":
        print(first * second)

    elif action == "4":
        if second != 0:
            print(first / second)
        else:

            print("Error: Cannot divide by zero")
