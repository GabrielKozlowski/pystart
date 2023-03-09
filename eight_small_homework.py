#
# import csv
#
# cars_data = [
#     {'car_name': 'Hennessey Venom F5', 'to_one_hundred': 2.6, 'top_speed': 484},{'car_name': 'SSC Tuatara', 'to_one_hundred': 2.5, 'top_speed': 460},{'car_name': 'Koenigsegg Agera RS', 'to_one_hundred': 3.1, 'top_speed': 457},{
#         'car_name': 'Koenigsegg One 1',
#         'top_speed': 450,
#         'to_one_hundred': 2.6
#     }
# ]
#
# with open('cars.csv', mode='w', newline='') as csv_file:
#     fieldnames = ['car_name', 'to_one_hundred', 'top_speed']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for row in cars_data:
#         writer.writerow(row)
#
#
# with open('cars.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',')
#     for row in reader:
#         print(row['car_name'], row['top_speed'])
#
##############################################################################################

# import subprocess
#
# address_ip = 'pystart.pl'
# output = subprocess.run(['ping', '-n', '1', address_ip], shell=True, capture_output=True)
#
# if 'could not find' in output.stdout.decode('utf8'):
#     print('Domain Not Found...')
# else:
#     print('Access To Domain.')
#
##############################################################################################


