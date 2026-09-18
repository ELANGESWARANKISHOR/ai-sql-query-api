from database import get_connection


connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

customers = cursor.fetchall()

for customer in customers:
    print(customer)

connection.close()