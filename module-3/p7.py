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
        Prints the sequence "AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG"
        using only four loops, as per requirements.
    """
    # AAAAAAAAAA segment
    for _ in range(10):
        print('A', end="")

    # BBBBBBB segment
    for _ in range(7):
        print('B', end="")

    # CDCDCDCD segment
    for _ in range(4):
        print("CD", end="")

    # EFFFFFFG segment
    for i in range(8):
        if i == 0:
            print('E', end="")

        elif i == 7:
            print('G', end="")

        else:
            print('F', end="")


# Only execute when run
if __name__ == "__main__":
    main()
