class Singleton:
    _instance = None

    def __new__(clss):
        if clss._instance is None:
            clss._instance = super(Singleton, clss).__new__(clss)
        return clss._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

