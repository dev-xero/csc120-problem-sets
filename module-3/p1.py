# Imports
from random import randint


# Main entry point
def main(**args):
    """
        Generates and prints 50 random integers all between
        3 and 6.
    """
    for i in range(50):
        print(f"Gen: {i+1}: {randint(3, 6)}")


if __name__ == "__main__":
    main()
