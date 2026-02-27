import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "yourpassword"),
        database=os.getenv("DB_NAME", "placement_tracker")
    )

db = get_db_connection()
cursor = db.cursor(dictionary=True)
