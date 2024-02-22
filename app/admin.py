from django.contrib import admin
from .models import  CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','username','password1','password2','gender','current_location','specialization', 'contact_no')

#  Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
# # admin.site.register(Myuser,MyAdmin)
