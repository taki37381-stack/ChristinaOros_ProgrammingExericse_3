# -----------------------------------------------
# This program collects a user's monthly expenses,
# calculates the total, highest, and lowest expense 
# using the reduce() function, and displays the results.
# -----------------------------------------------

from functools import reduce

# CONSTANT to limit number of expenses for demo (can be removed for unlimited input)
MAX_EXPENSES = 100


# Function to collect monthly expenses from the user
def get_expenses():
    expenses = []

    print("Welcome! Let's enter your monthly expenses.\n")

    while True:
        # Prompt user for type of expense
        expense_type = input("Enter the type of expense (e.g., Rent, Food, Utilities): ").strip()

        # Prompt user for amount of expense
        while True:
            try:
                amount = float(input(f"Enter the amount for {expense_type}: $"))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")

        # Append the expense as a dictionary
        expenses.append({"type": expense_type, "amount": amount})

        # Ask user if they want to continue
        more = input("Do you want to enter another expense? (yes/no): ").strip().lower()
        if more != "yes":
            break

        if len(expenses) >= MAX_EXPENSES:
            print("Maximum number of expenses reached.")
            break

    return expenses


# Function to calculate the total expense using reduce()
def calculate_total(expenses):
    return reduce(lambda acc, exp: acc + exp["amount"], expenses, 0)


# Function to find the highest expense using reduce()
def find_highest(expenses):
    return reduce(lambda x, y: x if x["amount"] >= y["amount"] else y, expenses)


# Function to find the lowest expense using reduce()
def find_lowest(expenses):
    return reduce(lambda x, y: x if x["amount"] <= y["amount"] else y, expenses)


# Main function to run the program
def main():
    # Collect expenses from the user
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered. Exiting program.")
        return

    # Calculate total, highest, and lowest expenses
    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    # Display results
    print("\n--- Monthly Expense Summary ---")
    print(f"Total Monthly Expense: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} - ${highest['amount']:.2f}")
    print(f"Lowest Expense: {lowest['type']} - ${lowest['amount']:.2f}")
    print("--------------------------------\n")


# Entry point of the program
if __name__ == "__main__":
    main()
