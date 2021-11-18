import json
from Elevator import Elevator


class Building:

    def __init__(self):
        self.elevators = []
        self.min_floor = 0
        self.max_floor = 0
        self.num_of_elevators = 0

    # def get_elev(self, index):
    #     elevator = Elevator(index)
    #     return elevator

    def load_json(self, file_name):
        # build = {}
        try:
            with open(file_name, "r") as f:
                build = json.load(f)
                self.min_floor = build["_minFloor"]
                self.max_floor = build["_maxFloor"]
                self.num_of_elevators = len(build["_elevators"])
                self.elevators = build["_elevators"]

        except IOError as e:
            print(e)

    def __str__(self) -> str:
        return f"{self.elevators}\n"
