# 🚀 Smart File Organiser

A modern Python desktop app that automatically organises your messy folders into clean categories like **Images**, **Docs**, **Medias**, and **Others** — all with a single click.

This project includes two powerful versions:
- ✅ **SQLite (GUI desktop app with .exe)** — Lightweight, portable, and ready to use
- 🛠️ **MySQL (CLI-based)** — Great for learning database integration and file structuring

---

## 📥 Try the App (No Setup Needed)

> 🧩 Works on any Windows PC — no installation required

🔽 <a href="https://drive.google.com/file/d/1GNbUD0INrie1aGNrc-VXcg8i3pdM8wjP/view?usp=sharing" target="_blank"><b>Download Smart File Organiser (.exe)</b></a>

📁 Just download and double-click to sort your files in seconds.  
💬 Feedback is welcome!

---

## ✨ Features

- 🔄 Automatically detects & moves files from any messy folder
- 🗂 Organises into: `Images`, `Docs`, `Medias`, `Others`
- 🔒 Ignores subfolders — doesn’t disturb nested folder structure
- 💾 Logs every action (either in a database or log file)
- 🧠 Clean, modular code — ready for future GUI/API extensions
- 📦 Built with both SQLite and MySQL support

---

## 🧑‍💻 Versions Included

### 🟢 `sqlite-version/` – GUI Desktop App

| Feature            | Description                                     |
|--------------------|-------------------------------------------------|
| Interface          | Clean GUI built with `CustomTkinter`            |
| DB Used            | `SQLite` (embedded local database)              |
| Packaging          | Compiled to `.exe` using `PyInstaller`          |
| Portability        | Fully standalone — no installation needed       |
| Use Case           | Ideal for end-users, students, and demos        |

### 🔵 `mysql-version/` – CLI Terminal App

| Feature            | Description                                     |
|--------------------|-------------------------------------------------|
| Interface          | Text-based menu (command-line)                  |
| DB Used            | `MySQL` (remote/local database setup required)  |
| Logging            | Tracks file info: name, extension, category     |
| Use Case           | Ideal for backend learning, DB practice, DSA    |

---

## 🧠 How It Works (Common Flow)

1. Select a folder
2. App scans files in that folder
3. Sorts them into:
   - 📷 `Images/`
   - 📄 `Docs/`
   - 🎞 `Medias/`
   - 📦 `Others/`
4. Stores history in DB (SQLite/MySQL) or `logs.log`
5. ✅ Leaves nested folders untouched

---

## 🛠️ Tech Stack

| Area           | Technology Used                                   |
|----------------|----------------------------------------------------|
| Language       | Python 3.10+                                       |
| GUI Framework  | `CustomTkinter`, `Tkinter`                         |
| DB (v1)        | SQLite (`sqlite3`)                                 |
| DB (v2)        | MySQL (`mysql-connector-python`)                   |
| Packaging      | `PyInstaller` for `.exe` generation                |
| Others         | `os`, `shutil`, `logging`, `schedule`              |

---

## 🗂 Project Structure

