import os
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from utils.sorter import sort_files
from db.setup import setup_database
from db.connection import get_connection

# App UI Setup
ctk.set_appearance_mode("System")  # or "Light"/"Dark"
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("📂 Smart File Organiser - SDE Level")
app.geometry("600x450")
app.resizable(False, False)

# Title Label
title_label = ctk.CTkLabel(app, text="Smart File Organiser", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# 🔹 Function: Browse folder and sort files
def browse_and_sort():
    folder_path = filedialog.askdirectory()
    if folder_path:
        try:
            os.chdir(folder_path)
            setup_database()
            sort_files()
            messagebox.showinfo("✅ Done", "Files sorted and saved to database.")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Something went wrong:\n{e}")
    else:
        messagebox.showwarning("⚠️ No Folder", "Please select a folder to sort.")

# 🔹 Function: Display sorted records
def show_records():
    try:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Sorter")
        records = cursor.fetchall()
        con.close()

        # Create new window for displaying records
        record_win = tk.Toplevel()
        record_win.title("📊 Sorted File Records")
        record_win.geometry("700x450")
        record_win.configure(bg="#f5f5f5")

        # Heading
        heading = tk.Label(record_win, text="📁 All Sorted Files", font=("Arial", 18, "bold"), bg="#f5f5f5")
        heading.pack(pady=10)

        # Scrollable table
        frame = tk.Frame(record_win)
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        yscroll = tk.Scrollbar(frame, orient="vertical")
        yscroll.pack(side="right", fill="y")

        xscroll = tk.Scrollbar(frame, orient="horizontal")
        xscroll.pack(side="bottom", fill="x")

        tree = ttk.Treeview(
            frame,
            columns=("Name", "Type", "Ext", "SortedAt"),
            show="headings",
            yscrollcommand=yscroll.set,
            xscrollcommand=xscroll.set
        )

        tree.heading("Name", text="📄 File Name")
        tree.heading("Type", text="🗂️ Category")
        tree.heading("Ext", text="📎 Extension")
        tree.heading("SortedAt", text="🕒 Sorted At")

        tree.column("Name", width=250, anchor="w")
        tree.column("Type", width=100, anchor="center")
        tree.column("Ext", width=100, anchor="center")
        tree.column("SortedAt", width=200, anchor="center")

        yscroll.config(command=tree.yview)
        xscroll.config(command=tree.xview)

        # Style
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", font=("Arial", 11), rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        # Insert data
        for row in records:
            tree.insert("", tk.END, values=row)

        tree.pack(fill="both", expand=True)

    except Exception as e:
        messagebox.showerror("❌ Error", f"Couldn't load records:\n{e}")

# 🔘 Buttons
browse_btn = ctk.CTkButton(app, text="📁 Choose Folder & Sort", font=("Arial", 16), command=browse_and_sort, corner_radius=10)
browse_btn.pack(pady=20)

record_btn = ctk.CTkButton(app, text="📊 Show Records", font=("Arial", 16), command=show_records, corner_radius=10)
record_btn.pack(pady=10)

exit_btn = ctk.CTkButton(app, text="Exit", command=app.destroy, fg_color="gray", hover_color="red")
exit_btn.pack(pady=20)

# Run the app
app.mainloop()
