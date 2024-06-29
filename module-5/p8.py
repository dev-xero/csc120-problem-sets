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
        Prompts the use for a year and prints whether its
        a leap year or not.
        A year is a leap year if divisible by 4, but if
        divisible by 100, it must also be divisible by 400.
    """
    year = int(input("> Enter year: "))
    if year % 4 == 0:
        if (year % 100 == 0):
            if (year % 400 != 0):
                print("- Not a leap year, divisible by 100 but not 400.")

            else:
                print("- Leap year, divisible by 4, 100, and 400.")

        else:
            print("- Leap year, divisible by 4.")

    else:
        print("- Not a leap year.")


# Only execute when run
if __name__ == "__main__":
    main()
