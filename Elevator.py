class Elevator:
    def __init__(self, id: int, speed: float, minFloor: int, maxFloor: int, closeTime: float,
                 openTime: float,
                 startTime: float,
                 stopTime: float) -> None:
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.stopTime = stopTime
        self.startTime = startTime
        self.position = 0

        # self.floorTime = 1 / speed + closeTime + openTime + startTime + stopTime    
        # self.callList = []
        # def calcTimeToDest(self, src, dest) -> float:
        #     print(self.floorTime)
        #     print(src)
        #     print(dest)
        #     return 1
