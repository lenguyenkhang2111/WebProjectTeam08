
# Create your views here.

# Create your views here.

from django.shortcuts import redirect, render
from django.http import HttpResponse
from account.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from WebProjectTeam08 import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from . tokens import generate_token

# Create your views here.


# sign


def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # neu đã có username
        if Account.objects.filter(username=username):
            messages.error(
                request, "User name already exist!!! Please try some other username")
            return redirect('signup')
        if Account.objects.filter(email=email):
            messages.error(request, "Email already exist!!!")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if password1 != password2:
            messages.error(request, "Password didn't match!!!")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha_Numberic!!!")
            return redirect('signup')

        myuser = Account.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, username=username, password=password1)

        myuser.save()

        messages.success(
            request, "Your Account has been successfully create. ")

        # Welcome email
        subject = "Welcome to NAME- Django login"
        message = "Hello" + myuser.first_name + \
            "!!! \n" + "Welcome to NAME!!! \n Thanks you buying our court \n we have also send you a confirmation email, please confirm your email address in oder to active your account. \n\n Thanking you \n NAME "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Adress Confirm

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ hocDjango"
        message2 = render_to_string('account/email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(

            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect("signin")

    return render(request, "account/signup.html")

# sign in


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "home.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')

    return render(request, "account/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'account/activation_failed.html')
