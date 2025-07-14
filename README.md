## Django Point of Sale (POS) suited for Agrovet 💸

A Point of Sale web app for Agrovet built with Python and Django.


## Table of Contents:
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)
- [License](#license)



## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, to CSV, and to PDF buttons
- Categories and Products Management
- Clients Management
- Sales Management


## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap, SweetAlert, DataTables
- Backend: Django, Python, Ajax, SQLite 

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [pip package manager](https://pip.pypa.io/en/stable/installation/)

  
#### Browser Compatibility Notice: Firefox NOT Supported ‼
#### Please Use Chrome or Edge Browsers ‼
    
  1. Clone or download the repository:

  ` git clone https://github.com/betofleitass/django_point_of_sale`

  2. Go to the project directory

  ` cd django_point_of_sale`

  3. Create a virtual environment :

  PowerShell:
  ```
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```
  
  Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  4. Install dependencies:  
  ` pip install -r requirements.txt`
  
  5.  Update pip and setuptools  
  ` python -m pip install --upgrade pip setuptools`  
  
 
  
## Run it locally
After restarting your computer

1. Go to the project directory: `cd django_point_of_sale`

2. Activate the virtual enviroment

    
    Linux:
    ```
    source venv/bin/activate
    ```
3. Go to the django_pos folder: `cd django_pos`

4. Make database migrations:  
  `python manage.py makemigrations` and 
  `python manage.py migrate`

5. Create superuser `python manage.py createsuperuser` 
  
   with the following data, or with the data you prefer:
   `username: admin,
    password: admin,
    email: admin@admin`

7. Run the server: `python manage.py runserver`

8. Open a browser and go to: `http://127.0.0.1:8000/`

9. Log In with your superuser credentials.
    



## Authors

- [@Theuri Joseph](https://www.github.com/codetheuri)

##  License

This project is under [MIT License.](https://choosealicense.com/licenses/mit/)

[Back to top ⬆️](#django-point-of-sale-pos-)
