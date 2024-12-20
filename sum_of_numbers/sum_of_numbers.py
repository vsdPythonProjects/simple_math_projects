def get_sum_of_two_numbers():
    """
    Prompts the user to input two numbers and prints their sum.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
        return result
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None
