import os.path

import matplotlib.pyplot as plt
import csv

from datetime import datetime, date

statistics = {}
with open('operacje.csv', newline='', encoding='utf8') as csv_file:
    columns = ['data', 'rodzaj operacji', 'opis operacji', 'kwota operacji']
    reader = csv.DictReader(csv_file)

    for row in reader:
        operation_date = datetime.strptime(row['data'], '%Y-%m-%d')
        if operation_date.strftime('%B') not in statistics:
            statistics[operation_date.strftime('%B')] = {
                'total': 0,
                'income_quantity': 0,
                'expense_quantity': 0
            }

        if row['rodzaj operacji'] == 'przychód':
            statistics[operation_date.strftime('%B')]['total'] += float(row['kwota operacji'])
            statistics[operation_date.strftime('%B')]['income_quantity'] += 1
        else:
            statistics[operation_date.strftime('%B')]['total'] -= float(row['kwota operacji'])
            statistics[operation_date.strftime('%B')]['expense_quantity'] += 1


months = list(statistics.keys())
total = []
quantity = []
for month, data in statistics.items():
    total.append(data['total'])
    quantity.append(data['income_quantity'] + data['expense_quantity'])


fig, ax = plt.subplots()
ax.set_xlabel('Months')
ax.set(ylabel='Amount', title='Income In Months')
ax.bar(months, total)
plt.savefig('podsumowanie.png')



fig, ax = plt.subplots()
ax.set_xlabel('Months')
ax.set(ylabel='Operations', title='Operations In Months')
ax.bar(months, quantity)
plt.savefig('ilosc_operacji.png')

