# Django SQL-CRUD Project

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-orange.svg)](https://www.mysql.com/)
[![Aiven](https://img.shields.io/badge/Aiven-Cloud%20Database-purple.svg)](https://aiven.io/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-blueviolet.svg)](https://getbootstrap.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![AJAX](https://img.shields.io/badge/AJAX-Async-red.svg)](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)

## 📋 Project Overview

This Django web application demonstrates comprehensive SQL CRUD (Create, Read, Update, Delete) operations for a film database management system. The project utilizes a cloud-hosted MySQL database on **Aiven.io** and provides an intuitive web interface for managing film records with advanced search and filtering capabilities.

## 🎬 Demo Video

https://github.com/user-attachments/assets/e5fc973e-3a15-4545-8dd7-073fa6147428

*Watch the complete demonstration of all CRUD operations in action!*

## ✨ Features

### Core Functionality
- 🎬 **Add New Films** - Insert film records with complete details
- 📖 **View All Films** - Display comprehensive film catalog
- 🔍 **Advanced Search** - Filter by genre and language
- ✏️ **Update Records** - Modify film ratings and details
- 🗑️ **Delete Records** - Remove films by ID
- 📱 **Responsive Design** - Mobile-friendly interface

### Technical Features
- **AJAX Integration** - Seamless user experience without page reloads
- **Cloud Database** - Reliable Aiven.io MySQL hosting
- **Bootstrap UI** - Modern and responsive design
- **Error Handling** - Robust validation and error management
- **SQL Optimization** - Efficient database queries

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.x | Web Framework |
| **Python** | 3.x | Backend Language |
| **MySQL** | 8.x | Database |
| **Aiven.io** | Cloud | Database Hosting |
| **HTML5** | Latest | Markup |
| **CSS3** | Latest | Styling |
| **JavaScript** | ES6+ | Frontend Logic |
| **AJAX** | - | Asynchronous Operations |
| **Bootstrap** | 5.x | UI Framework |

## 🗄️ Database Schema

### Films Table Structure
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

### Field Descriptions
| Field | Type | Description |
|-------|------|-------------|
| `filmid` | INT (PK) | Auto-incrementing primary key |
| `filmnm` | VARCHAR(100) | Film name (required) |
| `genre` | VARCHAR(50) | Film genre category |
| `language` | VARCHAR(50) | Film language |
| `rating` | FLOAT | Film rating (0.0-10.0) |
| `relyr` | INT | Release year |
| `description` | VARCHAR(200) | Film description |

## 🔧 CRUD Operations

### 1. **CREATE** - Add New Film
- Form-based film entry
- Input validation
- Auto-generated film ID

### 2. **READ** - View & Search Films
- **View All Films** - Complete catalog display
- **Search by Genre** - Filter films by genre
- **Search by Language** - Filter films by language
- **Advanced Filtering** - Multiple search criteria

### 3. **UPDATE** - Modify Film Records  
- **Update Rating** - Modify film ratings
- **Edit Details** - Update film information
- **Bulk Updates** - Multiple record modifications

### 4. **DELETE** - Remove Film Records
- **Delete by ID** - Remove specific films
- **Confirmation Dialogs** - Prevent accidental deletions
- **Soft Delete Options** - Recoverable deletions

## 🚀 Installation & Setup

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **Code Editor** (VS Code recommended)

### Step-by-Step Installation

#### 1. **Setup Virtual Environment**
```bash
# Install virtualenv (one-time setup)
pip install virtualenv

# Create project directory
mkdir django-webapps
cd django-webapps

# Create virtual environment
virtualenv rohan
cd rohan

# Activate virtual environment
# On Windows:
cd Scripts
activate

# On macOS/Linux:
source bin/activate
```

#### 2. **Install Django**
```bash
pip install django
pip install mysqlclient  # For MySQL connectivity
```

#### 3. **Clone & Setup Project**
```bash
# Clone the repository
git clone https://github.com/ARONAGENT/Django-SQL-CRUD.git
cd Django-SQL-CRUD

# Create Django project structure (if starting fresh)
django-admin startproject filmsWeb
cd filmsWeb

# Create required directories
mkdir templates
mkdir static
```

#### 4. **Configure Django Settings**

Edit `settings.py` to include:

```python
# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Updated path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static Files Configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Database Configuration (Aiven.io MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_aiven_host',
        'PORT': '25061',  # Default Aiven MySQL port
    }
}
```

#### 5. **Database Migration**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. **Run Development Server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📁 Project Structure

<img width="388" height="632" alt="image" src="https://github.com/user-attachments/assets/3a5742d4-bf5a-4cd5-a4c8-a36ed1fe782b" />


## 🔗 API Endpoints

This project supports the following operations on the films table:
1. Add Film (INSERT) - Users can add new films to the database.
2. View All Films (SELECT) - Displays a list of all films.
3. Search by Genre (SEARCH) - Filters films based on genre.
4. Search by Language (SEARCH) - Filters films based on language.
5. Update Film Rating (UPDATE) - Allows users to update a film's rating.
6. Delete Film by ID (DELETE) - Removes a film record from the database.

## 🎨 Frontend Features

### User Interface
- **Responsive Design** - Bootstrap-powered responsive layout
- **Interactive Forms** - Real-time validation and feedback
- **Search Filters** - Dynamic filtering without page reload
- **Modal Dialogs** - Confirmation prompts for critical actions
- **Loading States** - Visual feedback during operations

### JavaScript/AJAX Implementation
- **Asynchronous Operations** - Smooth user experience
- **Form Validation** - Client-side input validation
- **Dynamic Content** - Real-time updates without page refresh
- **Error Handling** - User-friendly error messages


## 👥 Authors & Contributors

- **[ARONAGENT](https://github.com/ARONAGENT)** - Project Creator & Maintainer

## 🙏 Acknowledgments

- **Django Community** - For the excellent web framework
- **Aiven.io** - For reliable cloud database hosting
- **Bootstrap Team** - For the responsive UI framework
- **MySQL** - For the robust database system
- **Open Source Community** - For continuous inspiration and support

## 📞 Support & Contact

### Getting Help
- 📖 **Documentation**: Check this README first
- 🐛 **Bug Reports**: [Create an Issue](https://github.com/ARONAGENT/Django-SQL-CRUD/issues)
- 💡 **Feature Requests**: [Suggest Features](https://github.com/ARONAGENT/Django-SQL-CRUD/issues)
- 💬 **Questions**: [Start a Discussion](https://github.com/ARONAGENT/Django-SQL-CRUD/discussions)

### Connect with the Developer
- **GitHub**: [@ARONAGENT](https://github.com/ARONAGENT)
- **LinkedIn**: [Connect for professional inquiries]
- **Email**: [Contact via GitHub]

---

⭐ **If you find this project helpful, please give it a star!** ⭐

*Built with ❤️ using Django and modern web technologies*
