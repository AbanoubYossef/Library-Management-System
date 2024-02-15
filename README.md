# Django Book Management System

This is a simple web application built with Django that allows users to manage books and categories.

## Features

- Add, edit, and delete books
- Add, edit, and delete categories
- Search for books by title
- View book details
- View all books or books by category
- Track book status (available, sold, rental)
- Upload book images

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-book-management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-book-management
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```


5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- Home page: View all books and categories. Add new books and categories.
- Books page: Search for books by title and view details. Add, edit, or delete books.
- Categories page: Add, edit, or delete categories.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
