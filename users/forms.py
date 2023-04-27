from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """
    This class is used to configure the registration form by adding the email field to the pre-configured registration form of django.
    """
    email = forms.EmailField()

    class Meta:
        """
        This class is used to configure the model and fields of the registration form.
        To represent what fields are shown in the registration form.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']