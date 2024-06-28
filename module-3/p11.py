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
        Given any amount of change less than $1.00, print out
        exactly how many:
            - Quarters -> 25 cents
            - Dimes    -> 10 cents
            - Nickels  -> 5 cents
            - Pennies  -> 1 cent
        will be needed to efficiently make up that amount.
    """
    change = float(input("> Enter change less than $1.00: "))

    # Check that change is less than 1.00
    if not (change < 1.00):
        raise ValueError("Change must be less than $1.00.")

    # Convert dollars to cents, so we avoid float inconsistencies
    cents = round(change * 100)

    # Compute quarters
    quarters = cents // 25
    cents %= 25

    # Compute dimes
    dimes = cents // 10
    cents %= 10

    # Compute nickels
    nickels = cents // 5
    cents %= 5

    # Compute pennies
    pennies = cents // 1

    print("- {:10s} {:2d}".format("Quarters:", quarters))
    print("- {:10s} {:2d}".format("Dimes:", dimes))
    print("- {:10s} {:2d}".format("Nickels:", nickels))
    print("- {:10s} {:2d}".format("Pennies:", pennies))


# Only execute when run
if __name__ == "__main__":
    main()
