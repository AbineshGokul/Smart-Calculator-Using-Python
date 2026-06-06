history = []

ops = {
    "add": 0,
    "sub": 0,
    "mul": 0,
    "div": 0
}


def calc(a, b, op):
    if op == '+':
        ops["add"] += 1
        return a + b

    elif op == '-':
        ops["sub"] += 1
        return a - b

    elif op == '*':
        ops["mul"] += 1
        return a * b

    elif op == '/':
        ops["div"] += 1
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    else:
        return "Invalid Operator"


while True:
    print("\n1. Calculator")
    print("2. History")
    print("3. Analysis")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")

            result = calc(a, b, op)
            print("Result:", result)

            history.append(f"{a} {op} {b} = {result}")

        except ValueError:
            print("Please enter valid numbers.")

    elif ch == '2':
        if history:
            print("\nCalculation History:")
            for h in history:
                print(h)
        else:
            print("No history available.")

    elif ch == '3':
        print("\nOperation Analysis:")
        for k, v in ops.items():
            print(f"{k} used {v} times")

    elif ch == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
