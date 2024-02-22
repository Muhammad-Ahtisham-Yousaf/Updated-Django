from django.db import models

# Create your models here.
class CustomUser (models.Model):
    first_name = models.CharField(max_length=55, null = True )
    username = models.CharField(max_length=55,null =True)
    email = models.EmailField( null =True )
    password1 = models.CharField(max_length=10, null =True)
    password2 = models.CharField(max_length=10, null =True)
    gender = models.CharField(max_length=55,null =True)
    # cv = models.FileField(null =True)
    current_location = models.CharField(max_length =66,null =True)
    contact_no = models.CharField(max_length=30,null =True)
    specialization = models.CharField(max_length =200,null =True)

    def __str__(self):
         return f' {self.id} -  {self.first_name} - {self.username} - {self.email}  - {self.password1} - {self.password2} - {self.gender} - {self.current_location} - {self.contact_no}-{self.specialization}' 

# class Myuser (models.Model):
#     full_name = models.CharField(max_length=150)
    
#     email = models.EmailField(max_length=150)

#     contact_no = models.CharField(max_length=150)
   
#     def __str__(self):
#         return f'User :{self.username}'
#         # return f' {self.id} -  {self.f_name} - {self.l_name} - {self.email} - {self.contact_no}' 