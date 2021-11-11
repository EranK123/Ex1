import Elevator as Elevator


class Building:
    elevs = []

    def __init__(self, min_floor, max_floor, elevs):
        self.min_floor = min_floor
        self.max_floor = max_floor
        building = Building(min_floor, max_floor, elevs)
        for i in building.elevs:
            i = Elevator(building)

    def get_elev(self, index) -> Elevator:
        return self.elevs[index]

    def number_of_elevs(self) -> int:
        return len(self.elevs)
