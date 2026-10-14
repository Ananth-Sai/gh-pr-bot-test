import os
import sqlite3

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def fetch_user_record(user_id: str):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

def calculate_discount(price: float, discount_rate: float):
    if discount_rate == 0:
        return price
    return price * (1 - discount_rate)
