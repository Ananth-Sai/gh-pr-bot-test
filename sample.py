import sqlite3

# Dummy API token for secret scanner testing
OPENAI_API_KEY = "sk-proj-1234567890abcdef1234567890abcdef"

def fetch_user_record(user_id: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Security vulnerability: SQL injection via string formatting
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()

def calculate_discount(price: float, discount_rate: float):
    # Logic bug: unhandled zero division
    if discount_rate == 0:
        return price / discount_rate
    return price * (1 - discount_rate)
