# Django Tweet App

A simple microblogging web application built with Django where users can register, log in, create, edit, and delete tweets—with optional image uploads. It showcases core Django features including user authentication, file uploads, and custom views.

## Features

- User registration and login/logout
- Post tweets with text (and images!)
- Edit or delete your own tweets
- Image handling using Django's `ImageField`
- Responsive UI with Bootstrap 5
- Auth-protected routes and form validation

## Tech Stack

- Python 3.13+
- Django 5.2.3
- SQLite (default, but easily swappable)
- HTML, CSS (Bootstrap 5)
- Jinja2 templating engine

## Getting Started

### Clone the repo

```bash
git clone https://github.com/yourusername/django-tweet-app.git
cd django-tweet-app
Set up a virtual environment
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Create a superuser (admin)
python manage.py createsuperuser
Start the development server
python manage.py runserver
Open your browser and visit:
http://127.0.0.1:8000/

Usage
Register or log in using the /register/ or /accounts/login/ route

Navigate to /create to post a new tweet

View, edit, or delete tweets on the homepage

Media & Static Files
Ensure your settings include:
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
And in urls.py:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Directory Structure
main/
├── tweet/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── main/
│   ├── settings.py
│   ├── urls.py
├── media/
├── static/
├── templates/
└── manage.py

License
This project is open-source and available under the MIT License.
