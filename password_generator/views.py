"""from django.shortcuts import render
from django.views.decorators.http import require_POST
import secrets
import random
import string

def index(request):
    # Render the index template which contains the form.
    return render(request, 'password_generator/index.html')

@require_POST
def password(request):
    """
    Generate a secure password based on user-selected options.

    - Accepts POST parameters:
      - length: integer (default 12), bounded between 4 and 128
      - uppercase: checkbox (present when checked)
      - numbers: checkbox (present when checked)
      - special: checkbox (present when checked)
    - Uses secrets.choice for secure random selection and SystemRandom.shuffle for secure shuffle.
    - Guarantees that when a category is selected, at least one character from that category appears in the password.
    """
    # Get and validate length
    length_raw = request.POST.get('length', '12')
    try:
        length = int(length_raw)
    except (TypeError, ValueError):
        return render(request, 'password_generator/index.html', {
            'error': 'Length must be an integer between 4 and 128.',
        })

    # Enforce sensible bounds
    if length < 4 or length > 128:
        return render(request, 'password_generator/index.html', {
            'error': 'Length must be between 4 and 128 characters.',
        })

    # Build character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if request.POST.get('uppercase') else ''
    digits = string.digits if request.POST.get('numbers') else ''
    special = '!@#$%^&*()' if request.POST.get('special') else ''

    all_chars = ''.join(filter(None, [lower, upper, digits, special]))
    if not all_chars:
        # If no options selected (shouldn't happen since lowercase is always available),
        # fall back to lowercase
        all_chars = lower

    # Ensure at least one character from each selected category
    password_chars = []
    if upper:
        password_chars.append(secrets.choice(upper))
    if digits:
        password_chars.append(secrets.choice(digits))
    if special:
        password_chars.append(secrets.choice(special))

    # Fill remaining characters using secure choice
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Securely shuffle using SystemRandom
    random.SystemRandom().shuffle(password_chars)
    thepassword = ''.join(password_chars)

    return render(request, 'password_generator/password.html', {'password': thepassword})
"""