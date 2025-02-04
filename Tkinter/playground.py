# def add(*args):
#     sum=0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(1,2,3,4,5))
# print(add(1,2))
# print(add(1))
# print(add())
# print(add(1,2,3,4,5,6,7,8,9))


def calculate(n, **kwargs):
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)


calculate(3,add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)