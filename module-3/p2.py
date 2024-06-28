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
        Fill the screen horizontally and vertically with your
        name.
    """
    name = args.get("name") or "user"
    for _ in range(1000):
        print(" ", end=name)


# Only run when executed
if __name__ == "__main__":
    main(name="xero")
