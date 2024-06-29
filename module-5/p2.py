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
        Prompts the user for a temperature, then asks what unit
        the temperature is in (Celsius or Fahrenheit), then
        converts it into the other.
    """
    temp = float(eval(input("> Temperature: ")))
    unit = input("> Unit (C/F): ")

    if not unit in ['C', 'F']:
        raise ValueError("Invalid unit provided.")

    # Handle celsius conversion
    if unit == 'F':
        conv = (5/9)*(temp - 32)
        print(f"- {temp:.2f}F to celsius: {conv:.2f}C")

    # Handle fahrenheit conversion
    else:
        conv = (9/5)*temp + 32
        print(f"- {temp:.2f}C to fahrenheit: {conv:.2f}F")


# Only execute when run
if __name__ == "__main__":
    main()
