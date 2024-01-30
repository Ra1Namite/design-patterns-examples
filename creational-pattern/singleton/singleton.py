class Singleton:
    "classical singleton pattern"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class LazySingleton:
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


if __name__ == "__main__":
    print("Classical Singleton pattern")
    s = Singleton()
    s1 = Singleton()
    print(s1 is s)

    print("\n\n Lazy Singleton pattern")
    lazy = LazySingleton()
    print(lazy)

    lazy1 = LazySingleton.getInstance()
    print(lazy1)
    lazy2 = LazySingleton()
    print(lazy2)
