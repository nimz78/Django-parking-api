# Parking Management App

A parking management REST api implemented in Django.

## Setup

First clone the repository:
    
    $ git clone https://github.com/nimz78/Django-parking-api.git
    $ cd Parking-api


Second create virtualenv inside the project directory:

    $ python3 -m venv .venv


Third activate the virtualenv:

    $ source .venv/bin/activate

Install packages from requirements.txt file:

    $ pip install -r requirements.txt

Making migrations:

    $ python manage.py makemigrations

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

## Usage

http://127.0.0.1:8000/parkings

http://127.0.0.1:8000/spaces