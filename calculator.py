def main():
    """Simple command‑line calculator.
    Expects two numeric arguments and prints their sum and product.
    """
    import sys
    if len(sys.argv) != 3:
        print("Usage: python calculator.py <num1> <num2>")
        return
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(f"Sum: {a + b}")
        print(f"Product: {a * b}")
    except ValueError:
        print("Please provide numeric arguments.")

if __name__ == "__main__":
    main()