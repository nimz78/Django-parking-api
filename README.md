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

You can post Name, Address, Capacity of the parking with this Endpoint below:

    http://127.0.0.1:8000/parkings


You can Post code(Exact location of parking), Parking (Parking name), Status(status of the parking space which is one of Empty, Full, Booked statuses) with this Endpoint below:

    http://127.0.0.1:8000/spaces

You can access to put, patch and delete with add the id number end of the URL path like the example below:

    http://127.0.0.1:8000/parkings/1
    http://127.0.0.1:8000/spaces/1