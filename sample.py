import os
import sqlite3

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def fetch_user_record(user_id: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Fixed SQL injection using parameterized query
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def calculate_discount(price: float, discount_rate: float):
    # Fixed division by zero when discount_rate is 0
    if discount_rate == 0:
        return price
    return price * (1 - discount_rate)
