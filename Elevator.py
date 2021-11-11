from Building import Building


class Elevator:
    UP = 1
    Down = -1
    Level = 0

    def __init__(self, building: Building):
        self.building = building
        self.state = self.Level
        self.pos = 0
        self.open_time = 0
        self.close_time = 0
        self.start_time = 0
        self.stop_time = 0

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
        return self.open_time

    def get_time_for_close(self):
        return self.close_time

    def get_start_time(self):
        return self.state

    def get_stop_time(self):
        return self.stop_time

    def get_max_floor(self):
        return self.building.max_floor

    def get_min_floor(self):
        return self.building.min_floor


