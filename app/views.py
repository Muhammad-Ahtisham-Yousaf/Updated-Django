from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# user authentication
from django.contrib.auth import authenticate, login, logout

# user auth forms
from django.contrib.auth.forms import UserCreationForm
from .djangoForms.registration import BuiltinUserCreationForm,BuiltinEmployerCreationForm

# for editing
from .djangoForms.password_edit_form import UserChangeCustomForm,FullUserDetailsForm,EmployerChangeCustomForm,FullEmployerDetailsForm
# user auth model
from django.contrib.auth.models import User

# flash messages
from django.contrib import messages

#  Custom forms
from .djangoForms.job_posting import JobPostingForm
from .djangoForms.password_edit_form import UserDetailsForm

# Custom Models
from .models import JobPosting , EmployerDetails ,UserDetails

# Create your views here.
def home (request):
    # return HttpResponse( 'working')
   job_posting=JobPosting.objects.all()
   if request.user.is_authenticated:
      return  render (request , 'main.html',{'jobs':job_posting})
   else:
     messages.warning(request,'kindley login first!.')
     return redirect ('candidate_login')
 





# def candidate_registration (request):
    # if request.method == 'GET':
    #  form = BuiltinUserCreationForm()
    # #  return HttpResponse (form)
    #  return render (request, 'Candidate/registration.html' ,{ 'form_data':form})
    # else:
    #     form = BuiltinUserCreationForm(request.POST,request.FILES)
    #     # return HttpResponse(form)

    #     first_name= request.POST['first_name']
    #     email= request.POST['email']
    #     username= request.POST['username']
    #     password1= request.POST['password1']
    #     password2= request.POST['password2']

    #     if not password1:
    #              messages.error(request, 'Password cannot be empty')
    #              return  HttpResponse (form.errors)
    #              return redirect('candidate_registration')     
    #     elif User.objects.filter(first_name=first_name).exists():
    #            messages.error(request,'Name already exist')
    #            return redirect('candidate_registration')
    #     elif User.objects.filter(username=username).exists():
    #           messages.error(request,'Username already exist')
    #           return redirect('candidate_registration')
    #     elif User.objects.filter(email=email).exists():
    #          messages.error(request,'email already exist')
    #          return redirect('candidate_registration')
    #     # elif User.objects.filter(password1=password2).exists():
    #     #       messages.error(request,'password is already taken')
    #     #       return redirect('candidate_registration')
    #     elif password1 != password2:
    #          messages.error(request, 'Passwords do not match')
  
    #          return redirect('candidate_registration')
    #     # return  HttpResponse (form.errors)
        
    #     if form.is_valid():
    #         # return HttpResponse ('suscuss')
    #         form.save()
    #         # return HttpResponse(form)
    #         messages.success(request,'User Registered succussfully')
    #         return redirect(candidate_login)
    #     else:
    #         messages.error(request,'Please try again')
    #         return  HttpResponse (form.errors)
def candidate_registration (request):
    if request.method == 'GET':
        form = BuiltinUserCreationForm()
        return render(request, 'Candidate/registration.html', {'form_data': form})
    else:
        form = BuiltinUserCreationForm(request.POST, request.FILES)
        specialization= request.POST['specialization']
        if form.is_valid() and specialization:
            user=form.save()
            edit_user= UserDetails (specialization=specialization,user=user,type=0)
            edit_user.save()
            messages.success(request, 'User registered successfully.')
            # return HttpResponse (edit_user)
            return redirect (candidate_login)
        else:
            messages.error(request, 'You does not follow the instructions.')
            return HttpResponse (form.errors)

# def custom_candidate_registration (request):
#     if request.method == 'GET':
#      form = CustomRegistrationForm2()
#     #  return HttpResponse (form)
#      return render (request, 'Candidate/custom_registration.html' ,{ 'form_data':form})
#     else:
#         form = CustomRegistrationForm2(request.POST)
#         # return HttpResponse(form)
#         first_name= request.POST['first_name']
#         email= request.POST['email']
#         username= request.POST['username']
#         password1= request.POST['password1']
#         password2= request.POST['password2']


