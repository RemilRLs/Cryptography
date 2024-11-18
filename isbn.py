def is_valid_isbn13(isbn: str) -> bool:
    """
    A function that checks if a given ISBN-13 is valid.
    :param isbn: int - The ISBN-13 to check.
    :return: bool - True if the ISBN-13 is valid, False otherwise.
    """

    if(len(str(isbn)) != 13):
        return False

    total = 0

    for index, digit in enumerate(isbn):
        num = int(digit) # I convert the char to an int.

        if(index % 2 == 0):
            total += num
        else:
            total += num * 3

    return total % 10 == 0 # If the total is divisible by 10, then the ISBN-13 is valid.

isbn = "9783161481200"
print(is_valid_isbn13(isbn))