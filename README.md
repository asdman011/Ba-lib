# Baġlib

Baġlib is an interactive platform designed for book lovers to track, share, and immerse in a personalized reading experience. Whether you're organizing your digital bookshelf or maintaining your reading streaks, Baġlib has you covered.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Track your books and reading progress
- Organize books into folders
- Share public folders and profiles with the community
- Maintain personal and folder-specific reading streaks
- User authentication and profile management

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.2.16
- Virtualenv

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/Baglib.git
    cd Baglib
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Collect static files:**

    ```sh
    python manage.py collectstatic
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### User Authentication

- Sign up for a new account
- Log in to your account
- Manage your profile

### Book Management

- Add new books
- Track reading progress
- Organize books into folders

### Community Features

- Share public folders and profiles
- View other users' public profiles and folders

## Deployment

### Deploying on PythonAnywhere

1. **Create a virtual environment on PythonAnywhere:**

    ```sh
    mkvirtualenv myenv --python=python3.8
    pip install -r requirements.txt
    ```

2. **Upload your project files to PythonAnywhere.**

3. **Set up the web app:**

    - Go to the "Web" tab on PythonAnywhere.
    - Click "Add a new web app".
    - Choose "Manual configuration" and select the correct Python version.

4. **Configure the WSGI file:**

    Edit the WSGI configuration file to point to your Django project's `wsgi.py` file.

    ```python
    import os
    import sys

    project_home = '/home/yourusername/Baglib'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    os.environ['DJANGO_SETTINGS_MODULE'] = 'Baglib.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```

5. **Set up static files:**

    Configure the static files URL and directory in the "Static files" section of the Web tab.

    - URL: `/static/`
    - Directory: `/home/yourusername/Baglib/staticfiles`

6. **Run database migrations:**

    ```sh
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

8. **Test your deployment:**

    Visit your PythonAnywhere domain to ensure your application is running correctly.

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.