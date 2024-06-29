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
        A store charges $12 per item you buy, if you buy
        less than 10 items, $10 if you buy between
        10 and 99 items, $7 if you buy 100 or more.

        Computes the cost of buying `n` items given
        these conditions.
    """
    quantity = int(eval(input("> Quantity: ")))

    if quantity < 10:
        print(f"- Price (qty x 12): ${12 * quantity}")

    elif 10 <= quantity < 100:
        print(f"- Price (qty x 10): ${10 * quantity}")

    else:
        print(f"- Price (qty x 7): ${7 * quantity}")


# Only execute when run
if __name__ == "__main__":
    main()
