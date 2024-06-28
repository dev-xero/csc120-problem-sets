# Main entry point
def main(**args):
    weight = float(input("> Enter a weight (kg): "))
    pounds_weight = weight * 2.2 # Conversion factor: 1 kg = 2.2 pounds

    print("- Weight in pounds (#):", pounds_weight)

if __name__ == "__main__":
    main()