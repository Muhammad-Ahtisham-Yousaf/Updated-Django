from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('candidate_registration/',views.candidate_registration, name='candidate_registration'), 
    path('employer_registration/',views.employer_registration, name='employer_registration'),
    path('employer_login/',views.employer_login, name='employer_login'),
    path('candidate_login/',views.candidate_login, name='candidate_login'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('job_posting/',views.job_posting, name='job_posting'),
    path('privacy_and_policy/',views.privacy_and_policy, name='privacy_and_policy'),
    path('dashboard/',views.dashboard, name='dashboard'),
   
     path('edit_user/<int:id>',views.edit_user, name='edit_user'),
    path('delete_user/<int:id>',views.delete_user, name='delete_user'),
    #  path('update_user/',views.update_user, name='update_user'),
     
    #  path ('edit_custom_user/<int:id>',views.edit_custom_user, name= 'edit_custom_user')
    # path('custom_candidate_registration/',views.custom_candidate_registration, name='custom_candidate_registration'), 
    # path('custom_candidate_login/',views.custom_candidate_login, name='custom_candidate_login'), 
    path('candidates/',views.candidates, name='candidates'), 
    path('profile/',views.profile, name='prof'), 

    
    path('edit_custom_user/',views.edit_custom_user, name='edit_custom_user'), 
    # path('dashboard2/',views.dashboard2, name='dashboard2'),


]
