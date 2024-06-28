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
        Receives an angle between -180 and 180 degrees and returns
        its equivalent in 0 - 360 deg.
    """
    angle = float(input("> Enter an angle between -180 and 180 deg: "))

    if not (-180 <= angle <= 180):
        raise ValueError("Angle must be between -180 and 180 degrees.")

    corresponding_angle = angle % 360
    print("- Corresponding angle (deg):", corresponding_angle)


# Only execute when run
if __name__ == "__main__":
    main()
