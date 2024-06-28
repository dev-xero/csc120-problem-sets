# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

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


# Only execute when run
if __name__ == "__main__":
    main()
