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
        Prompts the user for `n` and prints up till the `nth`
        Fibonacci number
    """
    n = int(input("> How many fib numbers?: "))

    # Check that n is greater than 0
    if n < 1:
        raise ValueError("n must be greater than 0.")

    if n == 1:
        print("1")
        return

    if n == 2:
        print("1 1")
        return

    # For n > 2
    n_1 = 1  # current - 1 (1 element before)
    n_2 = 1  # current - 2 (2 elements before)

    print("1 1", end=" ")
    for i in range(n-2):
        curr = n_1 + n_2
        print(curr, end=" ")

        # The new curr-1 is curr and new curr-2 is prev of curr-1
        n_2, n_1 = n_1, curr


# Only execute when run
if __name__ == "__main__":
    main()
