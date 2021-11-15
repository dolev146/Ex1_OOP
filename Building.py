from Elevator import Elevator
from operator import attrgetter


class Building:
    def __init__(self, minFloor: int, maxFloor: int, elevators: list) -> None:
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.size = abs(maxFloor - minFloor)
        self.elevators = []
        self.fast_elev_list = []
        for elevator in elevators:
            elv = Elevator(elevator['_id'],
                           elevator['_speed'],
                           elevator['_minFloor'],
                           elevator['_maxFloor'],
                           elevator['_closeTime'],
                           elevator['_openTime'],
                           elevator['_startTime'],
                           elevator['_stopTime']
                           )
            self.elevators.append(elv)
            if elv.speed >= 5:
                self.fast_elev_list.append(elv)
        self.elev_amount = len(elevators)
        self.fastest_elv = max(elevators, key=lambda elev: elev['_speed'])

    def __str__(self) -> str:
        return (f'minFloor : {self.minFloor}\nmaxFloor : {self.maxFloor},\nelevators : {self.elevators}')
