def f(x: int) -> int:
    doubled = 2 * x

    # So if the doubled number is greater than 9, I subtract 9 from it.
    return doubled if doubled < 10 else doubled - 9

def is_credit_card(card: str) -> bool:
    """
    A function that checks if a given Credit Card number is valid.
    :param card: str - The card number to check.
    :return: bool - True if the credit card number is valid, False otherwise.
    """

    if len(card) not in (16, 19):
        return False

    total = 0
    reverse_digits = card[::-1] # I reverse the digits of the card number because luhn algorithm read from right to left.


    for index, digit in enumerate(reverse_digits):
        num = int(digit) # I convert the char to an int.

        if index % 2 == 1:
            total += f(num)
        else:
            total += num

    return total % 10 == 0 # If the total is divisible by 10, then the Credit Card number is valid.
