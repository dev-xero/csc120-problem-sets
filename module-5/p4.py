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
        Prompts the user for how many college credits 
        they've taken, then prints their college year / status
        based on the number range.
    """
    creds = int(input("> How many credits have you taken?: "))

    if creds <= 23:
        print("- Freshman.")

    elif 24 <= creds <= 53:
        print("- Sophomore.")

    elif 54 <= creds <= 83:
        print("- Junior.")

    else:
        print("- Senior.")


# Only execute when run
if __name__ == "__main__":
    main()
