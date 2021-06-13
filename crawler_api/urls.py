from django.urls import path
from crawler_api import views
urlpatterns = [
    path('new', views.storeDailyMenu),
    path('get', views.get_Menu),
    path('update', views.update_menu),
    
    # path('input/<slug:index>', views.input_filtDish)

    
    
    
]



