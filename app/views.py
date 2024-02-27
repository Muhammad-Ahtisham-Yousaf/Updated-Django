from django.shortcuts import render, redirect
from django.http import HttpResponse


# user authentication
from django.contrib.auth import authenticate, login, logout

# user auth forms
from django.contrib.auth.forms import UserCreationForm
from .djangoForms.registration import BuiltinUserCreationForm
from .djangoForms.registration import BuiltinEmployerCreationForm

# for editing
from .djangoForms.password_edit_form import UserChangeCustomForm
# user auth model
from django.contrib.auth.models import User

# flash messages
from django.contrib import messages

#  Custom forms
from .djangoForms.job_posting import JobPostingForm
from .djangoForms.password_edit_form import EditUserForm

# Custom Models
from .models import JobPosting
from .models import EditUser
# Create your views here.
def home (request):
    # return HttpResponse( 'working')
   if request.user.is_authenticated:
      return  render (request , 'main.html')
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
        if form.is_valid():
            first_name = request.POST['first_name']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if not  password1:
                messages.error(request, 'Password cannot be empty')
                return redirect('candidate_registration')
            elif User.objects.filter(first_name=first_name).exists():
                messages.error(request, 'Name already exists')
                return redirect('candidate_registration')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('candidate_registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('candidate_registration')
            elif password1 != password2:
                messages.error(request, 'Passwords do not match')
                return redirect('candidate_registration')
          
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('candidate_login')
        else:
            first_name = request.POST['first_name']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if not  password1:
                messages.error(request, 'Password cannot be empty')
                return redirect('candidate_registration')
            elif User.objects.filter(first_name=first_name).exists():
                messages.error(request, 'Name already exists')
                return redirect('candidate_registration')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('candidate_registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('candidate_registration')
            elif password1 != password2:
                messages.error(request, 'Passwords do not match')
                return redirect('candidate_registration')

            messages.error(request, 'You does not follow the instructions')
            return redirect (candidate_registration)

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
           # return HttpResponse (user)
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

def candidates (request):
           users = User.objects.all()
        #    return HttpResponse (custom_users)
           return render(request, 'Candidate/candidates.html', {'users':users})

def myprofile (request):
    # Get the currently logged-in user
    user = request.user
    # return HttpResponse (user)
    return render(request, 'Candidate/myprofile.html', {'user': user})

def profile_page (request):
    user = request.user
    return render (request,'profile_page.html',{'user':user})


def employer_registration (request):
    if request.method == 'GET':
        form = BuiltinEmployerCreationForm()
        return render(request, 'Employer/registration.html', {'form_data': form})
    else:
        form = BuiltinEmployerCreationForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = request.POST['first_name']
            email = request.POST['email']
            username = request.POST['username']
            password2 = request.POST['password1']
            password1 = request.POST['password2']
            if not  password1:
                messages.error(request, 'Password cannot be empty')
                return redirect('employer_registration')
            elif User.objects.filter(first_name=first_name).exists():
                messages.error(request, 'Name already exists')
                return redirect('employer_registration')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('employer_registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('employer_registration')
            elif password1 != password2:
                 messages.error(request, 'Passwords do not match')
                 return redirect('employer_registration')
          
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('employer_login')
        else:
            first_name = request.POST['first_name']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
        
            if not  password1:
                messages.error(request, 'Password cannot be empty')
                return redirect('employer_registration')
            elif User.objects.filter(first_name=first_name).exists():
                messages.error(request, 'Name already exists')
                return redirect('employer_registration')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('employer_registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('employer_registration')
        

            messages.error(request, 'You does not follow the instructions')
            return HttpResponse (form.errors)
        

def employer_login(request):
    if request.method == 'GET':
        return render(request,'Employer/login.html')
    else:
        username = request.POST['username']
        user_password = request.POST['password']

        if username and user_password:
           user = authenticate(request,username=username, password=user_password)
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

def aboutus (request):
    return render (request, 'aboutus.html')

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
     return render (request, 'Employer/employers.html')


def employer_dashboard (request):
    employers = User.objects.all ()
    return render (request,'Employer/employer_dashboard.html',{ 'employers':employers})

# def dashboard2 (request):
#        # return HttpResponse(request.user.is_authenticated)
#     # if request.user.is_authenticated:
#         custom_users = CustomUser.objects.all()
#         return render(request,'Candidate/dashboard2.html',{'users':custom_users})
#     # else:
#         messages.error(request,'Kindly Login first')

#         return HttpResponse(users)
#         return  render (request,'dashboard.html')

def password_edit (request,id):
    user = User.objects.get(id=id)
    # return HttpResponse(user)
    if request.method == 'GET':
        form =UserChangeCustomForm(request.POST or None,instance=user)
        # return HttpResponse (form)
        return render(request,'Candidate/password_edit.html',{'form_data':form,'user_id':id} )

        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        form = UserChangeCustomForm(request.POST,instance=user)
        # return HttpResponse (form)
        if form.is_valid:
            # return HttpResponse (form.errors)
            form.save()
            messages.success(request,'Record updated Successfully!')
            return redirect(user_dashboard)
        else:
            # return HttpResponse (form.errors)
            messages.error(request,'invalid data')
            return redirect('edit_user',id)

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


def edit_user(request):
   
    # return HttpResponse(user)
    if request.method == 'GET':
        user_edit = EditUserForm(request.POST or None,instance=request.user)
        return render(request,'Candidate/edit_user.html',{'user_edit':user_edit} )
        # form = UserChangeForm()
        # return HttpResponse(form)
        # return HttpResponse(f'edit: {id}')
    else:
        form = EditUserForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request,'Record updated Successfully!')
            return redirect(home)
        else:
            messages.error(request,'invalid data')
            return HttpResponse (form.errors)


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