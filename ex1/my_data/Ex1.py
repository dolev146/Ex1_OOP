import json


''' 
Ex1 <Building.json> <Calls.csv> <output.csv>
'''


class Ex1:

    def __init__(self):
        self.load_json()

    def load_json(self, j_file):
        with open(j_file, "r") as file:
            data = json.load(file)
            self._minFloor = data["_minFloor"]
            self._maxFloor = data["_maxFloor"]
            for _elevators in data['_elevators']:
                self._id = _elevators['_id']
                self._speed = _elevators['_speed']
                self._minFloor = _elevators['_minFloor']
                self._maxFloor = _elevators['_maxFloor']
                self._closeTime = _elevators['_closeTime']
                self._openTime = _elevators['_openTime']
                self._startTime = _elevators['_startTime']
                self._stopTime = _elevators['_stopTime']
