from ElevatorCall import ElevatorCall
from Building import Building


def allocate(call: ElevatorCall, building: Building) -> int:
    if len(building.elevators) == 1:
        return building.elevators[0].id

    return 1
