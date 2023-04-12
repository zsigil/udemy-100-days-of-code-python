def add(*args):
    sum = 0
    #args is a tuple
    for n in args:
        sum += n
    return sum


print(add(5,6,7))


def calculate(n, **kwargs):
    #kwargs is a dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw["make"] #will crash if make not provided
        self.model = kw.get("model")


my_car = Car(make="VW")
print(my_car.model) # "None"

