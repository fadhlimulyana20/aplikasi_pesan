from django.urls import path

from .views import signup_view, user_logout, create_profile, signin_view, home_view

app_name = 'registration'
urlpatterns = [
    path('sign_up/', signup_view, name='sign_up'),
    path('sign_in/', signin_view, name='sign_in'),
    path('logout/', user_logout, name='user_logout'),
    path('create_profile/', create_profile, name='create_profile'),
    path('', home_view, name='home')
]

