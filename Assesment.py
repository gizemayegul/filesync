import os
import shutil
import datetime
import logging
import time
import sys
#folder paths arg

source_folder = sys.argv[1]
replica_folder=sys.argv[2]
logfile_path = sys.argv[3]

#time interval
time_interval =sys.argv[4]
# set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',handlers=[
        logging.FileHandler(f'{logfile_path}/logfile.log'),
        logging.StreamHandler()
    ])

logging.info(f'Synchronization Starting...')

#create copy of source folder
if not os.path.exists(replica_folder):
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
        else:
            if not os.path.exists(dest):
                shutil.copy2(src,dest)
                logging.info(f'File copied: {src} to {dest}')
    for f in replica_files:
        src = os.path.join(source_folder, f)
        dest = os.path.join(replica_folder, f)
        if not os.path.exists(src):
            if os.path.isdir(dest):
                shutil.rmtree(dest)
                logging.info(f'Folder removed: {dest}')
            else:
                os.remove(dest)
                logging.info(f'File removed: {dest}')
while True:
    sync_folders(source_folder, replica_folder)
    time.sleep(int(time_interval))
