import psycopg2

connection = psycopg2.connect(
    database="Chef",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()