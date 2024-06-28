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
        Generates a random number `n` between 1 and 10
        and prints your name `n` times.

        Note: You pass in your name through the main function call.
    """
    name = args.get("name") or "user"
    n = randint(1, 10)

    print(f"{name} "*n)


# Only execute when run
if __name__ == "__main__":
    main(name="xero")
