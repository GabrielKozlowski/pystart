from requests import get


response = get("https://danepubliczne.imgw.pl/api/data/synop")

for station in response.json():
    if station['id_stacji'] == '12566':
        for parameter, value in station.items():
            print(f'{parameter.capitalize()}:  {value}')
            

