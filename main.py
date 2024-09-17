from datetime import datetime

expenses = [
    {'amount': 50.0, 'category': 'Food', 'date': '2023-10-01'},
    {'amount': 20.0, 'category': 'Transport', 'date': '2023-10-02'},
    {'amount': 100.0, 'category': 'Utilities', 'date': '2023-10-03'}
]

def add_expense():
    category = input('Enter category: ')
    amount = float(input('Enter amount in USD: '))
    date = datetime.today().strftime("%d-%m-%Y")

    expenses.append({'category': category, 'amount': amount, 'date': date})

    print(f'''\n\t--------- Expense added! --------------
                Category: {category}
                Amount:   ${amount:.2f}
                Date:     {date }
          ''')
    input('Press Enter to continue... ')

def view_expenses():
    if not expenses:
        print('\nNo Expenses recorded yet.')
    else:
        print(f'\n\t--------- Expenses ----------\n')
        print(f'+-------------------------------------------------------+')
        print(f'| {"#":<6}  | {"Category":<15} | {"Amount":<10} | {" Date":<12} |')
        print(f'+-------------------------------------------------------+')
        for i, expense in enumerate(expenses, start=1):
            print(f'| {i:<6}  | {expense.get("category"):<15} | {expense.get("amount"):<10.2f} | {expense.get("date"):<12} |') 

        print(f'+-------------------------------------------------------+')
        input('Press Enter to continue...')

def main():

    while True:
        print('\n----------- Expense Trucker -------- \n')
        print('''\t
            1. Add Expense
            2. View Expenses
            3. Update Expense
            4. Delete Expense
            5. Calculate Total Expenses
            6. Exit 
        ''')
        choice = int(input('\n\tSelect an option: '))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            break
        else:
            print('\n\tInvalid option, please try again')
            input('press Enter to continue...')
        

     

main()
