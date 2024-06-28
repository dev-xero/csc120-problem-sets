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
        Print the line number and your name next to it, 100 times.
    """
    name = args.get("name") or "user"
    for i in range(1, 101):
        print(f"{i:3d}. {name}")


# Only execute when run
if __name__ == "__main__":
    main(name="xero")
