# абстрактная фабрика

class CarFactory:
    def create_engine(self):
        raise NotImplementedError()
    def create_color(self):
        raise NotImplementedError()

class DefaultCarFac(CarFactory):
    def create_engine(self):
        return "двигатель 150 л.с."

    def create_color(self):
        return "красный цвет"

class FastCarFac(CarFactory):
    def create_engine(self):
        return "двигатель 540 л.с."

    def create_color(self):
        return "серебристый цвет"

def create_car(factory: CarFactory):
    engine = factory.create_engine()
    color = factory.create_color()
    return f'В автомобиле установлен {engine} и автомобиль имеет {color}'

default_car = create_car(DefaultCarFac())
fast_car = create_car(FastCarFac())

print(default_car)
print(fast_car)