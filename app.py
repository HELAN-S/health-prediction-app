import streamlit as st
import pandas as pd
from datetime import date

from database import (
    create_table,
    add_patient,
    get_all_patients,
    update_patient,
    delete_patient
)

from validation import (
    is_valid_email,
    is_valid_dob
)

from ai_service import generate_health_remark


create_table()

st.set_page_config(
    page_title="Health Prediction App",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Health Prediction Application")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Add Patient",
        "View Patients",
        "Update Patient",
        "Delete Patient"
    ]
)

# ==========================
# ADD PATIENT
# ==========================

if menu == "Add Patient":

    st.header("Add Patient")

    full_name = st.text_input("Full Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0
    )

    if st.button("Generate & Save"):

        if not is_valid_email(email):
            st.error("Invalid Email Address")

        elif not is_valid_dob(dob):
            st.error("Date of Birth cannot be in future")

        else:

            with st.spinner("Generating AI Health Remark..."):

                remarks = generate_health_remark(
                    glucose,
                    haemoglobin,
                    cholesterol
                )

            add_patient(
                full_name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success("Patient Saved Successfully")

            st.text_area(
                "Generated Remarks",
                remarks,
                height=120
            )

# ==========================
# VIEW PATIENTS
# ==========================

elif menu == "View Patients":

    st.header("Patient Records")

    data = get_all_patients()

    if data:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Full Name",
                "DOB",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No Records Found")

# ==========================
# UPDATE PATIENT
# ==========================

elif menu == "Update Patient":

    st.header("Update Patient")

    data = get_all_patients()

    if not data:
        st.warning("No records available")
        st.stop()

    ids = [row[0] for row in data]

    selected_id = st.selectbox(
        "Select Patient ID",
        ids
    )

    patient = None

    for row in data:
        if row[0] == selected_id:
            patient = row
            break

    full_name = st.text_input(
        "Full Name",
        value=patient[1]
    )

    dob = st.date_input(
        "Date of Birth",
        value=date.fromisoformat(patient[2])
    )

    email = st.text_input(
        "Email",
        value=patient[3]
    )

    glucose = st.number_input(
        "Glucose",
        value=float(patient[4])
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        value=float(patient[5])
    )

    cholesterol = st.number_input(
        "Cholesterol",
        value=float(patient[6])
    )

    if st.button("Update Record"):

        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        update_patient(
            selected_id,
            full_name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Patient Updated Successfully")

# ==========================
# DELETE PATIENT
# ==========================

elif menu == "Delete Patient":

    st.header("Delete Patient")

    data = get_all_patients()

    if not data:
        st.warning("No records available")
        st.stop()

    ids = [row[0] for row in data]

    selected_id = st.selectbox(
        "Select Patient ID",
        ids
    )

    if st.button("Delete Record"):

        delete_patient(selected_id)

        st.success("Patient Deleted Successfully")