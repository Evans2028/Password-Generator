from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def index(request):
    return render(request, 'password_generator/index.html')

def password(request):
    length = int(request.GET.get('length'))
    
    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)
        
    return render(request, 'password_generator/password.html', {'password':thepassword})
