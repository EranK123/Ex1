class Elevator:

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
        self.time = 0
