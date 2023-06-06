import psycopg2

connection = psycopg2.connect(
    database="Hackathon_1",
    user='postgres',
    password='1948',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()