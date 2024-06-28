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
        Prints the numbers 8 - 89 with a gap of 3.
    """
    for i in range(8, 90, 3):
        print(i, end=" ")


# Only execute if run
if __name__ == "__main__":
    main()
