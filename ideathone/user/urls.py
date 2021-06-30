from django.urls import path
from .views import *

app_name = 'user'

urlpatterns=[
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
]