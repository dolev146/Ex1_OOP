import json

'''
this class represent building with elevators

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


class Building(Elevators):
    def __init__(self, minFloor, maxFloor, elevators):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevators = [{elevators}]
