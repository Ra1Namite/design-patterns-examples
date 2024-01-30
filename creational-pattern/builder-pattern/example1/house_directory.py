from house import HouseBuilder


class IglooDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        """Constructs and returns the final product
        Note that in this IglooDirector, it has omitted the set_number_of
        windows call since this Igloo will have no windows.
        """

        return (
            HouseBuilder()
            .set_building_type("Igloo")
            .set_wall_material("Ice")
            .set_number_doors(1)
            .get_result()
        )


class CastleDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return (
            HouseBuilder()
            .set_building_type("Castle")
            .set_wall_material("Sandstone")
            .set_number_doors(100)
            .set_number_windows(200)
            .get_result()
        )


class HouseBoatDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return (
            HouseBuilder()
            .set_building_type("House Boat")
            .set_wall_material("Wood")
            .set_number_doors(6)
            .set_number_windows(8)
            .get_result()
        )


if __name__ == "__main__":
    # client
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    HOUSEBOAT = HouseBoatDirector.construct()

    print(IGLOO.construction())
    print(CASTLE.construction())
    print(HOUSEBOAT.construction())
