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
        Prompt the user for an hour between 1 and 12, then
        prompt them for how many hours into the future they
        want to go.
    """
    hours = int(input("> Enter hour: "))

    # Check that the hour is in the range 1..12
    if not (1 <= hours <= 12):
        raise ValueError("Enter an hour between 1 and 12.")

    ahead = int(input("> How many hours ahead? "))
    new_hour = (hours + ahead) % 12

    # We show 12 o'clock instead of 0 o'clock
    print(f"- New hour: {new_hour if new_hour > 0 else 12} o'clock.")


# Only execute when run
if __name__ == "__main__":
    main()
