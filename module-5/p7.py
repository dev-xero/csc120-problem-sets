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
        Prompts the user for two numbers and prints
        "close" if they're withing 0.001 from each other,
        "not close" otherwise.
    """
    num1 = float(eval(input("> Enter num1: ")))
    num2 = float(eval(input("> Enter num2: ")))
    abs_diff = abs(num1 - num2)

    if abs_diff < 0.001:
        print("- These numbers are close.")
    
    else:
        print("- These numbers are not extremely close.")


# Only execute when run
if __name__ == "__main__":
    main()
