from accounts import views
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
