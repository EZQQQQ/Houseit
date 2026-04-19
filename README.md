# Houseit

Houseit is a Django-based property listing web application built around different user roles in the housing journey. The project supports account registration and login, owner-managed listings, buyer and tenant browsing flows, bookmarking, and an admin-facing master data refresh workflow backed by SQLite.

## What This Project Shows

- full-stack web development with Django
- role-based application flows for admin, owner, buyer, and tenant users
- form handling, authentication, templating, and media uploads
- structured property search and listing management on top of a relational data model

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML templates
- CSS and static assets

## Application Structure

The main application lives inside `Houseit-App (2)/`.

- `houseitapp/`: Django project configuration, settings, and URL entrypoints
- `houseit/`: core application models, views, forms, feature modules, and templates
- `houseit/templates/`: templates grouped by user flow such as shared views, owner views, admin views, and research pages
- `static/`: CSS, JavaScript, and shared static media
- `media/`: uploaded property and profile images
- `houseit.db`: bundled SQLite database used by the application

## Main User Flows

- guest users can register, log in, and recover passwords
- owners can create rental and resale listings, then manage their own properties
- buyers and tenants can search listings, view property details, and bookmark properties
- admins can access an internal dashboard and trigger master data refresh actions

## Running Locally

From the repository root:

```bash
cd "Houseit-App (2)"
python -m pip install django djangorestframework pillow
python manage.py runserver
```

Then open the local URL shown by Django, usually `http://127.0.0.1:8000/`.

## Notes

- the repository already includes a SQLite database file for local use
- static assets, templates, and sample media are committed in the repository
- this project appears to have been developed as a course team project, so some supporting presentation and report materials are included as well
