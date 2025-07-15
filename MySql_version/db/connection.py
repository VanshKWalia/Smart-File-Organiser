# db/connection.py

from mysql.connector import connect
from config import DB_CONFIG

def get_connection():
    return connect(**DB_CONFIG)
