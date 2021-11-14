class Building:
    def __init__(self, minFloor, maxFloor, elevators) -> None:
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = elevators

    def __str__(self) -> str:
        return(f'minFloor : {self.minFloor}\nmaxFloor : {self.maxFloor},\nelevators : {self.elevators}')
