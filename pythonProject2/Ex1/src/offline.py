import csv
import sys

from CallsForElevator import CallsForElevator
from Elevator import Elevator
from Building import Building


def allocate(call_file, building_file):
    time = 0
    elevs_times = []
    list_of_calls_allocated_to = []
    elev_index = -1
    min_time = sys.maxsize
    building = Building()
    building.load_json(building_file)
    calls_list = call_file.reader_csv(call_file)
    for call in calls_list:
        # call = CallsForElevator(i)
        source = call.src
        dest = call.dest

        for j in building.num_of_elevators:
            elevator = Elevator(building.elevators, j)
            time = elevator.close_time + elevator.start_time + elevator.stop_time + elevator.open_time \
                   + abs(dest - source) / elevator.speed
            if time < min_time:
                min_time = time
                elev_index = elevator.id
        elevs_times[elev_index] += min_time
        # elevs_times.sort()
        call.allocated_to = elev_index
        list_of_calls_allocated_to

        new_list_of_calls_allocated_to = []
        for item in list_of_calls_allocated_to:
            new_list_of_calls_allocated_to.append(item.__dict__.values())
        print(new_list_of_calls_allocated_to)
        # create out.csv
        with open('out.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(new_list_of_calls_allocated_to)


def reader_csv(file_name):
    try:
        with open(file_name, "r") as f:
            call_file = csv.reader(f)
            call = list(call_file)
            list_of_calls = []
            # self.stri = call[self.index_of_calls]
            # self.stri.pop()
            for item in call:
                list_of_calls.insert(len(list_of_calls),
                                     CallsForElevator(item[0], item[1], item[2], item[3], item[4], item[5]))

            # self.stri = "Elevator call," + str(self.time) +"," + str(self.src) +"," + str(self.dest) + "," + str(self.type)
    except IOError as e:
        print(e)

    return list_of_calls