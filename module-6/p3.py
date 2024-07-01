# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

from math import log


# Main entry point
def main(**args):
    """
        Prompts the user for a number `n` and computes:
        (1 + 12 + 13 + ... + 1n) - ln(n)
    """
    n = int(input("> Enter a number n: "))

    # Check that n > 1
    if not n > 1:
        raise ValueError("n must be greater than 1")

    running_sum = 1
    for i in range(2, n+1):
        new_num = int(f'1{i}')
        running_sum += new_num

    result = running_sum - log(n)
    print(f"Result (2 d.p.): {result:.2f}")


# Only execute when run
if __name__ == "__main__":
    main()
