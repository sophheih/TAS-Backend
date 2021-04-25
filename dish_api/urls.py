from django.urls import path
from dish_api import views
urlpatterns = [
    path('new', views.storeNutrition),
    path('get', views.get_dish),
    path('update', views.update_dish),
    path('delete', views.delete_dish)
]