#         if not password1:
#                 messages.error(request, 'Password cannot be empty')
#                 return redirect('custom_candidate_registration')     
#         elif User.objects.filter(first_name=first_name).exists():
#               messages.error(request,'Name already exist')
#               return redirect('custom_candidate_registration')
#         elif CustomUser.objects.filter(username=username).exists():
#              messages.error(request,'Username already exist')
#              return redirect('custom_candidate_registration')
#         elif CustomUser.objects.filter(email=email).exists():
#             messages.error(request,'email already exist')
#             return redirect('custom_candidate_registration')
       
#         elif CustomUser.objects.filter(password1=password1).exists():
#              messages.error(request,'password is already taken')
#              return redirect('custom_candidate_registration')
#         elif password1 != password2:
#             messages.error(request, 'Passwords do not match')
#             return redirect('custom_candidate_registration')

       
#         if form.is_valid():
#             # return HttpResponse ('suscuss')
#             form.save()
#             # return HttpResponse(form)
#             messages.success(request, 'Registration successfull')
#             return redirect(custom_candidate_login)
#         else:
#             messages.error (request,'Registration Failed')
#             return redirect ('custom_candidate_registration')

# def custom_candidate_login(request):
#     if request.method == 'GET':
#         return render(request, 'Candidate/login.html')
#     else:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # return HttpResponse (password)
#         if username and password:
#             custom_user = authenticate(request, username=username, password=password)
#             # return HttpResponse (custom_user)
#             if custom_user is not None :  # Check if custom_user is not None and active
#                 login(request, custom_user)
#                 messages.success(request, 'Logged In successfully!')
#                 return redirect('home')  # Redirect to the home page after successful login
#             else:
#                 messages.error(request, "Username or Password is incorrect")
#                 return redirect(custom_candidate_login) 
#         else:
#             messages.error(request, "Username and Password are required.")
#             return redirect(custom_candidate_login)  # Assuming 'candidate_login' is the name of your login URL pattern
#             # return HttpResponse(user)
#         # return HttpResponse(request.POST)




def candidate_login(request):
    if request.method == 'GET':
        return render(request,'Candidate/login.html')
    else:
        username = request.POST['username']
        user_password = request.POST['password']

        if username and user_password:
           user = authenticate(request,username=username, password=user_password)
        #    return HttpResponse (user)
           if user is not None:
                 login(request,user)
                 messages.success(request,'Logged In successfull!')
                 # return HttpResponse ()
                 return redirect(home)
           else:
                 messages.error(request,"Username or Password is incorrect")
                 return redirect(candidate_login)
        else:
             messages.error(request,"Username and Password are required.")
             return redirect(candidate_login)
            # return HttpResponse(user)
        # return HttpResponse(request.POST)

def candidate_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully!.")
    return redirect('candidate_login')


def candidates (request):
    users = User.objects.all()
    user_details = UserDetails.objects.all()
    #    return HttpResponse (users)
    return render(request, 'Candidate/candidates.html',{'users':users,'user_details':user_details})

def myprofile (request):
    # Get the currently logged-in user
    user = request.user
    # return HttpResponse (user)
    return render(request, 'Candidate/myprofile.html', {'user': user})

def profile_page (request,username):
    user_details = UserDetails.objects.filter(user__username=username).first()

    # return HttpResponse (user_details)
    return render (request,'Candidate/profile_page.html',{'user_details':user_details})

def candidate_profile_page (request,username):
    user = get_object_or_404(User, username=username)
    user_details = get_object_or_404(UserDetails, user=username)

    # return HttpResponse (user_details)
    return render (request,'Candidate/candidate_profile_page.html',{'user_details':user_details})

