# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

# Main entry point
def main(**args):
    weight = float(input("> Enter a weight (kg): "))
    pounds_weight = weight * 2.2  # Conversion factor: 1 kg = 2.2 pounds

    print("- Weight in pounds (#):", pounds_weight)


# Only execute when run
if __name__ == "__main__":
    main()
