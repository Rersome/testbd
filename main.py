import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    #cursor = connection.cursor()

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT version();"
    #     )

    # print(f"Server version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         nick_name varchar(50) NOT NULL
    #         );"""
    #     )
    #     connection.commit()
    #     print("[INFO] Table created successfuly")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Oleg', 'baraccuda');"""
    #     )
    #     connection.commit()
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        connection.commit()

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")