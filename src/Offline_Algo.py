import csv
import sys

from numpy import double
from decimal import Decimal
from Elevator import Elevator
from Ex1.src.Building import Building
from CallsForElevator import CallsForElevator


def dist(elev, call, list_of_calls_elevators):  # calculate the time for elevator to take the call
    dis = abs(int(call.dest) - int(call.src))
    dis /= elev.speed
    dis += elev.close_time + elev.open_time + elev.stop_time + elev.start_time

    dis2 = 0
    if len(list_of_calls_elevators) != 0:  # if the list_of_calls_elevators is not empty calculate the time that take to go from the last_call dest to the call.src
        last_call = list_of_calls_elevators[len(list_of_calls_elevators) - 1]
        dis2 = abs(int(last_call.dest) - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    else:  # if the list_of_calls_elevators is empty calculate the time that take to go from 0 floor dest to the call.src
        dis2 = abs(int(call.src) - 0)
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    return dis + elev.time + dis2



def allocate(call_file, building_file):
    list_of_calls_elevators = []
    list_of_elevator = []
    list_of_calls_allocated_to = []
    building = Building()
    building.load_json(building_file)
    num_of_elevators = building.num_of_elevators
    for j in range(num_of_elevators):
        list_of_calls_elevators.append([])
    # create list of the elevators
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
            source = call.src
            dest = call.dest
            min_time = sys.maxsize
            for j in range(num_of_elevators):
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
    # create out.csv
    with open('out.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(new_list_of_calls_allocated_to)


def reader_csv(file_name):
    # list_of_calls = []
    try:
        with open(file_name, "r") as f:
            call_file = csv.reader(f)
            call = list(call_file)
            list_of_calls = []
            for item in call:
                list_of_calls.insert(len(list_of_calls),
                                     CallsForElevator(item[0], item[1], item[2], item[3], item[4], item[5]))

    except IOError as e:
        print(e)

    return list_of_calls
