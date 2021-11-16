import csv

from pip._internal.cli.cmdoptions import src


class CallsForElevator:

    def __init__(self, name, time, src, dest, type, allocated_to):
        # self.calls = []
        # self.index_of_calls = str(index_call)
        self.name = name
        self.time = time
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = allocated_to
        # self.stri = ""

    # def reader_csv(self, file_name):
    #
    #     try:
    #         with open(file_name, "r") as f:
    #             call_file = csv.reader(f)
    #             call = list(call_file)
    #             # self.stri = call[self.index_of_calls]
    #             # self.stri.pop()
    #             self.time = call[int(self.index_of_calls)][1]
    #             self.src = call[int(self.index_of_calls)][2]
    #             self.dest = call[int(self.index_of_calls)][3]
    #             self.type = call[int(self.index_of_calls)][4]
    #             self.allocated_to = call[int(self.index_of_calls)][5]
    #             # self.stri = "Elevator call," + str(self.time) +"," + str(self.src) +"," + str(self.dest) + "," + str(self.type)
    #     except IOError as e:
    #         print(e)

    def __str__(self):
        return f"time: {self.time} src: {self.src} dest: {self.dest} type: {self.type} allocated_to: {self.allocated_to}"

