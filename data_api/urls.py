from django.urls import path
from data_api import views
urlpatterns = [
    path('new', views.add_member),
    path('get/<slug:member_id>/<slug:timestamp>', views.data),
    
    
]
