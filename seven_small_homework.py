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

date_start_work = '10.1.2020'
date_stop_work = '15.1.2020'
payment_for_day = 200

start_date = datetime.strptime(date_start_work, '%d.%m.%Y')
stop_date = datetime.strptime(date_stop_work, '%d.%m.%Y')
diff = stop_date - start_date
payment = diff.days * payment_for_day


while stop_date >= start_date:
    if start_date.strftime("%a") in ['Sat', 'Sun']:
        payment += payment_for_day
    print(start_date.strftime("%a %d.%m.%Y"))
    start_date += timedelta(days=1)

print(payment)
######################################################################################



