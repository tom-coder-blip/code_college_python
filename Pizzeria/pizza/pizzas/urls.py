from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('', views.pizzas_list, name='pizzas_list'),  # URL for pizza list page
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),  # URL for pizza detail page
]