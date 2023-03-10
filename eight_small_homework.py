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
# ##############################################################################################
#
# import argparse
# import os
# from os import walk
# from pathlib import Path
# from PIL import Image
#
# # Create Variable For Argument Parser
# parser = argparse.ArgumentParser(
#     prog='Content listing',
#     description='This program search file and extension',
#     epilog='Gabriel Kozłowski'
# )
#
# # Add Arguments
# parser.add_argument('--dir', type=str)
# parser.add_argument('--extension', type=str)
#
# # Create Variable For Inputted Data
# argument = parser.parse_args()
#
#
# def change_path(path_to_change: str) -> str:
#     """
#     This Function Change Path Name.
#     :param path_to_change: String Path For Change
#     :return: CHanging String Path
#     """
#     # Create List For New String Path
#     changed_path = []
#     # Split String Of Path With \\
#     for word in path_to_change.split('\\'):
#         # Check Word If Is Equal photos
#         if word == 'photos':
#             # Replace Word photos To Extended Path Name
#             word = word.replace('photos', 'resized\photos')
#             # Append To List New Word
#             changed_path.append(word)
#         else:
#             # Append Word To List
#             changed_path.append(word)
#     # Return New Path Wit Join Function
#     return '\\'.join(changed_path)
#
#
# def create_dict_to_save(path_to_change: str) -> str:
#     """
#     This Function Change Path For Create New Direction.
#     :param path_to_change: String Of File Path With Extension
#     :return: String Of New Path To Create
#     """
#     # Create List With String For New Path
#     create_diction = []
#     # Split String Using \\
#     for diction in path_to_change.split('\\'):
#         # Search If Word Is Equal photos
#         if diction == 'photos':
#             # Replace Word photos To New Word For Extension Path
#             diction = diction.replace('photos', 'resized\\photos\\')
#             # Append To List New Word
#             create_diction.append(diction)
#         # If Word Endswith Extension Pass That Word
#         elif diction.endswith('.jpg'):
#           continue
#         # Else Append Word To List
#         else:
#             create_diction.append(diction)
#     # Return String With Join Function
#     return '\\'.join(create_diction)
#
#
# path_of_photos = []
# # Loop With Walk Function For Params From inputted Direction
# for path, _, photos in walk(argument.dir):
#     # Loop For Get Unique Path For File
#     for photo in photos:
#         # Create Path Variable With Function Path
#         sample = Path(f'{path}\\{photo}')
#         # If Suffix Of File Path Is Equal Inputted Extension
#         if sample.suffix == f'.{argument.extension}':
#             # Append Path Absolute To List
#             path_of_photos.append(sample.absolute())
#
# # Loop For Paths In Path List
# for img_path in path_of_photos:
#     # Create Variable With Image From Path
#     im = Image.open(img_path)
#     # Create Variable With Changed Image Path With Function
#     new_path = change_path(str(img_path))
#     # Create Variable With New Direction To Save Changed Foto
#     new_diction =  create_dict_to_save(str(img_path))
#     # If New Direction Not Exist
#     if not os.path.exists(new_diction):
#         # Create new Direction
#         os.makedirs(new_diction)
#     # Change Size Of Foto
#     changed_im = im.resize((300, 300))
#     # Save New Resized Foto To New Direction Path
#     changed_im.save(new_path)

#############################################################################################
# from PIL import Image
#
# import argparse
# from os import walk, path, makedirs
# from pathlib import Path
#
#
# parser = argparse.ArgumentParser(
#     prog='Photo Resized',
#     description='This program change photo size',
#     epilog='Gabriel Kozłowski'
# )
#
# parser.add_argument('--dir')
# parser.add_argument('--extension')
# argument = parser.parse_args()
#
# for photo_path, _, photos in walk(argument.dir):
#     for photo in photos:
#         source = Path(f"{photo_path}\\{photo}")
#         if source.suffix == f'.{argument.extension}':
#             im = Image.open(source.absolute())
#             thumbnail = im.resize((300, 300))
#             if not path.exists(f'resize\\{photo_path}'):
#                 makedirs(f'resize\\{photo_path}')
#
#             thumbnail.save(f"resize\\{photo_path}\\{photo}")
###########################################################################################




