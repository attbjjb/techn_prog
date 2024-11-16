class Bakery:
    def create_product(self):
        raise NotImplementedError()

class Cake(Bakery):
    def create_product(self):
        return "Создание торта"

class Pancake(Bakery):
    def create_product(self):
        return "Создание панкейка"

class Eclair(Bakery):
    def create_product(self):
        return "Создание эклера"

# Фабрика
class Confectionary:
    @staticmethod
    def create_product(product_type):
        if product_type == "торт":
            return Cake().create_product()
        elif product_type == "эклер":
            return Eclair().create_product()
        else:
            return Pancake().create_product()

# вызов
print(Confectionary.create_product("торт"))
print(Confectionary.create_product("эклер"))
print(Confectionary.create_product("панкейк"))