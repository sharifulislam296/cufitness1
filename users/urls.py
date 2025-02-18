from django.urls import path
from .views import home, user_logout, register, profile

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('/accounts/profile/', profile, name='profile'),
    path('profile/', profile, name='profile'),

]
