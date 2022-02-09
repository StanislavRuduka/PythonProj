class Car:
    def __init__(self, model, color, engine, gear_type, year):  # attributes to be given when object is created of
        # type "Car"
        self.model = model
        self.color = color
        self.engine = engine
        self.gear_type = gear_type
        self.year = year

    def __str__(self):  # will be needed to print out the options of the cars
        return f'{self.model}, {self.color}, {self.engine}, {self.gear_type}, {self.year}'


class Dealer:
    car0 = Car('Toyota', 'White', 3.5, 'Manual', 2015)
    car1 = Car('BMW', 'Black', 4.4, 'Automatic', 2020)
    car2 = Car('Audi', 'Red', 2.0, 'Automatic', 2019)

    list_of_cars = [car0, car1, car2]  # creating a list of available cars

    def car_sell(self):
        print("Choose a car to buy?")
        counter = 0
        for i in self.list_of_cars:  # print available options due to __str__ used in Car class
            print(f'{counter}. {i}')
            counter += 1
        choice = int(input())
        print(f'{self.list_of_cars[choice].model} has been sold, thank you!')
        self.list_of_cars.pop(choice)  # remove sold car from the available catalog
        var_name = 'car' + str(choice)  # get the variable name for delattr
        delattr(Dealer, var_name)


deal = Dealer().car_sell()

deal2 = Dealer().car_sell()
