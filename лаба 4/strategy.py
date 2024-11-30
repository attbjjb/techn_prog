from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        print("Сортировка пузырьком")
        return sorted(data)

class InsertionSortStrategy(SortStrategy):
    def sort(self, data):
        print("Сортировка вставками")
        return sorted(data)

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Быстрая сортировка")
        return sorted(data)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)

# Пример использования
data = [5, 2, 9, 1, 5, 6]

sorter = Sorter(BubbleSortStrategy())
sorted_data = sorter.sort_data(data)
print(sorted_data)

sorter.set_strategy(QuickSortStrategy())
sorted_data = sorter.sort_data(data)
print(sorted_data)