from abc import ABCMeta, abstractmethod

from chair import ChairFactory
from table import TableFactory


class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract furniture factory interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "The static Abstract factory interface method"


class FurnitureFactory(IFurnitureFactory):
    "The Abstract factory concrete class"

    @staticmethod
    def get_furniture(furniture):
        "Static get_factory method"
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory().get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory().get_table(furniture)
            raise Exception("No factory found")
        except Exception as _e:
            print(_e)
        return None
