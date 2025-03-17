from django.shortcuts import render
from .models import Pizza

def home(request):
    """View function for the home page."""
    return render(request, 'pizzas/home.html')

# View to show all pizzas
def pizzas_list(request):
    pizzas = Pizza.objects.all()  # Retrieve all pizzas
    return render(request, 'pizzas/pizzas_list.html', {'pizzas': pizzas})

# View to show toppings for a selected pizza
def pizza_detail(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)  # Retrieve the selected pizza
    toppings = pizza.toppings_set.all()  # Retrieve all toppings for the selected pizza
    return render(request, 'pizzas/pizza_detail.html', {'pizza': pizza, 'toppings': toppings})

