"""
-author - Vijay/am.vijay@gmail.com/Vijayaraaghavan Manoharan
"""
import tarfile
from os import path

# Method to create tar file in backup process
def create_tar(folder_path,working_folder):
    if path.isdir(folder_path):
        tar_file_path = working_folder + path.basename(folder_path) + ".tar"
        print("tar_file_path :: " + tar_file_path)
        print("folder path :: " + folder_path)
        tar_file = tarfile.open(tar_file_path,"w")
        tar_file.add(folder_path)
        tar_file.close()
        return tar_file_path
    else:
        return Exception(str(folder_path) + " is not a valid folder")

# Separates the tar file into multiple chunks
def separate_tar_file(tar_file_path):
    # 100 MB
    CHUNK_SIZE_BYTES = 100 * ((1 * 1024) * 1024)
    chunk_index = 1
    if(tarfile.is_tarfile(tar_file_path)):
        with open(tar_file_path, mode="rb") as file_reader:
            chunk = file_reader.read(CHUNK_SIZE_BYTES)
            while chunk:
                with open(tar_file_path + str(chunk_index), mode="wb") as chunk_file:
                    chunk_file.write(chunk)
                chunk_index = chunk_index + 1
                chunk = file_reader.read(CHUNK_SIZE_BYTES)
    else:
        return Exception(str(tar_file_path) + " is not a valid tar filer")
