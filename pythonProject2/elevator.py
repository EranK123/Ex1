
class Elevator:

    # UP = 1
    # DOWN = -1
    # LEVEL = 0

    def __init__(self, elevator, index_of_elevator):
        self.index_of_elevator = index_of_elevator
        self.id = elevator[index_of_elevator]["_id"]
        self.speed = elevator[index_of_elevator]["_speed"]
        self.min_floor = elevator[index_of_elevator]["_minFloor"]
        self.max_floor = elevator[index_of_elevator]["_maxFloor"]
        self.close_time = elevator[index_of_elevator]["_closeTime"]
        self.open_time = elevator[index_of_elevator]["_openTime"]
        self.start_time = elevator[index_of_elevator]["_startTime"]
        self.stop_time = elevator[index_of_elevator]["_stopTime"]




    # def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
    #     self.id = id
    #     self.speed = speed
    #     self.min_floor = min_floor
    #     self.max_floor = max_floor
    #     self.close_time = close_time
    #     self.open_time = open_time
    #     self.start_time = start_time
    #     self.stop_time = stop_time

    # def get_min_floor(self):
    #     return