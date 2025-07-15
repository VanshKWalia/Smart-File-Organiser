import os
from tkinter import Tk
from tkinter import filedialog
from utils.sorter import sort_files
from db.setup import setup_database

def choose_folder():
    root = Tk()
    root.withdraw()  # Hide the root Tkinter window
    folder_selected = filedialog.askdirectory(title="📂 Choose folder to sort")
    return folder_selected

if __name__ == "__main__":
    print("📁 Smart File Organiser Launched")
    
    # Ask user to choose folder
    target_path = choose_folder()

    if not target_path:
        print("❌ No folder selected. Exiting.")
        exit()

    # Switch to target folder
    os.chdir(target_path)
    print(f"✅ Working in: {target_path}")

    # Setup DB & start sorting
    setup_database()
    sort_files()
    print("🎉 Done! Files sorted.")
