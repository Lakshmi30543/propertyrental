from django import forms
from django.contrib.auth.models import User

from PS6v3.psrm.adminapp.models import UserProfile


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=UserProfile.ROLES)  # Add role field

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'role']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Set the password properly
        user.role = self.cleaned_data['role']  # Save the selected role
        if commit:
            user.save()
        return user
