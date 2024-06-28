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
        Prints a list of integers and their squares from 1 - 20.
    """
    for i in range(1, 21):
        print(i, i**2, sep="------")


# Only execute when run
if __name__ == "__main__":
    main()
