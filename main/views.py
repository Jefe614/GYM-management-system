from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Image, Service, ServiceDetails, Trainer
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, UserSettingsForm, TrainerForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def pricing(request):
    return render(request, 'pricing.html')

def contacts(request):
    return render(request, 'contacts.html')

@login_required
def user_account(request):
    # Add logic to retrieve user information if needed
    user = request.user
    return render(request, 'user_account.html', {'user': user})


def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    form = ProfileEditForm(instance=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful edit

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'settings.html', {'form': form, 'success_message': 'Settings updated successfully'})
    else:
        form = UserSettingsForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})    

def custom_logout(request):
    logout(request)
    return redirect('home')     

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

def is_admin(user):
    return user.is_authenticated and user.is_staff  
@user_passes_test(is_admin)
def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form, 'action': 'Create'})


def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, 'trainer_detail.html', {'trainer': trainer})


# views.py
def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin)
def trainer_update(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', pk=pk)  # Redirect to trainer detail page
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_update.html', {'form': form, 'trainer': trainer})

def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin)
def trainer_delete(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainer_list')  # Redirect to trainer list page
    return render(request, 'trainer_delete.html', {'trainer': trainer})

def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin)
def trainer_update(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', pk=pk)  # Redirect to trainer detail page
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_update.html', {'form': form, 'trainer': trainer})


#login registration views
# 

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page or another desired page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to the home page or another desired page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})    

#pricing section
def basic_plan_page(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login to access this feature.')
        return redirect('login') 
    else:
        messages.success(request, 'You have successfully subscribed to the Basic Plan!')
        return redirect(reverse('basic_plan'))

def basic_plan(request):
    return render(request, 'basic_plan.html')        
       

def get_started_pro(request):
    
    return redirect('pro_plan_page') 

def get_started_premium(request):
   
    return redirect('premium_plan_page')  


#contact page submit button

def contact_form_submission(request):
    if request.method == 'POST':
        # Process the form data here (e.g., save to database, send email)
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email notification
        subject = 'New Contact Form Submission'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        recipient_list = ['jeffkimani32@gmail.com']  
        send_mail(subject, body, 'sender@example.com', recipient_list)

        return HttpResponse('Form submitted successfully!')
    else:
        # If the request method is not POST, return an error response
        return HttpResponse('Method not allowed', status=405)    