from django import forms
from ..models import CustomUser
from django.contrib import messages

class CustomRegistrationForm2 (forms.ModelForm):
    first_name = forms.CharField(max_length=55)
    username = forms.CharField(max_length=55)
    email = forms.EmailField(required=False, initial='example@gmail.com')
    password1 = forms.CharField(max_length=200 ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', )
    gender = forms.CharField(max_length=55)
    # cv = forms.FileField()
    current_location = forms.CharField()
    contact_no = forms.CharField(max_length=30)
    specialization = forms.CharField(max_length=200)

    class Meta:
       model = CustomUser
       fields = ('__all__')

    # def clean_email(self):
    #     # Check if the email is already registered
    #     email = self.cleaned_data.get('email')
    #     if CustomUser.objects.filter(email=email).exists():
    #         messages.error(request="This email is already registered.")
    #     return email

    # def clean_username(self):
    #     # Check if the username is already taken
    #     username = self.cleaned_data.get('username')
    #     if CustomUser.objects.filter(username=username).exists():
    #         raise forms.ValidationError("This username is already taken.")
    #     return username

    # def clean_password2(self):
    #     # Check if the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password2

    # def save(self, commit=True):
    #      # Save the provided password in hashed format
    #      user = super().save(commit=False)
    #      user.email = self.cleaned_data["email"]
    #      if commit:
    #          user.save()
    #      return user

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if len(username) < 4:
    #         raise forms.ValidationError("Username must be at least 4 characters long.")
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # Add email validation logic here if needed
    #     return email

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     # Add password1 validation logic here if needed
    #     return password1

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError("Passwords do not match.")
    #     return password2

    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     # Add first name validation logic here if needed
    #     return first_name