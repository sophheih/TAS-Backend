from django.urls import path
from data_api import views
urlpatterns = [
    path('new', views.add_member),
    path('get', views.get_member),
    
    
]
