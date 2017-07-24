import os   #for file access
import re   #for string processing
import shutil   #for copying files

src_folder = 'provided_photos'
dst_folder = 'processed_photos'

#clean_destination_folder
for file in os.listdir(dst_folder):
    full_filepath = os.path.join(dst_folder, file)
    os.remove(full_filepath)
    
#solve the secret message
list_of_filepaths = os.listdir(src_folder)
for filepath in list_of_filepaths:
    print(filepath)
    filepath_wo_numbers = re.sub('\d+', '', filepath)
    src_path = os.path.join(src_folder, filepath)
    dst_path = os.path.join(dst_folder, filepath_wo_numbers)
    shutil.copy(src_path, dst_path)

