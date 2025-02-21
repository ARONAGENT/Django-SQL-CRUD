# Django SQL-CRUD Project

This Django project demonstrates SQL CRUD (Create, Read, Update, Delete) operations using a cloud database hosted on [Aiven.io](https://aiven.io/).

## Project Overview
This project is designed to manage a database of films. It allows users to add, view, search, update, and delete films through a web interface.

### Technologies Used
- **Django** - Web framework for Python
- **Aiven.io** - Cloud database provider
- **MySQL** - Relational database
- **HTML, CSS , JavaScript(AJAX),Bootstraps** - Frontend design

---
## Django Project Setup
Follow these steps to set up the Django project on your machine:

### 1. Install Virtual Environment
```sh
pip install virtualenv  # Install virtualenv (one-time installation)
```

### 2. Create and Activate a Virtual Environment
```sh
mkdir django-webapps  # Create main directory
cd django-webapps
virtualenv rohan  # Create virtual environment
cd rohan
cd Scripts
activate  # Start virtual environment
```

### 3. Install Django
```sh
pip install django
```

### 4. Create a Django Project
```sh
django-admin startproject filmsWeb
cd filmsWeb
```

### 5. Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to check if the default Django homepage appears.

### 6. Create Required Directories
```sh
mkdir templates
mkdir static
```

### 7. Configure `settings.py`
Edit `settings.py` to include the following changes:

#### Modify TEMPLATES Section:
```python
'DIRS': [BASE_DIR, "templates"],
```

#### Add Static Files Configuration:
```python
STATICFILES_DIRS = [BASE_DIR, "static"]
```

### 8. Open the Project in VS Code
```sh
code .  # Opens VS Code with the project directory
```

---
## Database Schema (Films Table)
This project uses a `films` table for CRUD operations. Below is the schema:

```sql
CREATE TABLE films (
    filmid INT PRIMARY KEY AUTO_INCREMENT,
    filmnm VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    language VARCHAR(50),
    rating FLOAT,
    relyr INT,
    description VARCHAR(200)
);
```

---
## CRUD Operations Performed
This project supports the following operations on the `films` table:

1. **Add Film (INSERT)** - Users can add new films to the database.
2. **View All Films (SELECT)** - Displays a list of all films.
3. **Search by Genre (SEARCH)** - Filters films based on genre.
4. **Search by Language (SEARCH)** - Filters films based on language.
5. **Update Film Rating (UPDATE)** - Allows users to update a film's rating.
6. **Delete Film by ID (DELETE)** - Removes a film record from the database.

---
## Execution Video
For a step-by-step walkthrough, watch the [execution video](#)


---
## How to Run the Project
1. Clone this repository:
```sh
git clone https://github.com/ARONAGENT/Django-SQL-CRUD.git
cd Django-SQL-CRUD
```
2. Activate the virtual environment:
```sh
cd rohan
cd Scripts
activate
```
3. Run the Django server:
```sh
python manage.py runserver
```
4. Open `http://127.0.0.1:8000/` in your browser to use the application.

---
## Done!
This completes the setup and execution of the Django SQL-CRUD project. 🎉

Feel free to contribute, suggest improvements, or report issues!

