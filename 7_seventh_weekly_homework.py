# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # print Current Date DD/MM/YYYY, S:M:H
# from datetime import datetime
#
# now = datetime.now()
# print(f"{now.day}/{now.month}/{now.year}, {now.hour}:{now.minute}:{now.second}")

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Print How Many Days Are Left Until Summer
# from datetime import date, datetime, timedelta
# summer = '2023-6-21'
# summer_in_datetime = datetime.strptime(summer, '%Y-%m-%d')
#
# after_summer = datetime.strptime('2023-07-01', '%Y-%m-%d').date()
# before_summer = date.today()
#
# delta = (summer_in_datetime.date() - before_summer).days
# delta1 = (summer_in_datetime.date() - after_summer).days
# if int(delta1) < 0:
#     delta1 = int(delta) + 365
#
# print(f'Days To Summer in 2023: {delta}')
# print(f'Days To Summer In 2024: {delta1}')
#

# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Ask User For Name And Lastname. Save This Data To Txt File

# first_name = input('What Is Your Name?? ')
# last_name = input('What Is Your Last Name?? ')
#
# with open('user_data.txt', 'w', encoding='utf-8') as file:
#     file.write(f"{first_name}-{last_name}\n")



# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Graphic Interface For Task Three

from tkinter import *

app = Tk()
app.title('User Data')
count = 0
users_list = []
def getdata():
    first_name_value = enter_first_name.get()
    last_name_vale = enter_last_name.get()
    enter_last_name.delete(0, END)
    enter_first_name.delete(0, END)
    if len(first_name_value) > 0 and len(last_name_vale) > 0:
        with open('user_data.txt', 'a', encoding='utf-8') as file:
            file.write(f'{first_name_value.capitalize()}-{last_name_vale.capitalize()}\n')
    users_list.clear()
    global count
    count = 0


def showdata():
    global count
    if count == 0:
        with open('user_data.txt', 'r', encoding='utf-8') as file:
            user = file.read().strip()
            users_list.append(user)
            for numb, user in enumerate(users_list):
                user_label = Label(app, text=user)
                user_label.grid(column=0,columnspan=2, row=numb+5)
    count += 1



label_first_name = Label(app, text='Enter First Name', width=20)
label_first_name.grid(column=0, row=0)
enter_first_name = Entry(app)
enter_first_name.grid(column=0, row=1)

label_last_name = Label(app, text='Enter First Name', width=20)
label_last_name.grid(column=1, row=0)
enter_last_name = Entry(app)
enter_last_name.grid(column=1, row=1)

button_submit = Button(app, width=20, text='Submit', command=lambda :getdata())
button_submit.grid(column=0, row=3, columnspan=2)
button_show = Button(app, width=20, text='Show Names', command=lambda :showdata())
button_show.grid(column=0, row=4, columnspan=2)






app.mainloop()

# # >>>>>>>>>>>>>>> Fifth and Sixth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