def employer_registration (request):
    if request.method == 'GET':
        form = BuiltinEmployerCreationForm()
        return render(request, 'Employer/registration.html', {'form_data': form})
    else:
        form = BuiltinEmployerCreationForm(request.POST, request.FILES)
        company = request.POST['company']
        if form.is_valid() and company:
            employer = form.save()
            
            emplyer_details = EmployerDetails(company = company, employer = employer , type = 1)
            emplyer_details.save()
            
            messages.success(request, 'User registered successfully')
            return redirect('employer_login')
        else:
            messages.error(request, 'You does not follow the instructions')
            return HttpResponse (form.errors)
        

def employer_login(request):
    if request.method == 'GET':
        return render(request,'Employer/login.html')
    else:
        username = request.POST['username']
        user_password = request.POST['password']

        if username and user_password:
           user = authenticate(request,username=username, password=user_password,type=1)
           # return HttpResponse (user)
           if user is not None:
                 login(request,user)
                 messages.success(request,'Logged In successfull!')
                 # return HttpResponse ()
                 return redirect(home)
           else:
                 messages.error(request,"Username or Password is incorrect")

                 return redirect(employer_login)
        else:
             messages.error(request,"Username and Password are required.")
             return redirect(employer_login)
            # return HttpResponse(user)
        # return HttpResponse(request.POST)

def about_us (request):
    return render (request, 'about_us.html')


def terms_for_users (request):
    return render (request, 'terms_for_users.html')

def contact_us(request):
    return render (request, 'contact_us.html')

def job_posting(request):
    if request.method == "GET":
        jobs= JobPostingForm()
        return render (request, 'Employer/job_posting.html',{'job_posting':jobs})
    else:
        job_posting = JobPostingForm(request.POST,request.FILES)
        if job_posting.is_valid():
            job_posting.save()
            messages.success(request,'Job Posted Successfully!')
            return redirect ('full_job_profile')
        else:
            messages.error (request,'Same Job has already posted')
            # return redirect( 'job_posting')
            return HttpResponse (job_posting.errors)

def jobs (request):
   jobs = JobPosting.objects.all()
   return render (request,'jobs.html',{'jobs':jobs})


def full_job_profile (request):

    jobs = JobPosting.objects.all()
    return render(request,'full_job_profile.html',{'jobs':jobs})

def privacy_and_policy(request):
    return render (request, 'terms_of_user.html')

def things_you_should_know(request):
    return render (request,'blogs/things_you_should_know.html')


def writing_resume(request):
    return render (request,'blogs/writing_resume.html')

def stay_confident(request):
    return render (request,'blogs/stay_confident.html')

def most_asked(request):
    return render (request,'blogs/most_asked.html')

def writing_email(request):
    return render (request,'blogs/writing_email.html')


def user_dashboard (request):
       # return HttpResponse(request.user.is_authenticated)
    # if request.user.is_authenticated:
        users = User.objects.all()
        return render(request,'Candidate/user_dashboard.html',{'users':users})
    # else:
        messages.error(request,'Kindly Login first')

        return HttpResponse(users)
        return  render (request,'dashboard.html')


def employers (request):
     employers=User.objects.all()
     employer_details=EmployerDetails.objects.all()
     return render (request, 'Employer/employers.html',{'employers':employers,'employer_details':employer_details})


def employer_dashboard (request):
    employers = User.objects.all ()
    return render (request,'Employer/employer_dashboard.html',{'employers':employers})

# def dashboard2 (request):
#        # return HttpResponse(request.user.is_authenticated)
#     # if request.user.is_authenticated:
#         custom_users = CustomUser.objects.all()
#         return render(request,'Candidate/dashboard2.html',{'users':custom_users})
#     # else:
#         messages.error(request,'Kindly Login first')

#         return HttpResponse(users)
#         return  render (request,'dashboard.html')

def user_edit (request,id):
    user = User.objects.get(id=request.user.id)
    # return HttpResponse(user)
    if request.method == 'GET':
        form =UserChangeCustomForm(request.POST or None,instance=request.user)
        # return HttpResponse (form)
        return render(request,'Candidate/user_edit.html',{'form_data':form,'user_id':request.user} )

        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        form = UserChangeCustomForm(request.POST,instance=request.user)
        # return HttpResponse (form)
        if form.is_valid:
            # return HttpResponse (form.errors)
            form.save()
            messages.success(request,'Record updated Successfully!')
            return redirect(user_details_edit,user.username)
        else:
            # return HttpResponse (form.errors)
            messages.error(request,'invalid data')
            return redirect('user_edit',id)

