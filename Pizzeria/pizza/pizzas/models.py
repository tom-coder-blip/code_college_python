from django.db import models

# Create your models here.

class Pizza(models.Model):
    """A type of pizza available in the pizzeria."""
    name = models.CharField(max_length=200) #Stores the pizza name (e.g., Hawaiian)

    def __str__(self):
        """Return a string representation of the pizza."""
        return self.name


class Topping(models.Model):
    """Toppings available for pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE) #Links to a Pizza
    name = models.CharField(max_length=200) #Stores topping name (e.g., Pepperoni)

    def __str__(self):
        """Return a string representation of the topping."""
        return self.name