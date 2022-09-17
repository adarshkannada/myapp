import os
import shutil


def copy_common_files(path_to_files: str, path_to_source_folder: str, path_to_destination_folder: str):
    path_to_files = path_to_files
    list_of_files_in_source = os.listdir(path_to_files)
    print(list_of_files_in_source, sep='\n')

    path_to_source_folder = path_to_source_folder
    list_of_all_files = os.listdir(path_to_source_folder)
    print(list_of_all_files, sep='\n')
    path_to_destination_folder = path_to_destination_folder

    # getting common photos between two location
    c = set(list_of_files_in_source) & set(list_of_all_files)
    s = list(c)
    print('the number of common photos: ', len(c))

    # create destination folder if it is not present
    is_present = os.path.exists(path_to_destination_folder)
    if not is_present:
        os.makedirs(path_to_destination_folder)

    # copying the photos from source to destination
    for element in range(0, len(s)):
        shutil.copy(path_to_source_folder + str(s[element]), path_to_destination_folder + str(s[element]))
    print("Files are copied successfully")


copy_common_files(path_to_files="path",
                  path_to_source_folder="path",
                  path_to_destination_folder="path")
