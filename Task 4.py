class Car:
    def __init__(self, color):  # attributes to be given when object is created of
        # type "Car"
        self.color = color


class Car_model(Car):

    def __init__(self, color, model):
        super().__init__(color)
        self.model = model


class engine_specification(Car_model):

    def __init__(self, color, model, engine):
        super().__init__(color, model)
        self.engine = engine

    def __str__(self):
        return f'Color: {self.color}, Model: {self.model}, Engine: {self.engine}'


car1 = engine_specification('black', 'toyota camry', 3.5)
car2 = engine_specification('black', 'BMW 525M', 4.4)
car3 = engine_specification('black', 'Nissan GTR', 3.8)

print(car1, car2, car3, sep='\n')
