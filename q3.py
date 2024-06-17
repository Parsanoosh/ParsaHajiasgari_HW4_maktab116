def is_armstrong(number):
    """
    Checks if a number is an Armstrong number.
    """
    num_str = str(number)
    n = len(num_str)
    digit_sum = sum(int(digit) ** n for digit in num_str)
    return digit_sum == number


user_input = int(input("Enter a number: "))
if is_armstrong(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
