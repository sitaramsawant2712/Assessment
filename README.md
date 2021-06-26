## Create Virtualenv 
virtualenv env --python=/usr/local/bin/python3.7
## Activate Virtual env
source env/bin/activate

## install requirement.txt
pip install -r requirement.txt

## Command to create django project
django-admin startproject company
cd company/

## Command to create app
python manage.py startapp staff

## Command to migrate table in database
python manage.py migrate
python manage.py createsuperuser

## Command to run the project
python manage.py runserver
