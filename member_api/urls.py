from django.urls import path
from member_api import views
urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('<slug:user_id>', views.member_id)
    
    #/member/(user_id url) ==> <slug:user_id>
]