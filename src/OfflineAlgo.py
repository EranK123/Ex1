import csv
import sys

from Elevator import Elevator
from Building import Building
from CallsForElevator import CallsForElevator

"""
-------------------------------------------------
This function will calculate the time it takes for an elevator to go from floor a to floor b.
Returns the time from destination floor to source floor for the current call + last destination call floor 
to current source floor.
------------------------------------------------
"""


def dist(elev, call, list_of_calls_elevators):  # calculate the time for elevator to go from source floor to
    # destination floor
    dis = abs(int(call.dest) - int(call.src))
    dis /= elev.speed
    dis += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    dis2 = 0
    if len(list_of_calls_elevators) != 0:  # if the list_of_calls_elevators is not empty calculate the time that take
        # to go from the last_call destination to the current call source
        last_call = list_of_calls_elevators[len(list_of_calls_elevators) - 1]
        dis2 = abs(int(last_call.dest) - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    else:  # if the list_of_calls_elevators is empty calculate the time that take to go from 0 floor dest to the
        # current call source
        dis2 = abs(int(call.src) - 0)
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
    return dis + elev.time + dis2


"""
-------------------------------------------------
This function allocates the best elevator for the current floor based on it's time.
-------------------------------------------------
"""


def allocate(call_file, building_file, out_file):
    list_of_calls_elevators = []  # each elevator will have the calls allocated to the elevator
    list_of_elevator = []  # list represents the elevators
    list_of_calls_allocated_to = []  # list of the calls we are allocating
    building = Building()
    building.load_json(building_file)  # getting the building parameters
    num_of_elevators = building.num_of_elevators
    for j in range(num_of_elevators):
        list_of_calls_elevators.append([])
    for j in range(num_of_elevators):  # create list of the elevators
        elevator = Elevator(building.elevators, j)
        list_of_elevator.insert(j, elevator)

    elev_index = -1
    calls_list = reader_csv(call_file)  # getting the call parameters
    if num_of_elevators == 1:  # in case we have 1 elevator we allocate this elevator
        for call in calls_list:
            call.allocated_to = 0
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)
    else:
        for call in calls_list:
            min_time = sys.maxsize  # set minimum time to max size so we can do comparisons
            for j in range(num_of_elevators):
                elevator = list_of_elevator[j]
                elev_time = dist(elevator, call, list_of_calls_elevators[j])  # calculate the time using dist function
                if elev_time < min_time:
                    min_time = elev_time
                    elev_index = j
            call.allocated_to = elev_index  # allocating to the elevator with the minimum time
            list_of_elevator[elev_index].time = min_time  # updating the time
            list_of_calls_elevators[elev_index].insert(len(list_of_calls_elevators[elev_index]), call)  # add the call
            # to the elevator call list in the last position
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)  # add the call to the allocated
            # calls list in last position

    new_list_of_calls_allocated_to = []
    for item in list_of_calls_allocated_to:
        new_list_of_calls_allocated_to.append(item.__dict__.values())  # getting call values

    with open(out_file, 'w', newline='') as myfile:  # create out
        wr = csv.writer(myfile)
        wr.writerows(new_list_of_calls_allocated_to)


""""
This function reads the csv file for a call.
"""


def reader_csv(file_name):
    try:
        list_of_calls = []
        with open(file_name, "r") as f:
            call_file = csv.reader(f)
            call = list(call_file)
            for item in call:
                list_of_calls.insert(len(list_of_calls),
                                     CallsForElevator(item[0], item[1], item[2], item[3], item[4], item[5]))

    except IOError as e:
        print(e)

    return list_of_calls
