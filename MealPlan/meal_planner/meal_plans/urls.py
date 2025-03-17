from django.urls import path
from . import views

app_name = 'meal_plans'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
]