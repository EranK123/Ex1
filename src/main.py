import sys
from OfflineAlgo import allocate
import os

cases = [("B1", "a"), ("B2", "a"), ("B3", "a"), ("B3", "b"), ("B3", "c"), ("B3", "d"),
         ("B4", "a"), ("B4", "b"), ("B4", "c"), ("B4", "d"), ("B5", "a"), ("B5", "b"),
         ("B5", "c"), ("B5", "d")]


def make_all():
    for building, case in cases:
        sys.argv[1] = f"{building}.json"
        sys.argv[2] = f"Calls_{case}.csv"
        sys.argv[3] = f"out_{building}_Calls_{case}.csv"
        main()


def score():
    building_num = input("Enter building number: ")
    case = input("Enter case: ")

    building = f"B{building_num}.json"
    case_file = f"out/out_B{building_num}_Calls_{case}.csv"
    log_file = f"log_B{building_num}_Calls_{case}.log"
    tester = "/Users/erankatz/PycharmProjects/Ex1/ex1/src/Ex1_checker_V1.2_obf.jar"
    command = f"java -jar {tester} 212727283,315907113 {building} {case_file} {log_file}"
    os.system(command)


def main():
    building = sys.argv[1]
    calls = sys.argv[2]
    output = sys.argv[3]
    print(building, calls, output)
    allocate(calls, building, output)


if __name__ == '__main__':
    main()
