import os
import sqlite3
def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchall()
def run(cmd):
    os.system(cmd)
SECRET_KEY = "test-secret-key-12345"
password = "admin123"
