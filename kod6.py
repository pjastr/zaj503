class Car:

    def __init__(self, serial, capacity):
        self.serial = serial
        self.capacity = capacity

    def load(self, good):
        pass

    def __repr__(self):
        return f"Car: {self.serial},{self.capacity}"

    def __lt__(self, other):
        return (other.serial, other.capacity) < (self.serial, self.capacity)


class PassengerCar(Car):

    def load(self, passengers):
        self.capacity += passengers

    def __repr__(self):
        return f"PassengerCar: {self.serial},{self.capacity}"


class FirstClassCar(Car):

    def load(self, passengers):
        self.capacity += 2 * passengers

    def __repr__(self):
        return f"FirstClassCar: {self.serial},{self.capacity}"


class FreightCar(Car):
    def __init__(self, serial):
        self.goods = []
        super().__init__(serial, 0)

    def load(self, good):
        self.capacity += 1
        self.goods.append(good)

    def __repr__(self):
        return f"FreightCar: {self.serial},{self.capacity},{self.goods}"


cars = [Car("AC233",20), PassengerCar("WX233", 100), FirstClassCar("tg455", 50),
        FreightCar("pt345")]
print(cars)
cars.sort()
print(cars)
