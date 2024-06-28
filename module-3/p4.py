# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

# Imports
from random import random


# Main entry point
def main(**args):
    """
        Generates a random decimal between 1 and 10
        and prints it with 2 d.p. accuracy.
    """
    rand = random() * 10
    print(round(rand, 2))  # rounds to 2 d.p.


# Only execute when run
if __name__ == "__main__":
    main()
