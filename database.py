import sqlite3

def get_connection():
    conn = sqlite3.connect("id_and_passwd.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
