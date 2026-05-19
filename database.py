import sqlite3

def create_table():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        merchant TEXT,
        amount REAL,
        date TEXT,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_expense(merchant, amount, date, category):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses
    (merchant, amount, date, category)
    VALUES (?, ?, ?, ?)
    """, (merchant, amount, date, category))

    conn.commit()
    conn.close()


def get_all_expenses():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    data = cursor.fetchall()

    conn.close()

    return data