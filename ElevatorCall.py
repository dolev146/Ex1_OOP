class ElevatorCall:
    def __init__(self, strElevatorCall:str, timeStamp:float, sourceOfCall:int, destinationOfCall:int, stateOfElevator:int,
                 indexOfChosenElevatorToThisCall:int) -> None:
        self.strElevatorCall = strElevatorCall
        self.timeStamp = timeStamp
        self.sourceOfCall = sourceOfCall
        self.destinationOfCall = destinationOfCall
        self.stateOfElevator = stateOfElevator
        self.indexOfChosenElevatorToThisCall = indexOfChosenElevatorToThisCall

    def __str__(self) -> str:
        return f'''ElevatorCall : {self.strElevatorCall},timeStamp : {self.timeStamp} 
sourceOfCall : {self.sourceOfCall},destinationOfCall : {self.destinationOfCall}
stateOfElevator : {self.stateOfElevator},indexOfChosenElevatorToThisCall : {self.indexOfChosenElevatorToThisCall}'''

    def __repr__(self) -> str:
        return f'''ElevatorCall : {self.strElevatorCall},timeStamp : {self.timeStamp}
sourceOfCall : {self.sourceOfCall},destinationOfCall : {self.destinationOfCall}
stateOfElevator : {self.stateOfElevator},indexOfChosenElevatorToThisCall : {self.indexOfChosenElevatorToThisCall}'''
