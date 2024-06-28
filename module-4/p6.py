# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------


# Main entry point
def main(**args):
    """
        Prompts the user to enter two numbers, `x` and `y` and 
        computes the absolute difference and sum of the two.
    """
    x = float(input("> Enter number x: "))
    y = float(input("> Enter number y: "))

    print("- Absolute difference:", abs(x-y))
    print("- Sum:", x + y)


# Only execute when run
if __name__ == "__main__":
    main()
