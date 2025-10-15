# Used for interacting with the operating system, such as accessing files and directories.
import os
# Provides high-level file operations, including copying files and directories.
import shutil
# Helps manage timestamps for naming backup files and directories.
import datetime

import logging

import schedule
import time

# Set up logging
logging.basicConfig(filename='backup_log.txt',
                    level=logging.INFO, format='%(asctime)s - %(message)s')


def backup_files(source_dir, backup_dir):
    # Get the current date and time for naming the backup folder
    current_time = datetime.datetime.now().strftime('%S-%M-%H_%d-%m-%Y')
    # current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = os.path.join(backup_dir, f"backup_{current_time}")

    try:
        # Create the backup directory
        os.makedirs(backup_folder)

        # Copy all files and subdirectories from source to backup folder
        shutil.copytree(source_dir, backup_folder)

        print(f"Backup successful! Files have been copied to {backup_folder}")

    except Exception as e:
        print(f"Error: {e}")


# Function to preform schduled backup

def job():
    source_directory = '/path/to/source'
    backup_directory = '/path/to/backup'
    backup_files(source_directory, backup_directory)


schedule.every().day.at("02:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
