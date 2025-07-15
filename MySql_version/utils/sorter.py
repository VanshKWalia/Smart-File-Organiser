import os
from datetime import datetime
from utils.file_utils import create_if_not_exists, move_file
from db.connection import get_connection
from utils.logger import log_info, log_error

def sort_files():
    con = get_connection()
    cursor = con.cursor()

    try:
        files = os.listdir()

        folders = ['Images', 'Docs', 'Medias', 'Others']
        for folder in folders:
            create_if_not_exists(folder)

        categories = {
            'Images': ['.png', '.jpg', '.jpeg', '.gif', '.jfif', '.tiff'],
            'Docs': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
            'Medias': ['.mp3', '.mp4', '.mkv', '.avi']
        }

        for cat, exts in categories.items():
            matched = []
            for file in files[:]:
                ext = os.path.splitext(file)[1].lower()
                if ext in exts:
                    matched.append(file)
                    name = os.path.splitext(file)[0]
                    sorted_at = datetime.now()

                    cursor.execute(
                        "INSERT INTO Sorter (Name, Type, Extensions, SortedAt) VALUES (%s, %s, %s, %s)",
                        (name, cat[:-1], ext, sorted_at)
                    )

            move_file(cat, matched)
            files = [f for f in files if f not in matched]

        # Remaining files go to Others
        move_file("Others", files)
        for file in files:
            name = os.path.splitext(file)[0]
            ext = os.path.splitext(file)[1].lower()
            sorted_at = datetime.now()
            cursor.execute(
                "INSERT INTO Sorter (Name, Type, Extensions, SortedAt) VALUES (%s, %s, %s, %s)",
                (name, 'Others', ext, sorted_at)
            )

        con.commit()
        log_info("Sorting complete.")

    except Exception as e:
        log_error(f"Sorting failed: {e}")
    finally:
        cursor.close()
        con.close()
