operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Handle errors when input is 0
if operator == "/" and num2 == 0:
    print(f"Error: Cannot complete division by 0. Please try again.")
else:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2 
    else:
        print(f"{operator} is not valid.")
        result = None

if result is not None:
    print(round(result))