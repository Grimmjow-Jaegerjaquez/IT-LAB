"""
Definition of views.
"""

from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from app.models import RegisteredUser

def home(request):
	return render(request, 'app/register.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        RegisteredUser.objects.create(user_name=user_name, password=password, email=email, phone_number=phone_number)
        return redirect('welcome', user_name=user_name)


def welcome(request, user_name):
    user = RegisteredUser.objects.filter(user_name__exact=user_name).first()
    email = None
    phone_number = None
    if user:
        email = user.email
        phone_number = user.phone_number
    return render(request, 'welcome.html', locals())
