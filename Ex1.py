import sys
import json
import csv
from Building import Building
from ElevatorCall import ElevatorCall
import pandas as pd


def jsonBuildingToObj(jsonBuilding:str):
    try:
        file = open(jsonBuilding, "r+")
        buildingDict = json.load(file)
        file.close()
        return Building(buildingDict['_minFloor'], buildingDict['_maxFloor'], buildingDict['_elevators'])
        # for some reason spread operator not working: return Building(**buildingDict)

    except IOError as e:
        print(e)


def csvToList(callFile:str):
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
                indexOfChosenElevatorToThisCall=int(row[5])
            )
            calls.append(elevatorCall)
        return calls


def writeOutPutFile(csvList:list, outPutName:str):
    newCallList = []
    for call in csvList:
        newCallList.append(call.__dict__.values())
    with open(outPutName, 'w', newline="") as outPutFile:
        csvWriter = csv.writer(outPutFile)
        csvWriter.writerows(newCallList)
    outPutFile.close()


def applyAlgo(callList:list):
    for call in callsList:
        call.indexOfChosenElevatorToThisCall = 0
    return callList


if __name__ == '__main__':
    # requiring all the data needed for the program from the files
    # python Ex1.py <Building.json> <Calls.csv> <output.csv> as specified to do.

    # requiring building from its json file
    building = jsonBuildingToObj(sys.argv[1])
    # requiring calls from its json file
    callsList = csvToList(sys.argv[2])
    # apply algorithm
    newCallList = applyAlgo(callsList)
    # writing the output file
    writeOutPutFile(newCallList, sys.argv[3])
    print(pd.read_csv(sys.argv[3]))
    print(pd.read_csv(sys.argv[2]))
    # 
