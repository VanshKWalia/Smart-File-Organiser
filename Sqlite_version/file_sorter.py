import os
import shutil
import sqlite3
from datetime import datetime

# File categories
FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv'],
    "PDFs": ['.pdf'],
    "Documents": ['.docx', '.doc', '.txt', '.odt', '.pptx', '.xlsx'],
    "Others": []
}

def init_db():
    conn = sqlite3.connect("sorter.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sorted_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            file_type TEXT,
            original_path TEXT,
            sorted_path TEXT,
            sorted_on TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_record(file_name, file_type, original_path, sorted_path):
    conn = sqlite3.connect("sorter.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO sorted_files (file_name, file_type, original_path, sorted_path, sorted_on)
        VALUES (?, ?, ?, ?, ?)
    ''', (file_name, file_type, original_path, sorted_path, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def get_file_category(file_ext):
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def sort_files_in_directory(folder_path):
    init_db()
    summary = {cat: 0 for cat in FILE_CATEGORIES}
    summary["Others"] = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1]
            category = get_file_category(ext)
            target_dir = os.path.join(folder_path, category)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            dest_path = os.path.join(target_dir, file)
            shutil.move(file_path, dest_path)
            insert_record(file, category, folder_path, dest_path)
            summary[category] += 1
    return summary
