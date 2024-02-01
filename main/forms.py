# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        # Add additional customization if needed

    # You can add additional fields or customize the existing ones as needed

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed
        self.fields['email'].widget.attrs['readonly'] = True  # Example: Make email field read-only

    # You can add validation or additional customization here if needed