from project.meals.meal import Meal


class MainDish(Meal):

    def __init__(self, name: str, price: float, quantity: int = 50):
        super().__init__(name, price, quantity)

    @property
    def type_of_meal(self):
        return "Main Dish"
