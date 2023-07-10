CREATE TABLE IF NOT EXISTS students (
    id INT NOT NULL,
    student_name VARCHAR ( 50 ),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS houses (
    house VARCHAR ( 50 ) NOT NULL,
    head VARCHAR ( 50 ),
    PRIMARY KEY(house)
);

CREATE TABLE IF NOT EXISTS house_assigments (
    student_id INT NOT NULL,
    house_id VARCHAR ( 50 ) NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(house),
    PRIMARY KEY(house_id, student_id)
);"""