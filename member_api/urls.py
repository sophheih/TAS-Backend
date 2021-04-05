from django.urls import path
from member_api import views
urlpatterns = [
    path('register', views.register),
    path('login', views.login)
]