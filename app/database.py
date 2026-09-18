import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/database.db")


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            country TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    connection.commit()
    connection.close()


def insert_sample_data():
    connection = get_connection()
    cursor = connection.cursor()

    customers = [
        (1, "Kamal Perera", "kamal@example.com", "Sri Lanka"),
        (2, "Sarah Johnson", "sarah@example.com", "USA"),
        (3, "David Smith", "david@example.com", "UK"),
        (4, "Nimal Fernando", "nimal@example.com", "Sri Lanka"),
        (5, "Emma Brown", "emma@example.com", "Australia"),
        (6, "Raj Kumar", "raj@example.com", "India"),
        (7, "Daniel Wilson", "daniel@example.com", "Canada"),
        (8, "Aisha Khan", "aisha@example.com", "Pakistan")
    ]

    products = [
        (1, "Laptop", "Electronics", 1200.00),
        (2, "Wireless Mouse", "Electronics", 35.00),
        (3, "Keyboard", "Electronics", 75.00),
        (4, "Monitor", "Electronics", 300.00),
        (5, "Office Chair", "Furniture", 250.00),
        (6, "Desk Lamp", "Furniture", 45.00),
        (7, "Backpack", "Accessories", 60.00),
        (8, "USB Cable", "Accessories", 15.00)
    ]

    orders = [
        (1, 1, 1, 1, "2026-09-01"),
        (2, 1, 2, 2, "2026-09-02"),
        (3, 2, 4, 1, "2026-09-03"),
        (4, 2, 5, 1, "2026-09-04"),
        (5, 3, 1, 1, "2026-09-05"),
        (6, 3, 3, 2, "2026-09-06"),
        (7, 4, 6, 3, "2026-09-07"),
        (8, 4, 8, 5, "2026-09-08"),
        (9, 5, 2, 3, "2026-09-09"),
        (10, 5, 7, 2, "2026-09-10"),
        (11, 6, 1, 1, "2026-09-11"),
        (12, 6, 4, 2, "2026-09-12"),
        (13, 7, 5, 1, "2026-09-13"),
        (14, 7, 6, 2, "2026-09-14"),
        (15, 8, 3, 1, "2026-09-15"),
        (16, 8, 8, 4, "2026-09-16"),
        (17, 1, 5, 1, "2026-09-17"),
        (18, 2, 2, 2, "2026-09-17"),
        (19, 3, 7, 1, "2026-09-18"),
        (20, 4, 1, 1, "2026-09-18")
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)",
        customers
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)",
        products
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?, ?)",
        orders
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    insert_sample_data()
    print("Database created and sample data inserted.")