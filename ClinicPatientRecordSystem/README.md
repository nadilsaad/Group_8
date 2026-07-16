# Clinic Patient Records System

## Objective
Apply Django fundamentals to design and build a multi-app web application,
covering:
* Setting up a Python virtual environment and installing Django
* Creating a Django project and multiple related applications
* Designing models and relationships using the Django ORM
* Registering applications and connecting URL configurations
* Using the Django admin interface to manage application data
* Designing an Entity Relationship Diagram (ERD) before implementation

## What was done
Built a **Clinic Patient Records System** using Django, made up of four
apps that mirror the real entities of a clinic:

1. **patients** — stores patient bio-data (name, date of birth, gender,
   contact info, blood group, emergency contact)
2. **doctors** — stores doctor profiles (name, specialization, license
   number, contact info)
3. **appointments** — schedules appointments, linking a patient to a
   doctor with a date, reason, and status
4. **medicalrecords** — stores diagnosis, treatment, prescription, and
   notes for each visit, linked to a patient, a doctor, and optionally the
   related appointment

The project includes:
* A Python virtual environment with Django installed and verified
  (`python -m django --version`)
* Four Django apps, each registered inside `INSTALLED_APPS` in
  `settings.py`
* A `urls.py` in every app, connected to the project's root `urls.py`
  using `include()`
* A simple `HttpResponse` view in each app plus a project-level home page
  linking all modules, verified by running the development server
* Models for all four entities with primary keys and foreign key
  relationships (Patient ↔ Appointment ↔ Doctor, and Patient/Doctor ↔
  Medical Record), all registered in the Django admin
* An Entity Relationship Diagram (`docs/ERD.pdf`) showing entities,
  attributes, primary keys, and relationship cardinalities
* A superuser account created via `python manage.py createsuperuser` to
  access and manage data through `/admin/`

## Challenges faced
* Deciding how to split the system into separate apps versus one single
  app, and settling on four apps that map cleanly to the ERD entities
* Getting foreign key relationships right across apps (Appointment and
  Medical Record both depend on Patient and Doctor), and importing models
  between apps without circular imports
* Correctly wiring each app's `urls.py` into the project's root
  `urls.py` using `include()`
* Making the `appointment` field on Medical Record optional
  (`null=True, blank=True`) since not every record originates from a
  scheduled appointment
* Translating the ERD cardinalities (1‑to‑M and 1‑to‑0..1) accurately
  into Django model fields
* Keeping migrations consistent across four interdependent apps

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



## Members Participated

See [`docs/group_members.pdf`](docs/group_members.pdf).
