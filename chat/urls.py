from django.urls import path

from .views import create_chat, inbox, sent

app_name = 'chat'
urlpatterns = [
    path('create_chat/', create_chat, name='chat'),
    path('inbox_chat/', inbox, name='inbox_chat'),
    path('sent_chat/', sent, name='sent_chat'),
]
