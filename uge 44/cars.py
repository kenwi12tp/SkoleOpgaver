cars = {}
def build_car(cars):
    car_brand = input("What's the brand of car? ")
    model = input("What's the model of the car? ")
    color = input("What's the color of the car? ")
    towpackage = input("does it have towpackage) ")
    cars.update({car_brand: {"model": model,}, "color": color, "towpackage": towpackage})
    return cars
car = build_car(cars)
print(car)
