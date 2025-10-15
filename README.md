# Password Generator

This is a simple Django project that generates a random password based on user-selected criteria.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Evans2028/Password-Generator.git
    cd Password-Generator
    ```

2.  **Activate the virtual environment:**

    This project is configured to work with a Nix-based environment. To activate the virtual environment, run:

    ```bash
    source .venv/bin/activate
    ```

3.  **Create a `.env` file:**

    Create a `.env` file in the `mysite` directory and add your Django `SECRET_KEY` to it:

    ```
    DJANGO_SECRET_KEY='your-secret-key'
    ```

    You can generate a new secret key using an online generator or by running the following in a Python shell:

    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```

4.  **Install the dependencies:**

    ```bash
    pip install -r mysite/requirements.txt
    ```

## Running the application

1.  **Run the development server:**

    ```bash
    ./devserver.sh
    ```

2.  **Access the application:**

    Open your web browser and go to the URL provided by the development server.