# def edit_custom_user (request,id):
#         custom_users =  CustomRegistrationForm2.objects.get(id=id)
#         # return HttpResponse(user)
#         if request.method == 'GET':
#             form = CustomRegistrationForm2(request.POST or None,instance=custom_users)
#             # return HttpResponse (form)
#             return render(request,'Candidate/dashboard2.html',{'form_data':form,'user_id':id} )

#             # form = UserChangeForm()
#             # return HttpResponse(form)
#             # return HttpResponse(f'edit: {id}')
#         else:
#             form = UserChangeCustomForm(request.POST,instance=custom_users)
#             # return HttpResponse (form)
#             if form.is_valid:
#                 # return HttpResponse (form.errors)
#                 form.save()
#                 messages.success(request,'Record updated Successfully!')
#                 return redirect(user_dashboard)
#             else:
#                 # return HttpResponse (form.errors)
#                 messages.error(request,'invalid data')
#                 return redirect('edit_user',id)

def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request,'User deleted Successfully!')
    return redirect('dashboard')


def user_edit (request,id):
    user = User.objects.get(id=request.user.id)
    # return HttpResponse(user)
    if request.method == 'GET':
        form =UserChangeCustomForm(request.POST or None,instance=request.user)
        # return HttpResponse (form)
        return render(request,'Candidate/user_edit.html',{'form_data':form,'user_id':request.user} )

        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        # specialization=request.get('specialization')
        form = UserChangeCustomForm(request.POST,instance=request.user)
        # return HttpResponse (form)
        if form.is_valid :
            # return HttpResponse (form.errors)
            form.save()
            messages.success(request,'Record updated Successfully!')
            return redirect(user_details_edit,user.username)
        else:
            # return HttpResponse (form.errors)
            messages.error(request,'invalid data')
            return redirect('user_edit',id)



def user_details(request):
   
    # return HttpResponse(user)
    if request.method == 'GET':
        user_edit = UserDetailsForm()
        return render(request,'Candidate/edit_user.html',{'user_edit':user_edit} )
        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        form = UserDetailsForm(request.POST)

        specialization= request.POST['specialization']
        edit_user= UserDetails (specialization=specialization,user=request.user,type='0')
        if form.is_valid() and specialization:
            return HttpResponse (form)
            user=form.save()
           
            edit_user.save()
            messages.success(request, 'User registered successfully.')
            return HttpResponse (edit_user)
        else:
            messages.error(request,'invalid data')
            return HttpResponse (form.errors)
        
 

def user_details_edit(request, username):
    if UserDetails or EmployerDetails==type==0:
    # Retrieve the UserDetails instance for the user with the given username
     user_details = UserDetails.objects.filter(user__username=username).first()

     if request.method == 'GET':
        # Pass the UserDetails instance to the form if it exists
        full_user_details_form = FullUserDetailsForm(instance=user_details) if user_details else FullUserDetailsForm()
        return render(request, 'Candidate/user_details_edit.html', {
            'full_user_details_form': full_user_details_form,
            'username': username
        })
     elif request.method == 'POST':
        specialization = request.POST.get('specialization')  # Use get to avoid KeyError
        
        # Pass the instance and additional data to the form
        full_user_details_form = FullEmployerDetailsForm(request.POST, instance=user_details)

        if full_user_details_form.is_valid() and specialization:
            full_user_details_instance = full_user_details_form.save(commit=False)
            full_user_details_instance.user = request.user  # Assign the User instance directly
            full_user_details_instance.specialization = specialization  # Update specialization field
            full_user_details_instance.save()
            
            messages.success(request, 'User record updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid information')
            # Redirect back to the edit page with the current username
            return redirect('user_edit', username=username)
    else:
           # Retrieve the UserDetails instance for the user with the given username
       employer_details = EmployerDetails.objects.filter(employer__username=username).first()

       if request.method == 'GET':
        # Pass the UserDetails instance to the form if it exists
        full_employer_details_form = FullEmployerDetailsForm(instance=employer_details) if employer_details else FullEmployerDetailsForm()
        return render(request, 'Employer/employer_details_edit.html', {
            'full_employer_details_form': full_employer_details_form,
            'username': username
        })
       elif request.method == 'POST':
        company = request.POST.get('company')  # Use get to avoid KeyError
        
        # Pass the instance and additional data to the form
        full_employer_details_form = FullEmployerDetailsForm(request.POST, instance=employer_details)

        if full_employer_details_form.is_valid() and company:
            full_employer_details_instance = full_employer_details_form.save(commit=False)
            full_employer_details_instance.user = request.user  # Assign the User instance directly
            full_employer_details_instance.company = company  # Update company field
            full_employer_details_instance.save()
            
            messages.success(request, 'User record updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid information')
            # Redirect back to the edit page with the current username
            return redirect('employer_edit', username=username)
        

