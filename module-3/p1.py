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
        Prints a name 100 times.
    """
    name = args.get("name") or "user"
    print(f'{name}\n'*100)


# Only execute when run
if __name__ == "__main__":
    main(name="xero")  # Replace with yours
