
from django.urls import path
from user.views import signup, signin, signout, modify
from user import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signout/', views.signout, name='signout'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('modify/', modify, name='modify'),
]