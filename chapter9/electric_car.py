from car import Car as c
from battery import Battery as b


class ElectricCar(c):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = b


    def fill_gas_tank(self):
        print("This car cannot take gas.") 

new_car = ElectricCar("VW", "Up", 2020) 





