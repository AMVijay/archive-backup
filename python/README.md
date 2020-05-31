# Design

* Create a compressed tar file for the specified folder
* Split the tar file into multiple chunks based on configured size (assume 100 MB)
* Read each of the compressed tar file chunk content and write new file using cryptography fernet.
* Move all these files to AWS Glacier 

* Retrive the multiple chunks from AWS Glacier
* Using Fernet decrypt the file into compressed the tar file.
* Merge the tar files into single compressed tar file.
* Unzip and Create Folder.
