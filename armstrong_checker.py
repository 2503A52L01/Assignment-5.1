def is_armstrong_number(num):
    """
    Check if a number is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to easily iterate over digits
    digits = str(num)
    num_digits = len(digits)  # Get the number of digits

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)

    # Check if the calculated sum is equal to the original number
    return armstrong_sum == num

# Example usage
if __name__ == "__main__":
    test_number = 153
    if is_armstrong_number(test_number):
        print(f"{test_number} is an Armstrong number.")
    else:
        print(f"{test_number} is not an Armstrong number.")
