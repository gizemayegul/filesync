import os
import shutil
import datetime
import logging
import time

#create a folder
if not os.path.exists('source_folder'):
    os.mkdir('source_folder')

# set up logging
logging.basicConfig(filename='file_operations.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#folder pathsf

source_directory =os.getcwd()
myfolder_path = os.path.join(source_directory,'source_folder')
file_path = os.path.join(myfolder_path,'myfile.txt')
file_path2 = os.path.join(myfolder_path,'myfile2.txt')
replica_path=os.path.join(source_directory,'replica_folder')

#create a file inside the source folder
with open(file_path,'w') as f:
    f.write('HelloWorld')

    logging.info(f'File created: {file_path}')
with open(file_path2,'w') as f:
    f.write('HelloWorld')
    logging.info(f'File created: {file_path2}')

#create copy of source foldere

source_folder = myfolder_path
replica_folder = replica_path
shutil.copytree(source_folder,replica_folder)
logging.info(f'Folder copied: {source_folder} to {replica_folder}')

#sync


def sync_folders(source_folder,replica_folder):
    source_files =os.listdir(source_folder)
    replica_files=os.listdir(replica_folder)

    for f in source_files:
        src=os.path.join(source_folder,f)
        dest=os.path.join(replica_folder,f)
        if os.path.isdir(src):
            if not os.path.exists(dest):
                os.mkdir(dest)
                logging.info(f'Folder created: {dest}')
            sync_folders(src,dest)
        else:
            if not os.path.exists(dest):
                shutil.copy2(src,dest)
                logging.info(f'File copied: {src} to {dest}')
    for f in replica_files:
        src = os.path.join(replica_folder, f)
        dest = os.path.join(source_folder, f)
        if not os.path.exists(src):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
                logging.info(f'Folder removed: {dest}')
            else:
                os.remove(dest)
                logging.info(f'File removed: {dest}')
   
while True:
    sync_folders(myfolder_path, replica_path)
    time.sleep(3)
