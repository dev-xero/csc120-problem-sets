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
        Prints a list of squares from 1 to 100 and counts
        how many of these squares end in a 4 and 9.
    """
    count_4 = 0
    count_9 = 0

    for num in range(1, 11):
        sq = num**2
        # Stringify and check the last digit
        if str(sq)[-1] == '4':
            count_4 += 1

        elif str(sq)[-1] == '9':
            count_9 += 1

        print(sq, end=" ")

    print("\n\nSquares ending with 4:", count_4)
    print("Squares ending with 9:", count_9)


# Only execute when run
if __name__ == "__main__":
    main()
