import requests, sqlite3


def get_weather_data(station_id:str) -> dict:
    """This Function Get Station Id And Returns Data Of
       Mensurment Date, Station Name, Temperature, Pressure

    Args:
        station_id (str): Number of IMGW station id

    Returns:
        dict: Dict of station data.
    """
    response = requests.get(f'https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}')

    station_info = response.json()

    data = {
        'mensurment_date': station_info['data_pomiaru'],
        'station_name': station_info['stacja'],
        'temperature': station_info['temperatura'],
        'pressure': station_info['cisnienie'],
    }

    return data


def create_db_for_weather(db_name:str) -> str:
    """This Function Create Data Base For Weather Data

    Args:
        db_name (str): Name For Weather Data
    Returns:
        str: Info about success or error
    """

    create_table = """ CREATE TABLE stations_info(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                station_name VARCHAR(50) NOT NULL,
                mensurment_date BLOB,
                temperature REAL,
                pressure REAL
    )"""

    try:
        with sqlite3.connect(f'{db_name}.db') as conection:
            cursor = conection.cursor()
            cursor.execute(create_table)
            conection.commit()
            info_returned = 'Data Base Created Successfuly'
    except:
        info_returned = 'Error Something Went Wrong. Database Not Created'

    return info_returned



def add_weather_station_data_to_database(database_name:str, station_data:dict) ->str:
    """This Function Adds Data To Weater Data Base

    Args:
        database_name (str): The name of database, for adds data of weather. No extension!
        station_data (dict): Dictionary of weater data

    Returns:
        str: Info about success or error
    """
    # print(station_data)

    station_name = station_data['station_name']
    mensurment_date = station_data['mensurment_date']
    temperature = station_data['temperature']
    pressure = station_data['pressure']


    add_station_data = f"INSERT INTO stations_info(station_name, mensurment_date, temperature, pressure) VALUES ('{station_name}','{mensurment_date}','{temperature}','{pressure}')"


    try:
        with sqlite3.connect(f'{database_name}.db') as conection:
            cursor = conection.cursor()

            cursor.execute(add_station_data)

            conection.commit()
            info_returned = 'Added Data To Data Base Successfuly'

    except:
        info_returned = 'Error Something Went Wrong. Data Not Added To Database'

    return info_returned

database_name = 'weather_from_krakow'

data_from_station = get_weather_data(12566)
# print(create_db_for_weather(database_name))
print(add_weather_station_data_to_database(database_name, data_from_station))


