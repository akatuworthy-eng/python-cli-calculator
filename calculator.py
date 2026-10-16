while True:
    print("=== CLI CALCULATOR ===")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("q : Quit")

    action = input("Enter your choice (+, -, *, /, q):").strip()
    if action not in ["+", "-", "*", "/", "q"]:
        print("Invalid Action!!!")
        continue
        
    if action == "q":
        print("Goodbye!!!")
        break
    
    try:
        first = float(input("Enter first number:"))
        second = float(input("Enter second number"))
    except ValueError:
        print("Enter a valid number!!!")
        continue

    if action == "+":
        print(first + second)

    elif action == "-":
        print(first - second)

    elif action == "*":
        print(first * second)

    elif action == "/":
        if second != 0:
            print(first / second)
        else:

            print("Error: Cannot divide by zero")
