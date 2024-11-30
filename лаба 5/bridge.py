from abc import ABC, abstractmethod

class GraphicsLibrary(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

    @abstractmethod
    def draw_square(self, x, y, side):
        pass

class SimpleGraphics(GraphicsLibrary):
    def draw_circle(self, x, y, radius):
        print(f"SimpleGraphics: Рисуем круг в ({x}, {y}) с радиусом {radius}")

    def draw_square(self, x, y, side):
        print(f"SimpleGraphics: Рисуем квадрат в ({x}, {y}) со стороной {side}")

class AdvancedGraphics(GraphicsLibrary):
    def draw_circle(self, x, y, radius):
        print(f"AdvancedGraphics: Рисуем круг в ({x}, {y}) с радиусом {radius}")

    def draw_square(self, x, y, side):
        print(f"AdvancedGraphics: Рисуем квадрат в ({x}, {y}) со стороной {side}")

class Shape(ABC):
    def __init__(self, graphics: GraphicsLibrary):
        self._graphics = graphics

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, graphics: GraphicsLibrary, x, y, radius):
        super().__init__(graphics)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        self._graphics.draw_circle(self._x, self._y, self._radius)

class Square(Shape):
    def __init__(self, graphics: GraphicsLibrary, x, y, side):
        super().__init__(graphics)
        self._x = x
        self._y = y
        self._side = side

    def draw(self):
        self._graphics.draw_square(self._x, self._y, self._side)

# Пример использования
simple_graphics = SimpleGraphics()
advanced_graphics = AdvancedGraphics()

circle = Circle(simple_graphics, 10, 10, 5)
circle.draw()

square = Square(advanced_graphics, 20, 20, 10)
square.draw()