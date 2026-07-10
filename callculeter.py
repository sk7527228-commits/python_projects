print("=" * 50)
print("          PYTHON SMART CALCULATOR")
print("=" * 50)
try:
    num1 = float(input("\nEnter First Number  : "))
    num2 = float(input("Enter Second Number : "))
    print("\nChoose an Operation")
    print("-" * 30)
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" %  : Modulus")
    print(" // : Floor Division")
    print(" ** : Power")
    print("-" * 30)
    operator = input("Enter Operator: ")
    if operator == "+":
        answer = num1 + num2
        print(f"\nResult: {num1} + {num2} = {answer}")
    elif operator == "-":
        answer = num1 - num2
        print(f"\nResult: {num1} - {num2} = {answer}")
    elif operator == "*":
        answer = num1 * num2
        print(f"\nResult: {num1} * {num2} = {answer}")
    elif operator == "/":
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            answer = num1 / num2
            print(f"\nResult: {num1} / {num2} = {answer}")
    elif operator == "%":
        if num2 == 0:
            print("\nError: Modulus by zero is not allowed.")
        else:
            answer = num1 % num2
            print(f"\nResult: {num1} % {num2} = {answer}")
    elif operator == "//":
        if num2 == 0:
            print("\nError: Floor Division by zero is not allowed.")
        else:
            answer = num1 // num2
            print(f"\nResult: {num1} // {num2} = {answer}")
    elif operator == "**":
        answer = num1 ** num2
        print(f"\nResult: {num1} ** {num2} = {answer}")
    else:
        print("\nInvalid Operator!")
except ValueError:
    print("\nPlease enter valid numbers only!")
print("\n" + "=" * 50)
print("      THANK YOU FOR USING MY CALCULATOR")
print("             HAVE A GREAT DAY")
print("=" * 50)