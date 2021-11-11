from Building import Building


class Elevator:
    UP = 1
    Down = -1
    Level = 0

    def __init__(self, building: Building):
        self.building = building
        self.state = self.Level
        self.pos = 0

    def get_state(self):
        if self.UP:
            return 1
        elif self.Down:
            return -1
        else:
            return 0

    def ID(self, elevator):
        return self.building.elevs.index(elevator)

    def get_pos(self):
        return self.pos

    def get_time_for_open(self):
        return

    def get_time_for_close(self):
        pass
