from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'auth-input', 'placeholder': 'Логин'}),
        }

        labels = {
            'username': False,
        }
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'auth-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = False
        self.fields['password1'].help_text = None

        self.fields['password2'].widget.attrs['class'] = 'auth-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = False
        self.fields['password2'].help_text = None

        self.fields['username'].help_text = None
