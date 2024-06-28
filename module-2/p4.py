# -----------------------------------------------------------------
#
# Xero, 2024 - Open Source Software
# This file is part of a larger collection which can be found here:
# https://github.com/dev-xero/csc120-problem-sets
#
# ------------------------------------------------------------------

# Main entry point
def main():
    user_input = int(eval(input("> Enter a number: ")))
    print(f"- The square of {user_input} is {user_input**2}", "", sep=".")


# Only execute when run
if __name__ == "__main__":
    main()
