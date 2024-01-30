from abc import ABCMeta, abstractmethod


class House:
    "The Product"

    def __init__(
        self, building_type="Apartment", doors=0, windows=0, wall_material="Brick"
    ):
        # brick, wood, straw, ice
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hut, Castle, Duplex,
        # HouseBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        return (
            f"This is a {self.wall_material} "
            f"{self.building_type} with {self.doors} "
            f"door(s) and {self.windows} window(s)."
        )


class IHouseBuilder(metaclass=ABCMeta):
    "The House Builder Interface"

    @abstractmethod
    def set_building_type(self, building_type):
        "Build type"

    @abstractmethod
    def set_wall_material(self, wall_material):
        "Build material"

    @abstractmethod
    def set_number_doors(self, number):
        "Number of doors"

    @abstractmethod
    def set_number_windows(self, number):
        "Number of windows"

    @abstractmethod
    def get_result(self):
        "Return the final product"


class HouseBuilder(IHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house
