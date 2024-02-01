from django.shortcuts import render, redirect
from .models import Image, Service, ServiceDetails
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, UserSettingsForm
from django.contrib.auth import logout
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