import tarfile
import os

# tar = tarfile.open("sample.tar.gz","w:gz")
tar = tarfile.open("sample.tar","w")
tar.add("C:\\Users\\135670\\Vijay\\poc-code\\amvijay.github.io")
tar.close

# 500 MB
CHUNK_SIZE_BYTES = 500 * ((1 * 1024) * 1024)
file_number = 1
with open("sample.tar", mode="rb") as f:
    chunk = f.read(CHUNK_SIZE_BYTES)
    while chunk:
        with open("sample.tar" + str(file_number), mode="wb") as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE_BYTES)

file_number = 1
with open("sample-merged.tar",mode="ab") as merged_file:
    while os.path.exists("sample.tar"+str(file_number)):
        print("sample.tar"+str(file_number) + "reading the file")
        with open("sample.tar" + str(file_number), mode="rb") as chunk_file:
            merged_file.write(chunk_file.read())
            file_number = file_number + 1
