import csv
import sys

from Elevator import Elevator
from Building import Building
from CallsForElevator import CallsForElevator


def dist(elev, call, list_of_calls_elevators):
    dis = abs(int(call.dest) - int(call.src))
    dis /= elev.speed
    dis += elev.close_time + elev.open_time + elev.stop_time + elev.start_time

    if len(list_of_calls_elevators) != 0:
        last_call = list_of_calls_elevators[len(list_of_calls_elevators) - 1]
        dis2 = abs(int(last_call.dest) - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    else:
        dis2 = abs(0 - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    return dis + dis2 + elev.time


def allocate(call_file, building_file):
    list_of_calls_elevators = []
    list_of_elevator = []
    list_of_calls_allocated_to = []
    building = Building()
    building.load_json(building_file)
    num_of_elevators = building.num_of_elevators
    for j in range(num_of_elevators):
        list_of_calls_elevators.append([])
    for j in range(num_of_elevators):
        elevator = Elevator(building.elevators, j)
        list_of_elevator.insert(j, elevator)

    elev_index = -1
    calls_list = reader_csv(call_file)
    if num_of_elevators == 1:
        for call in calls_list:
            call.allocated_to = 0
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)
    else:
        for call in calls_list:
            min_time = sys.maxsize
            for j in range(building.num_of_elevators):
                elevator = list_of_elevator[j]
                elev_time = dist(elevator, call, list_of_calls_elevators[j])
                if elev_time < min_time:
                    min_time = elev_time
                    elev_index = j

            call.allocated_to = elev_index
            list_of_elevator[elev_index].time = min_time
            list_of_calls_elevators[elev_index].insert(len(list_of_calls_elevators[elev_index]), call)
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)
    new_list_of_calls_allocated_to = []
    for item in list_of_calls_allocated_to:
        new_list_of_calls_allocated_to.append(item.__dict__.values())
    print(new_list_of_calls_allocated_to)
    with open('out.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(new_list_of_calls_allocated_to)


def reader_csv(file_name):
    list_of_calls = []
    try:
        with open(file_name, "r") as f:
            call_file = csv.reader(f)
            call = list(call_file)
            for item in call:
                list_of_calls.insert(len(list_of_calls),
                                     CallsForElevator(item[0], item[1], item[2], item[3], item[4], item[5]))

    except IOError as e:
        print(e)

    return list_of_calls
