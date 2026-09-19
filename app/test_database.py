from database import get_connection


connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
    SELECT
        c.name,
        SUM(o.quantity * p.price) AS total_spending
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
    GROUP BY c.id
    ORDER BY total_spending DESC
""")

customers = cursor.fetchall()

for customer in customers:
    print(customer)

connection.close()