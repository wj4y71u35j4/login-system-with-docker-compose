import mysql.connector
from . import app

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='password',
        database='mydatabase'
    )