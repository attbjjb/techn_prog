class House:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_roof(self):
        self.house.add_part("крыша")
        return self

    def build_walls(self):
        self.house.add_part("стены")
        return self

    def build_foundation(self):
        self.house.add_part("фундамент")
        return self

    def build_windows(self):
        self.house.add_part("окна")
        return self

    def build(self):
        return self.house

builder = HouseBuilder()
house = builder.build_foundation().build_walls().build_roof().build_windows().build()
print(house.parts)
