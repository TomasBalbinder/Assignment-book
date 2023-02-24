from django.contrib.auth.models import User

def password(request):
    if request.POST['password1'] != request.POST['password2']:
        return True



def nickname(request):
    if User.objects.filter(username=request.POST['username']).exists():
        return True


def email(request):
    if User.objects.filter(email=request.POST['email']).exists():
        return True
