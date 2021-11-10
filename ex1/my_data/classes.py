import csv
import json

"""

this class represent building with elevators

"""


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


class Building:

    def __init__(self, j_file):
        with open(j_file, "r") as file:
            data = json.load(file)
            self.minFloor = data["_minFloor"]
            self._maxFloor = data["_maxFloor"]
            for _elevators in data['_elevators']:
                self._id = _elevators['_id']
                self._speed = _elevators['_speed']
                self.minFloor = _elevators['_minFloor']
                self._maxFloor = _elevators['_maxFloor']
                self._closeTime = _elevators['_closeTime']
                self._openTime = _elevators['_openTime']
                self._startTime = _elevators['_startTime']
                self._stopTime = _elevators['_stopTime']


# reading csv file:
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
