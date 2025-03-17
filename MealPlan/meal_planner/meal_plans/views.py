from django.shortcuts import render

# Create your views here.
def home(request):
    """Homepage for the Meal Planner app."""
    return render(request, 'meal_plans/home.html')