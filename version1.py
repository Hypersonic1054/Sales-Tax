def set_tax_rate():
    while True:
        try:
            tax_rate_input = float(input("Enter your state's sales tax rate: "))
            tax_rate = tax_rate_input / 100 
            return tax_rate
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    tax_rate = set_tax_rate()
    print(f"The tax rate is: {tax_rate}")

main()
