# utils/file_utils.py

import os

def create_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_file(folder, files):
    for file in files:
        if os.path.isdir(file):
            continue
        destination = os.path.join(folder, os.path.basename(file))
        if not os.path.exists(destination):
            os.replace(file, destination)
