from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .form import SignUpForm, UpdateProfileForm, SignInForm
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            # email = form.clean_email()
            # username = form.cleaned_data.get('username')
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return HttpResponseRedirect(reverse("registration:create_profile"))
    else:
        form = SignUpForm()
    
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def signin_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registration:home'))
    else:
        form = SignInForm(request.POST)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return HttpResponseRedirect(request.POST.get('next')    )
                    return HttpResponseRedirect(reverse('registration:home'))
                else:
                    return HttpResponse("Your account is inactive")
            else:
                print("Someone tried to login and failed")
                print("He used username : {}, password : {}".format(username, password))
                messages.error(request,'username atau password salah')
                return HttpResponseRedirect(reverse('registration:sign_in'))
        else:
            form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, 'signin.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration:home'))

def create_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)

        profile = user.profile
        
        form = UpdateProfileForm(instance=profile)

        if user.is_authenticated:
            if request.method == 'POST':
                form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
                if form.is_valid:
                    update = form.save(commit = False)
                    update.user = user
                    update.save()
                    # mail_subject = 'Selamat Datang di Aplikasi SunatLem'
                    # message = render_to_string('greeting_email.html', {
                    #     'logo' : 'http://app.sunatlemindonesia.com/static/img/sunatlem-banner.png',
                    # })
                    # to_email = request.user.email
                    # email = EmailMessage(
                    #     mail_subject, message, to=[to_email]
                    # )
                    # email.content_subtype = "html"
                    # email.send()
                return HttpResponseRedirect(reverse('registration:home'))
        else:
            form = UpdateProfileForm(instance=profile)
        context ={
            'form' :form,
            'profile' :profile
        }
        return render(request, 'create_profile.html', context)
    else:
        return HttpResponse("belum login")

@login_required
def home_view(request):
    return render(request,'home.html')

