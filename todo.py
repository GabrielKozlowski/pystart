import sqlite3
from sys import argv


def setup():
    with sqlite3.connect('todos.db') as conection:
        sql = """ CREATE TABLE todos(
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) UNIQUE NOT NULL,
            is_done INTEGER DEFAULT 0
        )"""
        cursor = conection.cursor()
        cursor.execute(sql)
        conection.commit()


if len(argv) == 2 and argv[1] == 'setup':
    setup()


def show_quest_list():
    with sqlite3.connect('todos.db') as conection:
        cursor = conection.cursor()
        for quest in cursor.execute('SELECT * FROM todos WHERE is_done=0'):
            print(quest)

def add_quest():
    with sqlite3.connect('todos.db') as conection:
        cursor = conection.cursor()
        quest = input('What quest you want added ?: ')
        cursor.execute(f'INSERT INTO todos(title) VALUES ("{quest}")')
        conection.commit()

def update_quest():
    with sqlite3.connect('todos.db') as conection:
        cursor = conection.cursor()
        quest = input('Enter id of completed quest ')
        cursor.execute(f'UPDATE todos SET is_done=1 WHERE todo_id={quest}')
        conection.commit()



while True:
        
    menu = """
    What you want to do ??
    0 - Show list to do.
    1 - Add new quest to do
    2 - Chcnge quest to complete
    3 - Exit
    """

    ansver = int(input(menu))

    if ansver == 0:
        show_quest_list()
    elif ansver == 1:
        add_quest()
    elif ansver == 2:
        update_quest()
    else:
        exit()