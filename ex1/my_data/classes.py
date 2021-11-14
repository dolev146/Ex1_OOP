import csv
import json
import sys

"""

this class represent building with elevators

"""
'''
class Elevators:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
'''


class Building:

    def __init__(self, j_file):
        with open(j_file, "r") as file:
            data = json.load(file)
            self.minFloor = data["_minFloor"]
            self.maxFloor = data["_maxFloor"]
            for _elevators in data['_elevators']:
                self.id = _elevators['_id']
                self.speed = _elevators['_speed']
                self.minFloor = _elevators['_minFloor']
                self.maxFloor = _elevators['_maxFloor']
                self.closeTime = _elevators['_closeTime']
                self.openTime = _elevators['_openTime']
                self.startTime = _elevators['_startTime']
                self.stopTime = _elevators['_stopTime']

                # class Building:
                #     def __init__(self, minFloor, maxFloor, elevators) -> None:
                #         self.minFloor = minFloor
                #         self.maxFloor = maxFloor
                #         self.elevators = elevators
                #
                #     def __str__(self) -> str:
                #         return (
                #             f'minFloor : {self.minFloor}\nmaxFloor : {self.maxFloor},\nelevators : {self.elevators}')

    # this function return the sum of the elev that in the list


"""
this class represent a call for the elevator that 
return : the time of the call, src and dest floor

"""


class Call:

    def __init__(self, f_csv, num_call):
        with open(f_csv) as file:
            reader = csv.reader(file, delimiter=',')
            cur_line = 1
            for row in reader:
                if cur_line == num_call:
                    self.time = row[1]
                    self.sre = row[2]
                    self.dest = row[3]
                    break
                else:
                    cur_line += 1


sys.argv = []
Buildings = list[1]
calls = list[2]
output = list[3]
print(list)
