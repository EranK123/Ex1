import csv
import pandas as pd


class calls_for_elevators:

    def __init__(self, index_of_calls, index_of_get_something_from_the_call):
        self.calls = [][]
        self.index_of_calls = index_of_calls
        self.index_of_get_something_from_the_call = index_of_get_something_from_the_call
        self.time = 0
        self.src = 0
        self.dest = 0
        self.type = 0
        self.allocated_to = 0

    def load_csv(self, file_name):

        try:
            with open(file_name, "r") as f:
                call = csv.load(f)
                self.time = call[self.index_of_calls]["time"]
                self.src = call[self.index_of_calls]["src"]
                self.dest = call[self.index_of_calls]["dest"]
                self.type = call[self.index_of_calls]["type"]
        except IOError as e:
            print(e)


    # def __init__(self, time, src, dest, type, allocated_to):
    #     self.time = time
    #     self.src = src
    #     self.dest = dest
    #     self.type = type
    #     self.allocated_to = allocated_to

    def __str__(self):
        return f"time: {self.time} src: {self.src} dest: {self.dest} type: {self.type} allocated_to: {self.allocated_to}"

