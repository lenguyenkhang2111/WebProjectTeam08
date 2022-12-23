from django import forms
from django.contrib.auth.models import User
from account.models import Account
from django.contrib.auth.forms import UserCreationForm

# forms.py:


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    birth_date = forms.DateField()

    class Meta:
        model = Account
        fields = ['username', 'email', 'birth_date',
                  'first_name', 'last_name', 'phone', 'image']

    # forms.py:
