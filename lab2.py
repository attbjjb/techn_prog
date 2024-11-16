class GameObject:
    def __init__(self, object_id, name, x, y):
        self.object_id = object_id  # Уникальный идентификатор объекта
        self.name = name            # Имя объекта
        self.x = x                  # Координата X объекта
        self.y = y                  # Координата Y объекта

    def get_id(self):
        return self.object_id       # Возвращает идентификатор объекта

    def get_name(self):
        return self.name            # Возвращает имя объекта

    def get_x(self):
        return self.x               # Возвращает координату X объекта

    def get_y(self):
        return self.y               # Возвращает координату Y объекта


class Building(GameObject):
    def __init__(self, object_id, name, x, y):
        # Инициализация здания с ID, именем и координатами (x, y)
        super().__init__(object_id, name, x, y)
        self.built = False  # Указывает, построено ли здание

    def is_built(self):
        # Возвращает, построено ли здание
        return self.built


class Fort(Building):
    def __init__(self, object_id, name, x, y):
        # Инициализация крепости, который является типом здания
        super().__init__(object_id, name, x, y)

    def attack(self, unit):
        # Атака юнита, нанося фиксированный урон
        damage = 10
        unit.receive_damage(damage)


class MobileHome(Building):
    def __init__(self, object_id, name, x, y):
        # Инициализация мобильного дома, который является типом здания
        super().__init__(object_id, name, x, y)

    def move(self, direction):
        # Перемещение мобильного дома в указанном направлении
        if direction == "на север":
            self.y += 1  # Движение на север
        elif direction == "на юг":
            self.y -= 1  # Движение на юг
        elif direction == "на восток":
            self.x += 1  # Движение на восток
        elif direction == "на запад":
            self.x -= 1  # Движение на запад
        print(f"{self.name} сдвинулся {direction} на ({self.x}, {self.y})")  # Вывод информации о перемещении


class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        # Инициализация юнита с очками здоровья (hp)
        super().__init__(object_id, name, x, y)
        self.hp = hp

    def is_alive(self):
        # Проверка, жив ли юнит на основе его очков здоровья
        return self.hp > 0

    def get_hp(self):
        # Возвращает текущее количество очков здоровья юнита
        return self.hp

    def receive_damage(self, damage):
        # Уменьшает количество очков здоровья юнита на величину урона
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0  # Обеспечивает, чтобы очки здоровья не опускались ниже нуля


class Attacker:
    def attack(self, unit):
        # Этот метод должен быть переопределён в подклассах
        raise NotImplementedError("надо переопределить")


class Moveable:
    def move(self, direction):
        # Этот метод должен быть переопределён в подклассах
        raise NotImplementedError("надо переопределить")


class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id, name, x, y, hp):
        # Инициализация лучника, который является типом юнита и может атаковать и перемещаться
        super().__init__(object_id, name, x, y, hp)

    def attack(self, unit):
        # Атака юнита, при нанесении фиксированный урон
        damage = 5
        unit.receive_damage(damage)
        print(f"{self.name} атаковал {unit.get_name()} на {damage} HP!")  # Вывод информации об атаке


# Примеры
fort = Fort(1, "Крепость", 0, 0)  # Создание объекта форта
archer = Archer(2, "Лучник", 2, 4, 100)  # Создание объекта лучника

# Вывод информации о форте и лучнике
print(f"Номер крепости: {fort.get_id()}, Имя: {fort.get_name()}, Позиция: ({fort.get_x()}, {fort.get_y()})")
print(f"Номер лучника: {archer.get_id()}, Имя: {archer.get_name()}, Здоровье: {archer.get_hp()}")

# Атака
fort.attack(archer)  # Форт атакует лучника
print(f"Здоровье лучника после атаки: {archer.get_hp()}")  # Вывод здоровья лучника после атаки

# Движение
mobile_home = MobileHome(3, "дом на колесах", 5, 3)  # Создание объекта мобильного дома
mobile_home.move("на юг")  # Перемещение мобильного дома на юг