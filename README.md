"""# Password Generator (updated)

This is a simple Django project that generates secure random passwords using Python's `secrets` module.

Environment and running locally
1. Create and activate a virtual environment (the project assumes a standard venv; adjust if you use another tool):
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r mysite/requirements.txt
   ```

3. Set required environment variables:
   - DJANGO_SECRET_KEY (required in production)
   - DJANGO_DEBUG (optional; "1" or "true" to enable debug mode)
   - DJANGO_ALLOWED_HOSTS (optional; comma-separated hosts when DEBUG is False)

   Example (development):
   ```
   export DJANGO_DEBUG=1
   export DJANGO_SECRET_KEY='dev-secret-key-for-local-testing'
   ```

4. Run the development server:
   ```
   cd mysite
   python manage.py migrate
   python manage.py runserver
   ```

Notes
- The application now uses cryptographically secure randomness for password generation.
- Inputs are validated and bounded to reasonable sizes.
- Do not commit real secrets to the repository. Rotate any secret that may have been exposed.
"""