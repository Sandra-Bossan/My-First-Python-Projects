# BUDGET TRACKER

import json

def add_expenses(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f'Added expense {description}, Amount {amount}')

def get_total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f'Total budget: {budget}')
    print('Expenses:')
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f'Total Spent: {get_total_expenses(expenses)}')
    print(f'Remaining Balance: {get_balance(budget, expenses)}')

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['opening_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_details(filepath, opening_budget, expenses):
    data = {
        'opening_budget': opening_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print('Welcome to MyBudget Tracker')
    filepath = 'budget_data.json'
    opening_budget, expenses = load_budget_data(filepath)
    
    if opening_budget == 0:
        opening_budget = float(input('Enter your opening budget: '))
    
    budget = opening_budget

    while True:
        print('\nWhat would you like to do?')
        print('1. Add an expense')
        print('2. Show budget details')
        print('3. Exit')
        choice = input('Enter your choice (1/2/3): ')
    
        if choice == '1':
            description = input('Enter your expense description: ')
            amount = float(input('Enter expense amount: '))
            add_expenses(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            print('\nAre you sure you want to exit MyBudget Tracker?')
            print('1. Yes')
            print('2. No')
            ur_choice = input('Enter your choice (1/2): ')
            if ur_choice == '1':
                save_budget_details(filepath, opening_budget, expenses)
                print('Thank you for utilising MyBudget Tracker. Goodbye!')
                break
        else:
            print('Invalid choice, please choose again.')

if __name__ == '__main__':
    main()