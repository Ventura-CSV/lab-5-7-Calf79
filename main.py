
def splitlist(args):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    if not args:
        return None, []
    number=list(args)
    index=number.index(min(number))
    number[0], number[index] = number[index],number[0]
    return number[0],number[1:]
def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
