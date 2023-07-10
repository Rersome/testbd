CREATE TABLE IF NOT EXISTS students (
    id INTEGER NOT NULL PRIMARY KEY,
    student_name TEXT,
);

CREATE TABLE IF NOT EXISTS houses (
    house TEXT NOT NULL PRIMARY KEY,
    head TEXT,
);

CREATE TABLE IF NOT EXISTS house_assigments (
    student_id INTEGER NOT NULL,
    house_id TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(house),
    PRIMARY KEY(student_id, house_id)
);