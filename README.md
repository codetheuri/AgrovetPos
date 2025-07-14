# Django Point of Sale (POS) for Agrovet 💸

A simple, clean, and extendable Point of Sale web application built with Python and Django — tailored specifically for Agrovet shops in Kenya and beyond.

Includes **M-Pesa payment integration** using the **Safaricom Daraja sandbox API**.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run It Locally](#run-it-locally)
- [Author](#author)


---

## Features

- 🔐 User authentication (login/logout)
- 📊 Dashboard with charts and stats
- 📋 DataTables with export (PDF, CSV, Print, Copy)
- 📦 Product & Category Management
- 👥 Client Management
- 🧾 Sales Recording
- 💰 M-Pesa Payment (Sandbox Integration)
- 🖥️ Admin-friendly UI

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap, SweetAlert, DataTables
- **Backend**: Python, Django, SQLite
- **Extras**: AJAX, jQuery, M-Pesa Daraja API

---

## Installation

### ✅ Prerequisites

- Python 3.11+ (recommended to use [pyenv](https://github.com/pyenv/pyenv))
- pip (Python package manager)

> ⚠️ **Browser Compatibility**\
> **ALL**

---

### 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/codetheuri/AgrovetPos.git
cd AgrovetPos
```

2. **Create and activate a virtual environment**

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```


3. **Install dependencies**

```bash
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

---

## Run It Locally

1. Make sure you're in the project root directory:

```bash
cd AgrovetPos
source venv/bin/activate
```

2. Go to the Django project folder:

```bash
cd django_pos
```

3. Make database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

> Use your preferred credentials or:
>
> - username: `admin`
> - password: `admin`
> - email: `admin@admin.com`

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser and go to:

```
http://127.0.0.1:8000/
```

7. Log in using your superuser credentials.

---

## Author

- [@Theuri Joseph](https://github.com/codetheuri)

---



---

[Back to top ⬆️](#django-point-of-sale-pos-for-agrovet-)

