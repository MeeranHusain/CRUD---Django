# Django CRUD Application

This is a simple **CRUD (Create, Read, Update, Delete)** web application built using **Python** and **Django**. It allows users to manage entries (such as students, employees, etc.) by performing basic database operations through a user-friendly interface.

## Features

- Add new entries
- View a list of all entries
- Update existing entries
- Delete entries
- Bootstrap for basic styling

## Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default DB)
- HTML, CSS, Bootstrap (for UI)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MeeranHusain/CRUD---Django.git
cd CRUD---Django
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
If requirements.txt is missing, you can install Django manually:
```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```


License
This project is open-source and available under the MIT License.

Made with ❤️ using Django
