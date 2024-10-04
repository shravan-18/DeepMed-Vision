from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse, HttpResponseNotFound
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .static.scripts import functions
from .forms import *
from .models import *

import os
import json
import base64


'''Function to fully delete all session variables from latest session'''
def clear_session_variables(request):
    # List of session keys you want to clear
    session_keys = [
        'patient_name',
        'patient_UHID_No',
        'created',
    ]
    
    for key in session_keys:
        try:
            if key in request.session:
                del request.session[key]
        except Exception as e:
            # Optionally log the exception if needed
            print(f"An error occurred while deleting session key '{key}': {e}")


'''View to render landing page'''
def home(request):
    return render(request, "DeepMedApp/index.html")


'''View to signup user'''
def signupuser(request):
    if request.method == 'GET':
        return render(request, "DeepMedApp/signupuser.html")
    
    else:   
        print(request.POST)
        # Validate Email...
        if functions.check_email(request.POST.get("Email Field")) == False:
            return render(request, "DeepMedApp/signupuser.html", {"error": "Invalid Email Address!"})

        # Create a new user...
        if request.POST.get("Password Field") == request.POST.get("Password Confirmation Field"):
            try:
                user = User.objects.create_user(request.POST['Email Field'], password=request.POST['Password Field'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, "DeepMedApp/signupuser.html", {"error": "Email already exists! Please Log in."})

        else:
            return render(request, "DeepMedApp/signupuser.html", {"error": "Passwords did not match!"})
        

'''View to login user'''
def loginuser(request):
    if request.method == 'GET':
        return render(request, "DeepMedApp/loginuser.html")
    
    else:
        # Validate Email...
        email = request.POST.get("Email")
        if not functions.check_email(email):
            return render(request, "DeepMedApp/loginuser.html", {"error": "Invalid Email Address!"})
        
        # Check if the user exists
        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            return render(request, "DeepMedApp/loginuser.html", {"error": "No user exists with this email address!"})
        
        # Authenticate the user
        user = authenticate(request, username=email, password=request.POST.get("Password"))
        if user is None:
            return render(request, "DeepMedApp/loginuser.html", {"error": "Email and Password did not match!"})
        else:
            login(request, user)
            return redirect('dashboard')


'''View to logout user'''
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


'''View to render dashboard'''
@login_required
def dashboard(request):
    return render(request, 'DeepMedApp/dashboard.html')


'''View to render navbar'''
def navbar(request):
    return render(request, 'DeepMedApp/partials/navbar.html')


'''View to render footer'''
@login_required
def footer(request):
    return render(request, 'DeepMedApp/partials/footer.html')


'''View to render about page'''
@login_required
def about(request):
    return render(request, 'DeepMedApp/about.html')

'''View to render contact page'''
@login_required
def contact(request):
    return render(request, 'DeepMedApp/contact.html')

'''View to render existing records page'''
@login_required
def existing_records(request):
    return render(request, 'DeepMedApp/existing_records.html')

'''View to render create records page'''
@login_required
def create_record(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page after saving
    else:
        form = PatientForm()
    return render(request, 'DeepMedApp/create_record.html')
