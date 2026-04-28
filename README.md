# Bookinfo

A simple Django project.

## Prerequisites

- Python 3.11+ (recommended)
- Windows PowerShell or Command Prompt

## Setup

1. Create and activate a virtual environment (example):

   ```bat
   python -m venv one-stop
   one-stop\Scripts\activate
   ```

2. Install dependencies:

   ```bat
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bat
   python manage.py migrate
   ```

4. Run the development server:

   ```bat
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ in your browser.

## Common tasks

- Create an admin user:

  ```bat
  python manage.py createsuperuser
  ```

- Run tests:

  ```bat
  python manage.py test
  ```

## Project structure

- `bookhub/` - Django project settings and configuration
- `main/` - Main application (views, urls, models)
- `manage.py` - Django management entry point
- `requirements.txt` - Python dependencies
