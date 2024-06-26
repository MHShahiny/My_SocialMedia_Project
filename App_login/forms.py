from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_login.models import UserProfile



class CreateNewUser(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': "Email", 'autocomplete': 'off'})
    )
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': "Username", 'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': "Password", 'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': "Password confirmation", 'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)



class EditProfile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=UserProfile
        fields="__all__"