def employer_edit (request,id):
    user = User.objects.get(id=request.user.id)
    # return HttpResponse(user)
    if request.method == 'GET':
        form =EmployerChangeCustomForm(request.POST or None,instance=request.user)
        # return HttpResponse (form)
        return render(request,'Employer/employer_edit.html',{'form_data':form,'user_id':request.user} )

        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        company = request.POST['company']
        form = EmployerChangeCustomForm(request.POST,instance=request.user)
        # return HttpResponse (form)
        if form.is_valid and company:
            # return HttpResponse (form.errors)
            form.save()
            messages.success(request,'Record updated Successfully!')
            return redirect(user_details_edit,username=user)
        else:
            # return HttpResponse (form.errors)
            messages.error(request,'invalid data') 
            return HttpResponse (form)                   
            return redirect('user_edit',id)


def employer_details_edit(request, username):
    # Retrieve the UserDetails instance for the user with the given username
    employer_details = EmployerDetails.objects.filter(employer__username=username).first()

    if request.method == 'GET':
        # Pass the UserDetails instance to the form if it exists
        full_employer_details_form = FullEmployerDetailsForm(instance=employer_details) if employer_details else FullEmployerDetailsForm()
        return render(request, 'Employer/employer_details_edit.html', {
            'full_employer_details_form': full_employer_details_form,
            'username': username
        })
    elif request.method == 'POST':
        company = request.POST.get('company')  # Use get to avoid KeyError
        
        # Pass the instance and additional data to the form
        full_employer_details_form = FullEmployerDetailsForm(request.POST, instance=employer_details)

        if full_employer_details_form.is_valid() and company:
            full_employer_details_instance = full_employer_details_form.save(commit=False)
            full_employer_details_instance.employer = request.user  # Assign the User instance directly
            full_employer_details_instance.company = company  # Update company field
            full_employer_details_instance.save()
            
            messages.success(request, 'User record updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid information')
            # Redirect back to the edit page with the current username
            return HttpResponse (full_employer_details_form.errors)
            return redirect('employer_edit')
# def edit_custom_user (request,id):
#     user = CustomRegistrationForm.objects.get(id=id)
#     # return HttpResponse(user)
#     if request.method == 'GET':
#         form =CustomRegistrationForm(request.POST or None,instance=user)
#         # return HttpResponse (form)
#         return render(request,'Candidate/custom_form.html',{'form_data':form,'user_id':id} )

#         # form = UserChangeForm()
#         # return HttpResponse(form)
#         # return HttpResponse(f'edit: {id}')
#     else:
#         form = CustomRegistrationForm(request.POST,instance=user)
#         # return HttpResponse (form)
#         if form.is_valid:
#             # return HttpResponse (form.errors)
#             form.save()
#             messages.success(request,'Record updated Successfully!')
#             return redirect(dashboard)
#         else:
#             # return HttpResponse (form.errors)
#             messages.error(request,'invalid data')
#             return redirect('edit_custom_user',id)