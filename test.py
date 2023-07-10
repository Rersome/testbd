import psycopg2
from config import host, user, password, db_name
import csv

students = []

with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
        #print(students)

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    print(students)
    for student in students:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO students(id, student_name) VALUES(%s,%s)
                ON CONFLICT DO NOTHING;""",
                (student["id"],
                student["student_name"])
                )
            cursor.execute("""
                INSERT INTO houses(house, head) VALUES(%s,%s)
                ON CONFLICT DO NOTHING;""",
                (student["house"],
                student["head"])
                )
            cursor.execute("""
                INSERT INTO house_assigments(student_id, house_id) VALUES(%s,%s)
                ON CONFLICT DO NOTHING;""",
                (student["id"],
                student["house"])
                )
            connection.commit()

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         CREATE TABLE IF NOT EXISTS students (
    #             id INT NOT NULL,
    #             student_name VARCHAR ( 50 ),
    #             PRIMARY KEY(id)
    #         );

    #         CREATE TABLE IF NOT EXISTS houses (
    #             house VARCHAR ( 50 ) NOT NULL,
    #             head VARCHAR ( 50 ),
    #             PRIMARY KEY(house)
    #         );

    #         CREATE TABLE IF NOT EXISTS house_assigments (
    #             student_id INT NOT NULL,
    #             house_id VARCHAR ( 50 ) NOT NULL,
    #             FOREIGN KEY(student_id) REFERENCES students(id),
    #             FOREIGN KEY(house_id) REFERENCES houses(house),
    #             PRIMARY KEY(house_id, student_id)
    #             );"""
    #     )
    # connection.commit()
    # with connection.cursor() as cursor:
    #      cursor.execute(
    #             """
    #             DROP TABLE students, houses, house_assigments;
    #             """)
    #      connection.commit()

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")