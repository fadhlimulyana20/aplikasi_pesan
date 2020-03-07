from django.shortcuts import render
from .form import Create_chat
from .models import Chat
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def create_chat(request):
    user = User.objects.get(id=request.user.id)
    form = Create_chat(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            update = form.save(commit = False)
            update.sender = user
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
        return HttpResponse("sent")
    else:
        form = Create_chat()
    context ={
        'form' :form,
    }
    return render(request, 'create_chat.html', context)

def inbox(request):
    chat_qs = Chat.objects.filter(destination=request.user.username)
    context = {
        'chat_qs' : chat_qs,
    }
    return render(request, 'inbox_chat.html', context)

def sent(request):
    chat_qs = Chat.objects.filter(sender=request.user)
    context = {
        'chat_qs' : chat_qs,
    }
    return render(request, 'sent_chat.html', context)
