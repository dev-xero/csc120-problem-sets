# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

# Main entry point
def main(**args):
    x = int(input("> Enter a number: "))
    print(x, 2*x, 3*x, 4*x, 5*x, sep="---")


# Only execute when run
if __name__ == "__main__":
    main()
