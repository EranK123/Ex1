

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
        self.pos = 0
        self.time = 0
        self.state = 0 #level

    def dist1(self, src, dest):
        temp = -1
        if src == dest:
            return temp
        else:
            dis = abs(dest - src)
            dis *= self.speed
            dis += self.close_time + self.open_time + self.stop_time + self.start_time
        return dis

    # def dist2(self, elev, call):
    #     temp = -1
    #     if src == dest:
    #         return temp
    #     else:
    #         dis = abs(dest - src)
    #         dis *= self.speed
    #         dis += self.close_time + self.open_time + self.stop_time + self.start_time
    #     return dis