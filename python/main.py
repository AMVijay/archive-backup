"""
-author - Vijay/am.vijay@gmail.com/Vijayaraaghavan Manoharan
"""
import os, shutil
from createtar import create_tar,separate_tar_file

working_folder = os.getcwd() + "/test/"
backup_folder = ""

print("Current working directory :: " + working_folder)
# if(os.path.exists(working_folder)):
#     shutil.rmtree(working_folder)
os.mkdir(working_folder)
tar_file = create_tar(backup_folder, working_folder)
print("Created tar file")
separate_tar_file(tar_file)
print("Tar files are separated")