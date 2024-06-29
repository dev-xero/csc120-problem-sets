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
        Prompts the user for a temperature in celsius, then
        gives them useful information on that temperature.
    """
    temp = float(eval(input("> Temperature (in Celsius): ")))

    # Handle temp < -273.15 (abs zero)
    if temp < -273.15:
        print("- Invalid temperature.")
        print("- Below absolute zero which is the coldest temperature in the Universe!")

    # Handle temp == -273.15
    elif temp == -273.15:
        print("- You've reached absolute zero! The coldest temperature in the Universe!")

    # Handle temp in range -273.15 - 0
    elif -275.15 < temp < 0:
        print("- You're at below freezing point.")
    
    # Handle temp == 0
    elif temp == 0:
        print("- You're at the freezing point.")
    
    # Handle temp in range 0 - 100
    elif 0 < temp < 100:
        print("- You're at normal temperature range.")

    # Handle temp == 100
    elif temp == 100:
        print("- You're at the boiling point of water!")

    # Handle temp > 100
    else:
        print("- You're above the boiling point.")

# Only execute when run
if __name__ == "__main__":
    main()
