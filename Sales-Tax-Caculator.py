import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

state_tax_rates = {
    "AL": 4.00, "AK": 0.00, "AZ": 5.60, "AR": 6.50, "CA": 7.25,
    "CO": 2.90, "CT": 6.35, "DE": 0.00, "FL": 6.00, "GA": 4.00,
    "HI": 4.00, "ID": 6.00, "IL": 6.25, "IN": 7.00, "IA": 6.00,
    "KS": 6.50, "KY": 6.00, "LA": 5.00, "ME": 5.50, "MD": 6.00,
    "MA": 6.25, "MI": 6.00, "MN": 6.875, "MS": 7.00, "MO": 4.225,
    "MT": 0.00, "NE": 5.50, "NV": 4.60, "NH": 0.00, "NJ": 6.625,
    "NM": 5.125, "NY": 4.00, "NC": 4.75, "ND": 5.00, "OH": 5.75,
    "OK": 4.50, "OR": 0.00, "PA": 6.00, "RI": 7.00, "SC": 6.00,
    "SD": 4.50, "TN": 7.00, "TX": 6.25, "UT": 4.85, "VT": 6.00,
    "VA": 5.30, "WA": 6.50, "WV": 6.00, "WI": 5.00, "WY": 4.00,
    "DC": 6.00
}

def set_tax_rate_by_state(state_tax_rates):
    while True:
        state = input("Enter your state abbreviation: ").upper().strip()
        if state in state_tax_rates:
            return state_tax_rates[state] / 100
        else:
            print("State not found. Please enter a valid state abbreviation.")

def get_number_items():
    while True:
        try:
            number_items = int(input("How many items are you purchasing? "))
            if number_items <= 0:
                print("Please enter a number greater than 0.")
            else:
                return number_items
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_item_costs(number_items):
    item_costs = []
    for i in range(number_items):
        while True:
            try:
                price = float(input(f"Enter the price of item {i + 1}: $"))
                if price < 0:
                    print("Please enter a positive number.")
                else:
                    item_costs.append(price)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return item_costs

def calculate_tax_amounts(item_costs, tax_rate):
    tax_amounts = [item * tax_rate for item in item_costs]
    return tax_amounts

def calculate_total_cost(item_costs, tax_amounts):
    total_costs = [item + tax for item, tax in zip(item_costs, tax_amounts)]
    return total_costs

def print_receipt(item_costs, tax_amounts, total_costs):
    print("\nReceipt:")
    print("-" * 30)
    for i in range(len(item_costs)):
        print(f"Item {i + 1}: ${item_costs[i]:.2f} | Tax: ${tax_amounts[i]:.2f} | Total: ${total_costs[i]:.2f}")
    print("-" * 30)
    print(f"Total Tax: ${sum(tax_amounts):.2f}")
    print(f"Total Cost: ${sum(total_costs):.2f}")

def main():
    while True:
        clear()
        
        tax_rate = set_tax_rate_by_state(state_tax_rates)
        number_items = get_number_items()
        item_costs = get_item_costs(number_items)
        tax_amounts = calculate_tax_amounts(item_costs, tax_rate)
        total_costs = calculate_total_cost(item_costs, tax_amounts)
        print_receipt(item_costs, tax_amounts, total_costs)
        
        repeat = input("\nDo you want to make another purchase? (y/n): ").lower()
        if repeat != 'y':
            break

main()
