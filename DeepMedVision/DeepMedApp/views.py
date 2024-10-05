from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage

from .static.scripts import functions, LLM
from .forms import *
from .models import *

import torch
from PIL import Image

import intel_extension_for_pytorch as ipex


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
            patient = form.save()
            request.session['patient_id'] = patient.id
            return redirect('scanner_view', patient.id)  # Redirect to a success page after saving
    else:
        form = PatientForm()
    return render(request, 'DeepMedApp/create_record.html')


'''View to render scanner page'''
@login_required
def scanner_view(request, id):
    if request.method == 'POST':
        # Handle any POST data or processing specific to this view
        # For example, you can process form data sent via POST here
        return JsonResponse({'message': 'POST request handled!'}, status=200)
    return render(request, 'DeepMedApp/scanner.html')


def infer(request, image_path):
    # Load the appropriate model based on the modality and task from the session
    model = torch.load(f"{request.session['modality']}_{request.session['task']}.pth")
    model = ipex.optimize(model)  # Optimize the model using Intel IPEX

    # Perform inference with the model
    input_image = Image.open(image_path)
    output_tensor = model(input_image)

    # Create a brief inference result
    mini_inference = f"Mini inference based on {image_path}: {output_tensor}"

    # Generate a detailed inference explanation using the LLM
    detailed_inference = f"Detailed inference based on {image_path}: {LLM(output_tensor, image_path)}"

    return mini_inference, detailed_inference



'''View to accept incoming image uploads in the scanner page'''
def upload_image(request):
    if request.method == 'POST':
        # Check if the image is in the POST request
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image file in request'}, status=400)
        
        image_file = request.FILES['image']
        
        # Debugging: log the received file
        print(f"Received image: {image_file.name}")

        # Get the patient id from session
        patient_id = request.session.get('id')
        if not patient_id:
            return JsonResponse({'error': 'No patient ID found in session'}, status=400)
        
        try:
            # Fetch the patient instance
            modality = request.POST['modality']
            task = request.POST['task']

            request.session['modality'] = modality
            request.session['task'] = task

            patient = Patient.objects.get(id=patient_id)
            patient.image = image_file  # Save image to the Patient model
            patient.save()

            # Run inference on saved image
            mini_inference, detailed_inference = infer(request, patient.image.path)
            
            return JsonResponse({
                'message': 'Image processed successfully!',
                'mini_inference': mini_inference,
                'detailed_inference': detailed_inference
            }, status=200)
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)
        except Exception as e:
            # Log any unexpected errors for debugging
            print(f"Unexpected error: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
