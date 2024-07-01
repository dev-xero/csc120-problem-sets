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
        how many of these squares end in a 1.
    """
    count = 0
    for num in range(1, 11):
        sq = num**2
        # Stringify and check the last digit
        if str(sq)[-1] == '1':
            count += 1

        print(sq, end=" ")

    print("\nNumbers ending with 1:", count)


# Only execute when run
if __name__ == "__main__":
    main()
