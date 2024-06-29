# Import
from random import randint


# Main entry point
def main(**args):
    show_streak = args.get("streak") or False
    attempts = 1  # keep track of how many times they've attempted

    while True:
        rand = randint(1, 10)
        choice = input("> Guess a number between 1 - 10 (q to quit): ")

        # Check if the user wants to quit
        if choice == 'q':
            print("- Quitting...")
            return

        guess = int(choice)

        if guess == rand:
            print("- Correct! Random number was:", rand, '\n')
            if show_streak:
                print(
                    f"- Took you {attempts} tr{'ies' if attempts > 1 else 'y'}!")

            return

        else:
            print("- Incorrect, try again?\n")
            attempts += 1


# Only execute when run
if __name__ == "__main__":
    main(streak=True)
