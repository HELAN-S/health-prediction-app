import sqlite3

DB_NAME = "patient.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            email TEXT NOT NULL,
            glucose REAL NOT NULL,
            haemoglobin REAL NOT NULL,
            cholesterol REAL NOT NULL,
            remarks TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_patient(full_name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients
        (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()
    conn.close()


def get_all_patients():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()

    conn.close()
    return data


def delete_patient(patient_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()


def update_patient(
        patient_id,
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE patients
        SET full_name=?,
            dob=?,
            email=?,
            glucose=?,
            haemoglobin=?,
            cholesterol=?,
            remarks=?
        WHERE id=?
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks,
        patient_id
    ))

    conn.commit()
    conn.close()