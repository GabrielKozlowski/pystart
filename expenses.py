from json import dump, load

text = """
Expenses
1. Add Expenses
2. Show All Expenses
3. Exit

"""
while True:
    user_choice = input(text)

    if user_choice == '1':
        with open('list_of_expenses.json', 'r') as file:
            list_of_expenses = load(file)
            name_of_expense = input('Enter Name Of Expense: ')
            value_of_expense = input('Enter Value Of Expense: ')
            expense = {
                "name": name_of_expense,
                "value": value_of_expense
            }
            list_of_expenses.append(expense)
            with open('list_of_expenses.json', 'w') as write_file:
                dump(list_of_expenses, write_file)

    elif user_choice == '2':
        with open('list_of_expenses.json', 'r') as file:
            print(load(file))
    elif user_choice == '3':
        print('Bye Bye...')
        quit()
    else:
        print('Wrong Number ! try Again...')