# Django CRM Project

This is a Django-based Customer Relationship Management (CRM) project that allows you to manage customers, products, orders, and tags. It provides a web-based interface for performing various CRM-related tasks.

## Features

- **Customer Management**: Create, update, and delete customer profiles. Includes fields for name, phone number, email, and profile picture.

- **Product Management**: Manage product information, including name, price, category, description, and associated tags.

- **Order Management**: Create and track orders with customer details, product selection, order status, and optional notes.

- **Tagging**: Categorize products using tags for better organization and searchability.

## Technology Stack

- **Django**: A high-level Python web framework used for building the backend of the application.

- **Database**: The project uses a PostgreSQL database to store customer, product, and order information.

- **User Authentication**: Django's built-in authentication system with the User model for user registration and login.

- **Static and Media Files**: The project handles static files (CSS, JavaScript) and media files (user-uploaded images) using AWS S3 for storage.

```
crm1
├─ manage.py
├─ crm1
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __pycache__
│  ├─ urls.py
│  ├─ __pycache__
│  ├─ templates
│  │  └─ accounts
│  │     ├─ dashboard.html
│  │     ├─ products.html
│  │     ├─ customer.html
│  │     ├─ main.html
│  │     ├─ navbar.html
│  │     ├─ status.html
│  │     ├─ order_form.html
│  │     ├─ delete.html
│  │     ├─ login.html
│  │     ├─ register.html
│  │     ├─ user.html
│  │     ├─ account_settings.html
│  │     ├─ password_reset.html
│  │     ├─ password_reset_sent.html
│  │     ├─ password_reset_done.html
│  │     └─ password_reset_form.html
│  ├─ static
│  ├─ queries.py
│  ├─ forms.py
│  ├─ filters.py
│  ├─ decorators.py
│  └─ signals.py
├─ requirements.txt
├─ static
│  ├─ css
│  │  └─ main.css
│  └─ images
│     ├─ default_profile.jpg
│     └─ logo.png
├─ runtime.txt
└─ Procfile
```