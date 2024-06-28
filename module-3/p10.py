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
        Asks the user the dimensions:
            - width
            - height
        of the asterisk box they want, then prints it.
    """
    width = int(input("> Width of the box: "))
    height = int(input("> Height of the box: "))

    print(f"- Dimensions: {width} x {height}")

    for _ in range(height):
        print("*"*width)


# Only execute when run
if __name__ == "__main__":
    main()
