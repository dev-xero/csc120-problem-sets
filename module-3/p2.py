# Imports
from random import randint


# Main entry point
def main(**args):
    """
        Generates a random number `x` in the range 1-50
        and a random number `y` in the range 2-5 and computes
        `x^y`
    """
    x = randint(1, 50)
    y = randint(2, 5)
    x_raised_to_y = x ** y

    print("- x:", x)
    print("- y:", y)
    print("- x^y:", x_raised_to_y)


if __name__ == "__main__":
    main()
