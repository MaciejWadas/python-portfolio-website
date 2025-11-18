# Portfolio Website

This is a personal portfolio website built with Flask, showcasing various projects with detailed descriptions, images, and GitHub links.

## Features

- Home page with a welcome landing section.
- Portfolio page displaying a list of projects fetched from a database.
- Each project includes a title, short description, detailed description with rich text support, image, and GitHub repository link.
- About Me page with personal and professional information.
- Add New Project form to submit new projects into the portfolio, with input validation including URL checks for images and GitHub links.
- Individual project detail pages accessible by clicking on projects in the portfolio.
- Database integration using SQLAlchemy to store project data.
- Flask-WTF form handling for secure and user-friendly input.
- CKEditor integration for rich text descriptions in projects.
- Bootstrap 5 for responsive and modern UI styling.

## Usage

- Run the app with Flask to start a local server.
- Navigate through the home, portfolio, about, and project submission pages.
- Add projects dynamically through the form by going to the "/add-project" route.
- View detailed information about each project.

## Technologies

- Python 3
- Flask web framework
- Flask-Bootstrap 5
- Flask-WTF for forms
- Flask-CKEditor for rich text editing
- SQLAlchemy ORM
- SQLite or other database configured via environment variables

## Setup

1. Set environment variables for `SECRETKEY` and `DBPATH`.
2. Install requirements (`Flask`, `Flask-Bootstrap`, `Flask-WTF`, `Flask-CKEditor`, `Flask-SQLAlchemy`).
3. Run the application:
