from abc import ABC, abstractmethod

class Resource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class HeavyResource(Resource):
    def __init__(self):
        print("Тяжелый ресурс инициализируется...")
        self._data = "Важные данные"

    def get_data(self):
        return self._data

class ResourceProxy(Resource):
    def __init__(self):
        self._resource = None

    def get_data(self):
        if self._resource is None:
            self._resource = HeavyResource()
        return self._resource.get_data()

# Пример использования
proxy = ResourceProxy()

# Ресурс загружается только при первом запросе данных
print("Запрос данных через прокси...")
print(proxy.get_data())

# Ресурс уже загружен, повторный запрос данных не инициализирует его заново
print("Повторный запрос данных через прокси...")
print(proxy.get_data())