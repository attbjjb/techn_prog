from abc import ABC, abstractmethod

class ModernPrinter(ABC):
    @abstractmethod
    def print_modern(self, text):
        pass

class LegacyPrinter:
    def print_legacy(self, text):
        print(f"LegacyPrinter: {text}")

class LegacyPrinterAdapter(ModernPrinter):
    def __init__(self, legacy_printer: LegacyPrinter):
        self._legacy_printer = legacy_printer

    def print_modern(self, text):
        self._legacy_printer.print_legacy(text)

# Пример использования
legacy_printer = LegacyPrinter()
adapter = LegacyPrinterAdapter(legacy_printer)

adapter.print_modern("Привет, мир!")