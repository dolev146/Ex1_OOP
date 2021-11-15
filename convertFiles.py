import json
import csv
from Building import Building
from ElevatorCall import ElevatorCall


def jsonBuildingToObj(jsonBuilding: str):
    try:
        file = open(jsonBuilding, "r+")
        buildingDict = json.load(file)
        file.close()
        return Building(buildingDict['_minFloor'], buildingDict['_maxFloor'], buildingDict['_elevators'])
        # for some reason spread operator not working: return Building(**buildingDict)

    except IOError as e:
        print(e)


def csvToList(callFile: str):
    calls = []
    with open(callFile) as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            elevatorCall = ElevatorCall(
                strElevatorCall=str(row[0]),
                timeStamp=float(row[1]),
                sourceOfCall=int(row[2]),
                destinationOfCall=int(row[3]),
                stateOfElevator=int(row[4]),
                idChosenElev=int(row[5])
            )
            calls.append(elevatorCall)
        return calls


def writeOutPutFile(csvList: list, outPutName: str):
    newCallList = []
    for call in csvList:
        newCallList.append(call.__dict__.values())
    with open(outPutName, 'w', newline="") as outPutFile:
        csvWriter = csv.writer(outPutFile)
        csvWriter.writerows(newCallList)
