from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()


class UserCreationForms(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
