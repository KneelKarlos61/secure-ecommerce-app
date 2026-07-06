# Secure E-Commerce Web Application

## Project Overview

This project is a simple secure e-commerce web application built with Python Flask. The application allows users to register, log in, view products, and access pages based on their role. The main purpose of this project is to demonstrate basic web application security concepts learned in class, including authentication, password hashing, HTTPS, SQL injection prevention, XSS prevention, and role-based access control.

This project was developed as a college cybersecurity project and is intended for local testing and demonstration purposes.

## Features

* User registration and login
* Password hashing instead of plaintext password storage
* Session-based authentication
* Protected routes using a `login_required` decorator
* Role-based access control
* SQLite database storage
* Parameterized SQL queries to help prevent SQL injection
* Jinja template escaping to help prevent XSS attacks
* Local HTTPS support using a certificate and key
* Basic product display pages

## Technologies Used

* Python
* Flask
* SQLite
* Werkzeug security library
* HTML / CSS
* Jinja templates
* Git and GitHub
* OpenSSL for local HTTPS certificates

## Repository Structure
## Repository Structure

- ecommApp.py - Main Flask application file. Contains routes, authentication, HTTPS startup, and RBAC checks.
- init_db.py - Creates and initializes the SQLite database tables.
- requirements.txt - Lists the Python packages needed to run the project.
- templates/ - HTML templates used by Flask.
  - home.html - Homepage.
  - products.html - Product listing page.
  - register.html - User registration page.
  - login.html - User login page.
  - checkout.html - Protected checkout page.
  - search.html - XSS testing page.
- static/ - CSS and other static files.
  - style.css - Basic styling for the web pages.
- certs/ - Local HTTPS certificate files.
  - ca.crt - Local certificate authority certificate.
  - server.crt - Server certificate used by Flask.
  - server.ext - Certificate extension file with Subject Alternative Name settings.
- database/ - Local SQLite database folder.
  - ecommerce.db - Local development database file. This file is ignored by Git.


## How to Reproduce the Environment

### 1. Clone the Repository

### 2. Create a Virtual Environment

On Windows:
python -m venv venv
venv\Scripts\activate


On Mac/Linux:
python3 -m venv venv
source venv/bin/activate


### 3. Install Dependencies


pip install -r requirements.txt


## Database Initialization

SQLite

### 1. Create the Database Folder and Run it


mkdir database

THen,

python init_db.py



## Running the Application

### HTTP Version

To run the Flask application normally:


python ecommApp.py


Then open the browser and go to:


http://127.0.0.1:5000


## Security Testing Summary

### Password Hashing

Passwords are hashed before being stored in the database preventing plaintext passwords from being exposed if the database is viewed.

### SQL Injection Protection

SQL queries use parameterized statements like in the SQL labs this semster.

### XSS Protection

User input displayed on pages is handled through Jinja templates, which escape output by default.

### HTTPS

The project supports HTTPS using local certificate files. This protects data in transit during testing.

### Protected Routes and RBAC

Some pages require the user to be logged in. This is handled with a `login_required` decorator. 


Certain pages are restricted based on the user’s role, such as admin only or merchant only pages. The default is "Buyer" (customer) 


## How to Stop the Application

To stop the Flask server, press:


CTRL + C


in the terminal where the server is running. If you modify the ecomApp.py file then this will need to not be running and then saved, run again.

## Author

Neil Carlos

## Project Status

Completed for class project demonstration.
