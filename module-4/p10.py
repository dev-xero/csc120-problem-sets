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
        Asks the user for a year ahead of 1600 and prints
        how many leap years there has been since.

        Note: A year is a leap if divisible by 4, if also
        divisible by 100, they must also be divisible by 400
    """
    year = int(input("> Enter a year ahead of 1600: "))

    # Check that this year > 1600
    if not (year > 1600):
        raise ValueError("Enter a year ahead of 1600.")

    years_since = year - 1600
    years_by_4 = years_since // 4      # years divisible by 4
    years_by_100 = years_since // 100  # years divisible by 100
    years_by_400 = years_since // 400  # years divisible by 400

    # A leap year is divisible by 4 and 400, but not 100
    leap_years = years_by_4 - years_by_100 + years_by_400

    print("- Year:", year)
    print("- Years since 1600:", years_since)
    print("- Leap years since 1600:", leap_years)


# Only execute when run
if __name__ == "__main__":
    main()
