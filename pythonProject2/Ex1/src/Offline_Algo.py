import csv
import sys

from Elevator import Elevator
from Ex1.src.Building import Building
from CallsForElevator import CallsForElevator

def dist(elev, call, list_of_calls_elevators):
    dis = abs(int(call.dest) - int(call.src))
    dis /= elev.speed
    dis += elev.close_time + elev.open_time + elev.stop_time + elev.start_time

    dis2 = 0
    if len(list_of_calls_elevators) != 0:
        last_call = list_of_calls_elevators[len(list_of_calls_elevators) - 1]
        dis2 = abs(int(last_call.dest) - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
        # dis2 = abs(dis2 - last_call.time)
    else:
        dis2 = abs(0 - int(call.src))
        dis2 /= elev.speed
        dis2 += elev.close_time + elev.open_time + elev.stop_time + elev.start_time
        # dis2 = abs(dis2 - last_call.time)
    # if call.src < call.dest:
    #     state = 1
    # elif call.src > call.dest:
    #     state = -1
    # dist3 = 0
    # if elev.state == state or elev.state == 0:
    #     dist3 = -1
    return dis+dis2+elev.time


def allocate(call_file, building_file):
    list_of_calls_elevators = []
    list_of_elevator = []
    list_of_calls_allocated_to = []
    building = Building()
    building.load_json(building_file)
    num_of_elevators = building.num_of_elevators
    # time_of_the_elevator = {}
    for j in range(num_of_elevators):
        list_of_calls_elevators.append([])
    # create list of the elevators
    for j in range(num_of_elevators):
        elevator = Elevator(building.elevators, j)
        list_of_elevator.insert(j, elevator)
    # max_speed = -1

    elev_index = -1
    calls_list = reader_csv(call_file)
    if num_of_elevators == 1:
        for call in calls_list:
            call.allocated_to = 0
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)
    else:
        i = 0
        for call in calls_list:
            min_time = sys.maxsize
            # source = call.src
            # dest = call.dest
            # time = call.time
            # elevator = list_of_elevator[0] # initial val
            # if i == 0:
            #     for j in range(num_of_elevators):
            #         elevator = list_of_elevator[j]
            #         speed = elevator.speed
            #         if speed > max_speed:
            #             max_speed = speed
            #             elev_index = elevator.id
            #         # elevator.pos = source
            #     call.allocated_to = elev_index
            #     # elevator.pos = call.src
            #     elevator.time +=
            #     list_of_calls_elevators[elev_index].insert(len(list_of_calls_elevators[elev_index]), call)
            #     list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)
                # if source < dest:
                #     elevator.state = 1
                # elif source > dest:
                #     elevator.state = -1
                # next call
                #i > 0
                # elevator = list_of_elevator[0]
                # if source < dest:
                #     state_call = 1
                # elif source > dest:
                #     state_call = -1
            for j in range(building.num_of_elevators):
                elevator = list_of_elevator[j]
                elev_time = dist(elevator, call, list_of_calls_elevators[j])
                print('time befor: {} elev time of {} : {}'.format(elevator.time,j,elev_time))
                if elev_time < min_time:
                    print('min_time: {} elev_time : {}'.format(min_time,elev_time))
                    min_time = elev_time
                    elev_index = j

            call.allocated_to = elev_index
            # elevator.pos = call.src
            list_of_elevator[elev_index].time = min_time
            list_of_calls_elevators[elev_index].insert(len(list_of_calls_elevators[elev_index]),call)
            # new_list = call.stri
            # new_list.insert(6,str(call.allocated_to))
            # list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), new_list)
            list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to), call)

                # list_of_calls_allocated_to.insert(len(list_of_calls_allocated_to),call.stri + "," + str(call.allocated_to)+"\n")
                # if source < dest:
                #     elevator.state = 1
                # elif source > dest:
                #     elevator.state = -1
            i = i+1
    # print(list_of_calls_allocated_to)
    new_list_of_calls_allocated_to = []
    for item in list_of_calls_allocated_to:
        new_list_of_calls_allocated_to.append(item.__dict__.values())
    print(new_list_of_calls_allocated_to)
    # create out.csv
    with open('out.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(new_list_of_calls_allocated_to)


def reader_csv(file_name):
    list_of_calls = []
    try:
        with open(file_name, "r") as f:
            call_file = csv.reader(f)
            call = list(call_file)
            # list_of_calls = []
            # self.stri = call[self.index_of_calls]
            # self.stri.pop()
            for item in call:
                list_of_calls.insert(len(list_of_calls), CallsForElevator(item[0],item[1], item[2], item[3] ,item[4], item[5]))

            # self.stri = "Elevator call," + str(self.time) +"," + str(self.src) +"," + str(self.dest) + "," + str(self.type)
    except IOError as e:
        print(e)

    return list_of_calls