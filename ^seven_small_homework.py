from datetime import date, datetime, timedelta

#
# today = date.today()
# print(f"Today is {today}")
#
# birthday = date(today.year, 1, 30)
#
# if birthday < today:
#     birthday = date(today.year + 1, 1, 30)
#
# print(f"Your Next Birthday Are {birthday.strftime('%a, %d.%m.%Y')}")
####################################################################################
#
# date_start_work = '10.1.2020'
# date_stop_work = '15.1.2020'
# payment_for_day = 200
#
# start_date = datetime.strptime(date_start_work, '%d.%m.%Y')
# stop_date = datetime.strptime(date_stop_work, '%d.%m.%Y')
# diff = stop_date - start_date
# payment = diff.days * payment_for_day
#
#
# while stop_date >= start_date:
#     if start_date.strftime("%a") in ['Sat', 'Sun']:
#         payment += payment_for_day
#     print(start_date.strftime("%a %d.%m.%Y"))
#     start_date += timedelta(days=1)
#
# print(payment)
######################################################################################

#
#
# with open('test_txt.txt', 'r') as handler:
#     for line in handler:
#         print(line.strip())
#
# with open('test_txt.txt', 'a') as file:
#     next_line = '11. Added Line\n'
#     file.write(next_line)
#
# with open('test_txt.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)
#
# with open('test_txt.txt', 'w') as file:
#     update_file = 'Here Was A 10 Lines And Now Is Only One\n'
#     file.write(update_file)
#
# with open('test_txt.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)

#####################################################################################

# with open('transakcje.txt', 'r', encoding='utf-8') as data_file, open('przychody.txt', 'w', encoding='utf-8') as output_file:
#     for line in data_file:
#         date, name, value = line.strip().split(';')
#         if int(value) > 0:
#             output_file.write(line)
#
# total = 0
# with open('przychody.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         date, name, value = line.strip().split(';')
#         total += int(value)
#
# print(total)

###########################################################################################



