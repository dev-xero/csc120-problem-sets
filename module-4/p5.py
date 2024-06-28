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
        Generates 50 random numbers such that the first number
        is between 1 - 2, second is between 1 - 3 and nth is 
        between 1 - n+1.
    """
    for i in range(1, 51):
        rand = randint(1, i+1)
        print(f"Gen {i}: {rand}")


# Only execute when run
if __name__ == "__main__":
    main()
