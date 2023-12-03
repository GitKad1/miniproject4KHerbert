# miniproject4KH


## Description
This project is built with Django to allow for customers to order pizza and view previous orders. The superuser can see the orders through the admin section of the site.

## Installation
To install dependencies:

pip install -r requirements.txt


To initialize the database:

python manage.py makemigrations 
This creates the schema that sets up the database.

python manage.py migrate
This applies the migrations.

python manage.py createsuperuser
This creates the administrator profile for the admin side of the website.
