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
        Prompts the user for some `n` seconds and prints
        the number of minutes and seconds composed of n.
    """
    n = int(input("> Enter some n seconds: "))

    # Subtract the remaining seconds then divide by 60
    mins = round((n - (n % 60)) / 60, 1)
    sec = float(n % 60)

    print(f"In {n} seconds, there are:")
    print(f"- Minutes: {mins}")
    print(f"- Seconds: {sec:.1f}")


# Only execute when run
if __name__ == "__main__":
    main()
