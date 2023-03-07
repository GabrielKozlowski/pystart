from json import dump, load

text = """
Expenses
1. Add Expenses
2. Show All Expenses
3. Exit

"""
while True:
    user_choice = input(text)
    with open('list_of_expenses.json', 'r') as file:
        list_of_expenses = load(file)


    if user_choice == '1':
            name_of_expense = input('Enter Name Of Expense: ')
            value_of_expense = float(input('Enter Value Of Expense: '))
            list_of_expenses.append({
                "name": name_of_expense,
                "value": value_of_expense
            })

            with open('list_of_expenses.json', 'w') as write_file:
                dump(list_of_expenses, write_file)

    elif user_choice == '2':
        total = 0
        for expense in list_of_expenses:
            total += expense['value']
            print(expense['name'], expense['value'])
        print('Total costs of expenses', total)



    elif user_choice == '3':
        print('Bye Bye...')
        quit()
    else:
        print('Wrong Number ! try Again...')