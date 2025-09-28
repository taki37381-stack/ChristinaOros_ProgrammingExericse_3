Technical Design Document
Name: Christina Oros
Date Created: September 26, 2025
Program Description:
This program collects a user's monthly expenses, allowing the user to input different expense types and amounts. It then calculates the total expenses, finds the highest and lowest expense using the reduce() function from the functools module, and displays a summary of the results.

Functions used in the Program (list in order as they are called):
1. Function Name: get_expenses()
Description: Collects monthly expenses from the user by repeatedly prompting for the expense type and amount until the user decides to stop or the maximum number of expenses is reached.
Parameters: None
Variables:
•	expenses (list): Stores dictionaries of expense types and amounts.
•	expense_type (string): User input for the type of expense.
•	amount (float): User input for the expense amount.
•	more (string): User input to continue or stop entering expenses.
Logical Steps:
1.	Initialize an empty list expenses.
2.	Prompt user repeatedly for expense type and amount.
3.	Validate amount input to ensure it’s numeric.
4.	Append each expense as a dictionary to expenses.
5.	Stop input if user answers anything other than "yes" or if max expenses reached.
6.	Return the list of expenses.
Returns: List of expense dictionaries with keys "type" and "amount".
2. Function Name: calculate_total(expenses)
Description: Uses the reduce() function to sum the amounts of all expenses in the list.
Parameters:
•	expenses (list): List of expense dictionaries.
Variables: None (uses lambda in reduce)
Logical Steps:
1.	Use reduce() with a lambda function that accumulates the sum of "amount" in the expenses list.
2.	Return the total sum.
Returns: Float representing the total expense amount.

3. Function Name: find_highest(expenses)
Description: Uses reduce() to find the expense with the highest amount.
Parameters:
•	expenses (list): List of expense dictionaries.
Variables: None (uses lambda in reduce)
Logical Steps:
1.	Use reduce() with a lambda that compares two expenses and returns the one with the higher amount.
2.	Return the highest expense dictionary.
Returns: Dictionary of the highest expense.

4. Function Name: find_lowest(expenses)
Description: Uses reduce() to find the expense with the lowest amount.
Parameters:
•	expenses (list): List of expense dictionaries.
Variables: None (uses lambda in reduce)
Logical Steps:
1.	Use reduce() with a lambda that compares two expenses and returns the one with the lower amount.
2.	Return the lowest expense dictionary.
Returns: Dictionary of the lowest expense.
5. Function Name: main()
Description: Orchestrates the program flow: collects expenses, calculates totals, highest and lowest, and displays results.
Parameters: None
Variables:
•	expenses (list): List of user-entered expense dictionaries.
•	total (float): Total expense calculated.
•	highest (dict): Highest expense found.
•	lowest (dict): Lowest expense found.
Logical Steps:
1.	Call get_expenses() to collect expense data.
2.	If no expenses entered, print message and exit.
3.	Calculate total using calculate_total().
4.	Find highest and lowest expenses using find_highest() and find_lowest().
5.	Print a summary showing total, highest, and lowest expenses.
Returns: None

Logical Steps (order of function calls):
1.	main() is the entry point.
2.	main() calls get_expenses() to collect data.
3.	main() calls calculate_total(expenses) to sum amounts.
4.	main() calls find_highest(expenses) to get highest expense.
5.	main() calls find_lowest(expenses) to get lowest expense.
6.	main() displays the results.
<img width="468" height="630" alt="image" src="https://github.com/user-attachments/assets/29575cd2-5a9c-47b8-82ee-e1a9c26cd18b" />
