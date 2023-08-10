# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create program which write product list and save it in the txt file

# from datetime import datetime

# ansvers = set()
# while True:
#     data_today = datetime.strftime(datetime.today(), '%d-%m-%Y')

#     info = '''Enter Produckt Name or exit: '''
#     product_name = input(info)
#     ansvers.add(product_name)

#     if product_name.lower() == 'exit':
#         with open(f'{data_today}.txt', 'a+') as file:
#             for ansver in ansvers:
#                 if ansver != 'exit':
#                     file.write(f'{ansver}\n')
#             quit()

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Serch of all txt files in catalog and save all content to one new txt file.
# import os


# def find_all_txt_file_in_catalog(path:str):
#     """Finds all txt file in catalog

#     Args:
#         path (str): Path for catalog

#     Returns:
#         _type_: List of all txt files
#     """
#     file_list_of_txt_extension = []
#     data = os.listdir(path)


#     lines = []

#     for d in data:
#         if os.path.isdir(path+'\\'+d):
#             for i in os.listdir(path+'\\'+d):
#                 if os.path.isdir(path+'\\'+d+'\\'+i):
#                     for a in os.listdir(path+'\\'+d+'\\'+i):
#                         if os.path.isdir(path+'\\'+d+'\\'+i+'\\'+a):
#                             continue

#                         elif os.path.isfile(path+d+'\\'+i+'\\'+a):
#                             _, extension = os.path.splitext(a)
#                             if extension == '.txt':
#                                 with open(path+d+'\\'+i+'\\'+a, 'r', encoding='UTF-8') as txt_f:
#                                     l = txt_f.readlines()
#                                     for line in l:
#                                         lines.append(line)

#                                 file_list_of_txt_extension.append(a)            
#                         else:
#                             continue                     

#                 elif os.path.isfile(path+d+'\\'+i):
#                     _, extension = os.path.splitext(i)
#                     if extension == '.txt':
#                         with open(path+d+'\\'+i, 'r', encoding='UTF-8') as txt_f:
#                             l = txt_f.readlines()
                            
#                             for line in l:
#                                 lines.append(line)

#                         file_list_of_txt_extension.append(i)            
#                 else:
#                     continue            

#         elif os.path.isfile(path+d):
#             _, extension = os.path.splitext(d)
#             if extension == '.txt':
#                 with open(path+d, 'r', encoding='UTF-8') as txt_f:
#                     l = txt_f.readlines()
#                     for line in l:
#                         lines.append(line)

#                 file_list_of_txt_extension.append(d)            
#         else:
#             continue


#     return lines


# def save_to_new_txt_file(list:list, path:str):
#     """Saveing all txt files in one new txt file

#     Args:
#         list (list): Of txt files
#         path (str): path for saving new txt file
#     """
    

#     files_list = list
#     file_path = path + 'scalone.txt'
#     with open(file_path, 'w' , encoding='UTF-8') as f:
#         for file in files_list: 
#             f.write(file)
    




# path = 'C:\\Users\\FiFka9\\desktop\\Nauka_IT\\'
# txt_files = (find_all_txt_file_in_catalog(path))

# save_to_new_txt_file(txt_files, path)




# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Search catalog for all extensions and print them and save in csv file

# import os, csv


# path_to_search = 'C:\\Users\\FiFka9\\desktop\\Nauka_IT\\'


# dir_of_extensions = {}

# data = os.listdir(path_to_search)

# for data_a in data:
#     if os.path.isdir(path_to_search + data_a):
#         for data_b in os.listdir(path_to_search + data_a):
#             if os.path.isdir(path_to_search + data_a + '\\' + data_b):
#                 for data_c in os.listdir(path_to_search + data_a + '\\' + data_b):
#                     if os.path.isdir(path_to_search + data_a + '\\' + data_b + '\\' + data_c):
#                         for data_d in os.listdir(path_to_search + data_a + '\\' + data_b + '\\' + data_c):
#                             if os.path.isdir(path_to_search + data_a + '\\' + data_b + '\\' + data_c + '\\' + data_d):
#                                 continue

#                             elif os.path.isfile(path_to_search + data_a + '\\' + data_b + '\\' + data_c + '\\' + data_d):
#                                 (_, extension) = os.path.splitext(data_d)
#                                 if extension[1:] not in dir_of_extensions.keys():
#                                     dir_of_extensions[extension[1:]] = 1
#                                 else:
#                                     dir_of_extensions[extension[1:]] += 1 

#                             else:
#                                 continue

#                     elif os.path.isfile(path_to_search + data_a + '\\' + data_b + '\\' + data_c):
#                         (_, extension) = os.path.splitext(data_c)
#                         if extension[1:] not in dir_of_extensions.keys():
#                             dir_of_extensions[extension[1:]] = 1
#                         else:
#                             dir_of_extensions[extension[1:]] += 1    
                    
#                     else:
#                         continue

#             elif os.path.isfile(path_to_search + data_a + '\\' + data_b):
#                 (_, extension) = os.path.splitext(data_b)
#                 if extension[1:] not in dir_of_extensions.keys():
#                     dir_of_extensions[extension[1:]] = 1
#                 else:
#                     dir_of_extensions[extension[1:]] += 1  
            
#             else:
#                 continue
    
#     elif os.path.isfile(path_to_search + data_a):
#         (_, extension) = os.path.splitext(data_a)
#         if extension[1:] not in dir_of_extensions.keys():
#             dir_of_extensions[extension[1:]] = 1
#         else:
#             dir_of_extensions[extension[1:]] += 1 

#     else:
#         continue

# sorted_dir_of_extensions = sorted(dir_of_extensions.items(), key=lambda x: x[1], reverse=True)

# sorted_dir_of_extensions = dict(sorted_dir_of_extensions)
# # print(sorted_dir_of_extensions)

# with open('csv_all_extensions.csv', 'w', encoding='UTF-8', newline='') as f:
#     headers = ['filetype;quantity']
#     writer = csv.writer(f)
#     writer.writerow(headers)    
#     for key in sorted_dir_of_extensions.keys():
#         f.write(f"{key};{sorted_dir_of_extensions[key]}\n")


# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Weather Program. Get Weather Information And Save Data To SQLITE

# # DONE


# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


