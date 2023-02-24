from django.shortcuts import render, redirect
from django.contrib import messages
from .utility import authentication
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import TodoForm, CustomRegisterForm, UserUpdateForm, UpdateProfilePicture, LoginForm, ResetForm
from .models import TodoModel
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site  
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .restapi import motivation_api
from django.conf import settings


# Create your views here



def home_page(request):   
    return render(request, 'ToDoApp/home_page.html')



def sign_up_user(request):

    if request.method == "GET":
        return render(request, 'ToDoApp/signup_user.html', {'form' : CustomRegisterForm()}) #create form

    else:
        if  authentication.password(request) and authentication.nickname(request):
            messages.error(request, 'nickname is exist', extra_tags='nickname')
            messages.error(request, 'password is wrong', extra_tags='password')
                           
        elif authentication.password(request):
            messages.error(request, 'password is wrong.', extra_tags='password')                       
               
        elif authentication.nickname(request):
            messages.error(request, 'Nickname is Exist.', extra_tags='nickname')
                 
        else:
            if request.method == "POST":               
                form = CustomRegisterForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    user = form.save(commit=False)
                    user.is_active = False      
                    user.save() 
                    current_site = get_current_site(request)
                    mail_subject = 'Activation link has been sent to your email id'  
                    message = render_to_string('ToDoApp/active_email.html', {  
                        'user': user,  
                        'domain': current_site.domain,  
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                        'token':account_activation_token.make_token(user),  
                    })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=[to_email]) 
                    email.send() 
                    return render(request, 'ToDoApp/sent_email.html', {'username' : username})
                    
                else:
                    form = CustomRegisterForm()
                    return render(request, 'ToDoApp/signup_user.html', {'form' : form})

    return render(request, 'ToDoApp/signup_user.html', {'form' : CustomRegisterForm()})




def activate_account(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid) 

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'ToDoApp/message_email.html')  
    else: 
        return render(request, 'ToDoApp/invalid_email.html')     

def current_login(request):
    response = motivation_api(request)
    split_text = response.text.split('-')
    context = {'text' : split_text[0], 
                'author' : split_text[1]}
    return render(request, 'ToDoApp/current_login.html',{'context' : context})




def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



def login_user(request):
    if request.method == "GET":
        return render(request, 'ToDoApp/login_user.html', {'form' : LoginForm()})

    username = request.POST['username']
    password = request.POST['password1']
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        username = user.get_username()
        messages.success(request, f'Your login has been successful, welcome {username}')
        return redirect('current')
   
    else:
        messages.error(request, 'Wrong password or nickname.', extra_tags='nickname')        
    return render(request, 'ToDoApp/login_user.html', {'form' : LoginForm()})



def create_article(request):

    if request.method == "GET":
        form = TodoForm()
        return render(request, 'ToDoApp/create_article.html', {'form' : form})

    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user   
        newtodo.save()
        messages.add_message(request, messages.SUCCESS, f'{newtodo.title}')
        return redirect('createtodo')



def show_posts(request):  
    mydata = TodoModel.objects.filter(user=request.user).order_by('-important','created')

    if not mydata:
        messages.error(request, 'You have no posts', extra_tags='noposts') 
        return render(request, 'ToDoApp/show_posts.html', {'mydata' : mydata})

    else:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')

            if not id_list:
                return render(request, 'ToDoApp/show_posts.html', {'mydata' : mydata})

            else:                  
                mydata.filter(pk__in=id_list).delete()
                messages.success(request, ("Delete data was success!"))
                return redirect('showposts')

        else:     
            return render(request, 'ToDoApp/show_posts.html', {'mydata' : mydata})




def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = ResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "ToDoApp/password/password_reset_email.txt"
                    c = {
                    'email':user.email,
                    'domain':'assignment-book1.onrender.com',
                    'site_name': 'Website',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'Assignment book' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('password_reset_done')
            messages.success(request, f'update was successful')
    password_reset_form = ResetForm()
    return render(request, "ToDoApp/password/password_reset.html", {"password_reset_form":password_reset_form})




@login_required
def profile(request):

    if request.method == "POST":
        user_update = UserUpdateForm(request.POST, instance=request.user)
        image_update = UpdateProfilePicture(request.POST, request.FILES, instance=request.user.profile)
        print(user_update)

        if user_update.is_valid() and image_update.is_valid():

            user_update.save()
            image_update.save()

            messages.success(request, f'update was successful')
            return redirect('profile')
    else:
        user_update = UserUpdateForm(instance=request.user)
        image_update = UpdateProfilePicture(instance=request.user.profile)

    
    context = {'user_update' : user_update, 
                'image_update' : image_update}
    return render(request, 'ToDoApp/profile.html', context)



def delete_account(request, pk):
    delete_user = User.objects.get(pk=pk) 
    if request.method == "POST":
        delete_user.delete()
        return render(request, 'ToDoApp/home_page.html')
    return render(request, 'ToDoApp/delete_confirm.html')





    


