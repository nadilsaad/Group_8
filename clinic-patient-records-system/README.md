# Clinic Patient Records System

A Django-based web application for managing patient records at a clinic. The
system keeps track of **patients**, **doctors**, **appointments**, and
**medical records**, and exposes an admin dashboard for staff to manage all
clinic data from one place.

This project was built as part of a group assignment to demonstrate the
fundamentals of Django project/app structure, models, the Django ORM, URL
routing, and the built-in admin interface.

## Project Description

The Clinic Patient Records System digitizes the day-to-day record keeping of
a small to medium-sized clinic. Front-desk and medical staff can:

- Register new patients and keep their demographic and contact details.
- Maintain a roster of doctors and their specializations.
- Schedule and track appointments between patients and doctors.
- Record diagnoses, treatments, prescriptions, and notes for every visit
  through medical records linked to a patient, a doctor, and (optionally)
  the appointment during which the record was created.

## Apps in this Project

| App | Purpose |
|---|---|
| `patients` | Manages patient bio-data (name, DOB, gender, contact info, blood group, emergency contact). |
| `doctors` | Manages doctor profiles (name, specialization, license number, contact info). |
| `appointments` | Schedules and tracks appointments between patients and doctors, including status (scheduled, completed, cancelled, no-show). |
| `medicalrecords` | Stores diagnosis, treatment, prescription, and notes for each patient visit. |

## Entity Relationship Diagram

See [`docs/ERD.pdf`](docs/ERD.pdf) for the full ERD. Summary of relationships:

- A **Patient** can have many **Appointments** and many **Medical Records** (1‑to‑M).
- A **Doctor** can attend many **Appointments** and author many **Medical Records** (1‑to‑M).
- An **Appointment** may optionally result in one **Medical Record** (1‑to‑0..1).

## Tech Stack

- Python 3.12
- Django 6.0
- SQLite (default development database)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd clinic-patient-records-system
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify the Django installation**
   ```bash
   python -m django --version
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open the application in your browser**
   - Home page: http://127.0.0.1:8000/
   - Patients module: http://127.0.0.1:8000/patients/
   - Doctors module: http://127.0.0.1:8000/doctors/
   - Appointments module: http://127.0.0.1:8000/appointments/
   - Medical Records module: http://127.0.0.1:8000/medicalrecords/
   - Admin dashboard: http://127.0.0.1:8000/admin/

## Project Structure

```
clinic-patient-records-system/
│── README.md
│── requirements.txt
│── manage.py
│── clinic_system/        # Project configuration (settings, root urls)
│── patients/              # Patient app
│── doctors/                # Doctor app
│── appointments/          # Appointment app
│── medicalrecords/        # Medical record app
│── docs/
│    ├── ERD.pdf
│    └── group_members.pdf
```

## Group Members

See [`docs/group_members.pdf`](docs/group_members.pdf).
