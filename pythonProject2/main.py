import csv
import json
from calls_for_elevators import calls_for_elevators
from elevator import Elevator
from building import Building
import pandas as pd

if __name__ == '__main__':
    # b1 = Building()
    # b2 = Building()
    # b1.load_json('B1.json')
    # b2.load_json('B2.json')
    # e1 = Elevator(b2.elevators, 1)
    # print(b2.num_of_elevators)
    # print(b2.min_floor)
    # print(b2.elevators[0].get('_speed'))
    # print(e1.speed)
    data = pd.read_csv("Calls_a.csv")
    # call = data[0].__getstate__()
    # print(call)
    print(data)

# rows = []
# call = []
# with open("Calls_a.csv") as f:
#     csv_reader = csv.reader(f)
#     header = next(csv_reader)
#     print("10")
#     for row in len(csv_reader):
#         print("12")
#         call = calls_for_elevators(time=row[0], src=row[1], dest=row[2], type=row[3], allocated_to=row[4])
#         rows.append(row)
#
# print(header)
#
# ile = open("Calls_a.csv", "r")
# csv_reader = csv.reader(f)
# lists_from_csv = []
# for row in csv_reader:
#     lists_from_csv.append(row)
# print(lists_from_csv)
# Each row is a list.separate

# with open('Calls_a.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(
#             f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

# for i in call:
#     i.add()

# new_call = []
# for k in call:
#     new_call.append(k.__dict__.values)
#     file = 'new_call.csv'
#
#
# def load_json(self, file_name):
#     new_b = {}
#     try:
#         with open(file_name, "r") as f:
#             my_b = json.load(f)
#             self._minFloor = my_b["_minFloor"]
#             self._maxFloor = my_b["_maxFloor"]
#             b_d = my_b["_elevators"]
#             for k,v in my_b.items():
#                 print(v)
#                 b = elevator(**v)
#                 b = building(id=v["_id"], speed=["_speed"], min_floor=v["_minFloor"],
#                              max_floor=v["_maxFloor"], close_time=v["_closeTime"],
#                              open_time=v["_openTime"], start_time=v["_startTime"], stop_time=v["_stopTime"])
# new_b[b.id]=b
# self.elevators=new_b
# except IOError as e:
#     print(e)
#
# def __iter__(self):
#     return self.building.elevators.__iter__()

# def __str__(self) -> str:
#     return f"{self.elevators}\n"
