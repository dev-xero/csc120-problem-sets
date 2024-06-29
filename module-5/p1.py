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
        Prompts the user for a length in cm, then converts it
        into inches.
        Conversion factor: 1in -> 2.54cm
    """
    length_cm = float(eval(input("> Length in cm: ")))
    length_in = length_cm / 2.54

    print("- Length in inches (3 d.p.):", round(length_in, 3))


# Only execute when run
if __name__ == "__main__":
    main()
