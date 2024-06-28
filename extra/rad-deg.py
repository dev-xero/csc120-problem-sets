# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

# Imports
from math import pi


# Main entry point
def main(**args):
    """
        Receives an input in radians (nπ) and returns its
        degree equivalent.

        Conversion factor: 1π rad -> 180 deg
    """
    rads = float(eval(input("> Enter angle in radians (nπ): ")))
    deg = rads * 180

    print(f"- Equivalent in deg/π: {deg}/π")
    print(f"- Full angle:", round(deg/pi, 4))


# Only run when executed
if __name__ == "__main__":
    main()
