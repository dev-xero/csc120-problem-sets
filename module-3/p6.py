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
        Prints even numbers from 100 - 2 in reverse.
    """
    for i in range(100, 0, -2):
        print(i, end=" ")


# Only execute if run
if __name__ == "__main__":
    main()
