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
        Asks the user to enter three numbers, then computes
        the sum and average of the numbers.
    """
    total = 0
    average = 0
    numbers = input("> Enter three numbers (comma separated): ")
    num_array = numbers.split(",")  # split the numbers by ","

    # Check that we have at least three elements
    if len(num_array) < 3:
        raise ValueError("Enter three comma separated numbers.")

    # Compute the total and averages
    total = sum(int(num) for num in num_array)
    average = total / 3

    # Print the results
    print("- Sum:", total)
    print("- Average:", average)


# Only execute when run
if __name__ == "__main__":
    main()
