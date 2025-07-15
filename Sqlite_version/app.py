import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import sqlite3
from file_sorter import sort_files_in_directory

# ------------------ DB Init ------------------ #
def init_database():
    conn = sqlite3.connect("sorter.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sorted_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            file_type TEXT,
            original_path TEXT,
            sorted_path TEXT,
            sorted_on TEXT
        )
    """)
    conn.commit()
    conn.close()

# ------------------ Fetch History ------------------ #
def fetch_history():
    conn = sqlite3.connect("sorter.db")
    cursor = conn.cursor()
    cursor.execute("SELECT file_name, file_type, original_path, sorted_path, sorted_on FROM sorted_files ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ------------------ Sort Function ------------------ #
def browse_and_sort():
    folder = filedialog.askdirectory()
    if folder:
        status_label.configure(text="🔄 Sorting in progress...", bootstyle="warning")
        app.update_idletasks()

        summary = sort_files_in_directory(folder)
        msg = "\n".join([f"{k}: {v}" for k, v in summary.items()])
        messagebox.showinfo("✅ Sorted", f"Files sorted:\n\n{msg}")

        status_label.configure(text="✅ Sorting done!", bootstyle="success")
        refresh_table()

# ------------------ Refresh History Table ------------------ #
def refresh_table():
    for row in history_table.get_children():
        history_table.delete(row)

    records = fetch_history()
    for rec in records:
        history_table.insert('', 'end', values=rec)

# ------------------ Init App ------------------ #
app = tb.Window(themename="cyborg")
app.title("🗂 Smart File Organiser - Pro Edition")
app.geometry("980x620")
app.resizable(True, True)  # Maximize enabled

# ------------------ Notebook Tabs ------------------ #
notebook = tb.Notebook(app, bootstyle="dark")
notebook.pack(fill=BOTH, expand=YES, padx=30, pady=25)

# ------------------ Tab 1: Sort ------------------ #
tab1 = tb.Frame(notebook)
notebook.add(tab1, text="📁 Sort Files")

tb.Label(tab1, text="Smart File Organiser", font=("Segoe UI", 22, "bold"), bootstyle="success").pack(pady=(30, 10))
tb.Label(tab1, text="Sort your files by type into folders with a single click!",
         font=("Segoe UI", 12), bootstyle="secondary").pack()

tb.Button(tab1, text="📂 Browse Folder", bootstyle="primary outline", command=browse_and_sort).pack(pady=30)

status_label = tb.Label(tab1, text="Waiting for folder selection...", font=("Segoe UI", 10), bootstyle="info")
status_label.pack(pady=(10, 0))

# ------------------ Tab 2: History ------------------ #
tab2 = tb.Frame(notebook)
notebook.add(tab2, text="🕘 View History")

tb.Label(tab2, text="Sorted File History", font=("Segoe UI", 18, "bold"), bootstyle="info").pack(pady=(20, 10))

columns = ("File Name", "Type", "Original Path", "Sorted Path", "Sorted On")
history_table = tb.Treeview(tab2, columns=columns, show="headings", bootstyle="dark", height=18)

for col in columns:
    history_table.heading(col, text=col)
    history_table.column(col, anchor="w", width=180 if col != "Type" else 100)

history_table.pack(fill=BOTH, padx=20, pady=10)

tb.Button(tab2, text="🔄 Refresh Table", bootstyle="secondary outline", command=refresh_table).pack(pady=10)

# ------------------ Start App ------------------ #
init_database()         # ✅ Table ban jaayega agar missing ho
refresh_table()
app.mainloop()
