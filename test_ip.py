import sqlite3, os, time, subprocess
from datetime import datetime

def create_sqlite_db(db_name:str, table_name:str, **kwargs:str) ->str:
    """This Function Create Sqlite DataBase

    Args:
        db_name (str): Name Of DataBase
        table_name (str): Name Of Table
        kwargs (str): Name, type and value of Table

    Returns:
        str: Information about errors or success
    """

    # Write construction for sqlite to create db
    kwargs_list = ''
    for n, (key, value) in enumerate(kwargs.items()):
        kwargs_list += f'{key.lower()} {value.upper()}'

        # add comma and new line exept at the end
        if n < len(kwargs) - 1:
            kwargs_list += ',\n'


    # Create db in sqlite
    try:
        with sqlite3.connect(f'{db_name}.db') as conection:
            cursor = conection.cursor()
            data = f"""CREATE TABLE {table_name.lower()}(
                {kwargs_list})"""


            cursor.execute(data)
            conection.commit()
        return "Create DB Successfuly"
    
    except:
        return 'Error! Someting went wrong.'


def delete_table_from_sqlite_db(db_name:str, table_name:str)-> str:
    """This Function Deleting Table From Sqlite DataBase

    Args:
        db_name (str): DataBase name
        table_name (str): Table name

    Returns:
        str: Info about errors or success
    """
    try:
        with sqlite3.connect(f'{db_name}.db') as conection:
            cursor = conection.cursor()
            data = f'DROP TABLE IF EXISTS {table_name}'
            cursor.execute(data)
            conection.commit()

        return "The table has been removed"
    
    except:
        return "Error, someting went wrong."






def add_ips_to_db(db_name:str, ip_adress:str) -> str:
    """This Function Add Ip adress To db

    Args:
        db_name (str): Name of db 
        ip_adress (str): Ip to added

    Returns:
        str: Info of errors or success
    """
    try:
        with sqlite3.connect(f'{db_name}.db') as conection:
            cursor = conection.cursor()
            cursor.execute(f'INSERT INTO ip_to_check(ip_adresses) VALUES("{ip_adress}")')
            conection.commit()
        return "Ip adress successfuly added"
    
    except:
        return "Error, someting went wrong."    



def ping_ips_from_db(db_name:str, trials:int, sleep:int)-> str:
    """This Program Pings Servers

    Args:
        db_name (str): Name of DataBase With Ips adress
        trials (int): Number of ping trials
        sleep (int): Time to sleep between trials in secounds

    Returns:
        str: All Trials , Number of successful and unsuccessful trials
    """
    with sqlite3.connect(f'{db_name}.db') as conection:
        cursor = conection.cursor()

        ip_list = []
        for data in cursor.execute('SELECT ip_adresses FROM ip_to_check'):                
            ip_list.append(data[0])
        
        repetitions = 0
        is_up = 0
        is_down = 0
        while repetitions < trials:
            time.sleep(sleep)
            for ip in ip_list:
                if ip is not None:
                    response = subprocess.call("ping -n 1 " + ip)

                    date = datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S')
                    if response == 0:                        
                        cursor.execute(f'INSERT INTO log("ip_adress", "date_of_checks_connection", "is_connected") VALUES ("{ip}", "{date}", "is up")')
                        is_up += 1
                    else:
                        cursor.execute(f'INSERT INTO log("ip_adress", "date_of_checks_connection", "is_connected") VALUES ("{ip}", "{date}", "is down")')
                        is_down += 1

            repetitions += 1
    return f"Trials = {is_up + is_down}, Up:{is_up}, Down:{is_down}"




# # First Creat db
# print(create_sqlite_db('test_ip', 'ip_to_check', id='INTEGER PRIMARY KEY AUTOINCREMENT' ,ip_adresses='VARCHAR(100) UNIQUE NOT NULL'))

# # Create Second table in this same db
# print(create_sqlite_db('test_ip', 'log', id='INTEGER PRIMARY KEY AUTOINCREMENT' , ip_adress='VARCHAR(100) NOT NULL' , date_of_checks_connection='BLOB' ,is_connected='VARCHAR(10) NOT NULL'))


# print(delete_table_from_sqlite_db("test_ip","log"))


# print(add_ips_to_db('test_ip', '192.168.10.1'))
# print(ping_ips_from_db('test_ip', 5, 60))

