from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    "The Table Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"


class SmallTable(ITable):
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 50
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return dict(width=self._width, depth=self._depth, height=self._height)


class MediumTable(ITable):
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 110
        self._depth = 70

    def get_dimensions(self):
        return dict(width=self._width, depth=self._depth, height=self._height)


class BigTable(ITable):
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80

    def get_dimensions(self):
        return dict(width=self._width, depth=self._depth, height=self._height)


class TableFactory:
    "The Factory class"

    @staticmethod
    def get_table(table):
        "A static method to get a table"
        try:
            if table == "BigTable":
                return BigTable()
            if table == "MediumTable":
                return MediumTable()
            if table == "SmallTable":
                return SmallTable()
            raise Exception("Table Not Found")
        except Exception as _e:
            print(_e)
            return None
