# Function to add a new expense to the expenses list
def add_expense(expenses, amount, category):
    # Appending a dictionary with 'amount' and 'category' to the list
    expenses.append({"amount": amount, "category": category})

# Function to display all expenses in the list
def view_expenses(expenses):
    # Loop through each expense in the list
    for expense in expenses:
        # Print the amount and category using f-string
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")

# Function to calculate total amount of all expenses
def total_expenses(expenses):
    # Use map to extract only the 'amount' values and sum them
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    # Use filter and lambda to get only those expenses matching the category
    return filter(lambda expense: expense['category'] == category, expenses)

# --- Main Program Starts Here ---
expenses = []  # Empty list to store all expenses

# Infinite loop for the menu
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Filter by Category")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Get details from user
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(expenses, amount, category)  # Call add function

    elif choice == "2":
        # Call view function
        view_expenses(expenses)

    elif choice == "3":
        # Call total function and print result
        print(f"Total: {total_expenses(expenses)}")

    elif choice == "4":
        # Get category and filter matching expenses
        category = input("Enter category to filter: ")
        filtered = filter_expenses_by_category(expenses, category)
        # Show filtered expenses
        for expense in filtered:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}")

    elif choice == "5":
        # Exit the loop
        break

    else:
        print("Invalid choice. Please try again.")
