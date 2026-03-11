""" Create Django project. """

import django

# Ensure Django is installed
try:
    django.setup()
except Exception as e:
    print(f"Error: {e}")
    exit()

# Create a new Django project
project_name = 'myproject'
django-admin startproject myproject

# Navigate into the project directory
import os
os.chdir(project_name)

# Create a new Django app
app_name = 'myapp'
python manage.py startapp myapp

# Update settings.py to include the new app
with open('myproject/settings.py', 'r') as file:
    settings = file.read()

settings = settings.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    '" + app_name + "',\n")

with open('myproject/settings.py', 'w') as file:
    file.write(settings)

# Create a model in the new app
with open('myapp/models.py', 'w') as file:
    file.write("""
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
""")

# Migrate the database
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver