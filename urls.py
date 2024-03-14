from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('candidate_registration/',views.candidate_registration, name='candidate_registration'), 
    path('employer_registration/',views.employer_registration, name='employer_registration'),
    path('employer_login/',views.employer_login, name='employer_login'),
    path('candidate_login/',views.candidate_login, name='candidate_login'),
    path('about_us/',views.about_us, name='about_us'),
    path('terms_for_users/',views.terms_for_users, name='terms_for_users'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('job_posting/',views.job_posting, name='job_posting'),
    path('privacy_and_policy/',views.privacy_and_policy, name='privacy_and_policy'),
    path('things_you_should_know/',views.things_you_should_know, name='things_you_should_know'),
    path('writing_resume/',views.writing_resume, name='writing_resume'),
    path('most_asked/',views.most_asked, name='most_asked'),
    path('stay_confident/',views.stay_confident, name='stay_confident'),
    path('writing_email/',views.writing_email, name='writing_email'),

    path('user_dashboard/',views.user_dashboard, name='user_dashboard'),
   
    path('user_details_edit/<int:id>',views.user_details_edit, name='user_details_edit'),
    path('user_details_edit/<int:id>',views.user_details_edit, name='user_details_edit'),
    path('delete_user/<int:id>',views.delete_user, name='delete_user'),
    #  path('update_user/',views.update_user, name='update_user'),
     
    path ('Candidate_details/',views.Candidate_details, name= 'Candidate_details'),
    path ('Employer_details/',views.Employer_details, name= 'Employer_details'),
    path ('JobPosted/',views.JobPosted, name= 'JobPosted'),
    path ('AdminPanel/',views.AdminPanel, name= 'AdminPanel'),
    
    path ('user_edit/<int:id>',views.user_edit, name= 'user_edit'),
    # path ('employer_edit/<int:id>',views.employer_edit, name= 'employer_edit'),
    path ('employer_details_edit/<str:username>',views.employer_details_edit, name= 'employer_details_edit'),
    path ('user_details_edit/<str:username>',views.user_details_edit, name= 'user_details_edit'),
    path ('candidate_logout/',views.candidate_logout, name= 'candidate_logout'),
    # path('custom_candidate_registration/',views.custom_candidate_registration, name='custom_candidate_registration'), 
    # path('custom_candidate_login/',views.custom_candidate_login, name='custom_candidate_login'), 
    path('candidates/',views.candidates, name='candidates'), 
    path('Employers/',views.employers, name='Employers'), 
    path('myprofile/',views.myprofile, name='myprofile'), 
    path('profile_page/<str:username>',views.profile_page, name='profile_page'), 
    # path('profile_page/<str:username>',views.profile_page, name='profile_page'), 
    # path('employer_profile_page/<str:username>',views.employer_profile_page, name='employer_profile_page'), 

    path('full_job_profile/',views.full_job_profile, name='full_job_profile'), 

    
    # path('edit_custom_user/',views.edit_custom_user, name='edit_custom_user'), 
    # path('dashboard2/',views.dashboard2, name='dashboard2'),
]
