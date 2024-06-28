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
        Prompts the user for their name and how many times to
        print it, then prints it that many times.
    """
    name = str(input("> Your name: "))
    times = int(input("> No. of times: "))

    # Check that times is greater than 0
    if not (times > 0):
        raise ValueError("Enter a number of times greater than zero.")

    for i in range(1, times+1):
        print(f"{i}. {name}")


# Only execute if run
if __name__ == "__main__":
    main()
