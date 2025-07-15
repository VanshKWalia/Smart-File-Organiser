from db.connection import get_connection

def setup_database():
    con = get_connection()
    cursor = con.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS Smart_File_Organiser")
    cursor.execute("USE Smart_File_Organiser")

    # Drop and recreate Sorter table with timestamp
    cursor.execute("DROP TABLE IF EXISTS Sorter")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sorter (
            Name CHAR(200),
            Type VARCHAR(20),
            Extensions VARCHAR(10),
            SortedAt DATETIME
        )
    """)

    con.commit()
    con.close()
