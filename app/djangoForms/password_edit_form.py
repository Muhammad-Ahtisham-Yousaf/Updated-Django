from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserChangeCustomForm(UserChangeForm):


    class Meta:
        model = User
        fields = ('first_name','username','email',)
        # fields = ('__all__')

from django import forms
from ..models import EditUser

class EditUserForm (forms.ModelForm):      
    location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={ 'placeholder': 'Dlocation', 'class': ''})  )
    mobile_no = forms.CharField(max_length=255,widget=forms.TextInput(attrs={ 'placeholder': 'Dmobile', 'class': ''}) )
    about_me = forms.CharField( widget=forms.Textarea(attrs={ 'placeholder': 'Dabout', 'class': ''}) )
    skills = forms.CharField(max_length=200, widget=forms.TextInput(attrs={ 'placeholder': 'Dskills', 'class': ''}) )
    joining_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'Djoining date', 'class': ''}) )
    education = forms.CharField(max_length=255, widget=forms.TextInput(attrs={ 'placeholder': 'Deducation', 'class': ''}) )
 #     company_logo = forms.ImageField,upload_to='app' ,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5RhqcwxGDJustOfPZ5ybmAWzysfuMvTAYoUyVx63gKBwNRIeMm9kDwlS5NEN6I6vrnac&usqp=CAU' )
    university = forms.CharField(max_length =66, widget=forms.TextInput(attrs={ 'placeholder': 'Duniverstiy', 'class': ''}) )
    priveus_job = forms.CharField(max_length=70, widget=forms.TextInput(attrs={ 'placeholder': 'Dprivious job', 'class': ''}) )
    projects = forms.CharField(max_length =200, widget=forms.Textarea(attrs={ 'placeholder': 'Dprojects', 'class': ''}) )
    project_desc = forms.CharField(max_length =200, widget=forms.Textarea(attrs={ 'placeholder': 'Dprojectd', 'class': ''}) )
    interests = forms.CharField(max_length =200, widget=forms.TextInput(attrs={ 'placeholder': 'Dinterests', 'class': ''}) )
    gender = forms.CharField(max_length =200, widget=forms.TextInput(attrs={ 'placeholder': 'Dgender', 'class': ''}) )
 
    class Meta:
        model = EditUser
        # fields = ('first_name','username','email',)
        fields = ('__all__')

    