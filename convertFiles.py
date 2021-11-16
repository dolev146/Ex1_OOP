import json
import csv
from Building import Building
from ElevatorCall import ElevatorCall


def jsonBuildingToObj(jsonBuilding: str):
    """
    Traversy Media pyhton crash course
    https://youtu.be/JJmcL1N2KQs startig from 1:26:17 he starts talking about working with files
    :param callFile:
    :return: calls tyoe : list
    """
    try:
        file = open(jsonBuilding, "r+")
        buildingDict = json.load(file)
        file.close()
        return Building(buildingDict['_minFloor'], buildingDict['_maxFloor'], buildingDict['_elevators'])
        # for some reason spread operator not working: return Building(**buildingDict)

    except IOError as e:
        print(e)


def csvToList(callFile: str):
    """
    acording to amichai in his youTube video
    https://www.youtube.com/watch?v=AgzaJpptbHE&ab_channel=CoreySchafer
    we also watched Traversy Media pyhton crash course
    https://youtu.be/JJmcL1N2KQs startig from 1:26:17 he starts talking about working with files
    :param callFile:
    :return: calls tyoe : list
    """
    try:
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
    except IOError as e:
        print(e)


def writeOutPutFile(csvList: list, outPutName: str):
    """
    acording to amichai in his youTube video
    https://www.youtube.com/watch?v=AgzaJpptbHE&ab_channel=CoreySchafer starting from minute 18:40
    there is a spesific way to write, we need to use the __dict__ method in order to be able to
    write the calls back to the csv file, so we worked according to the instructions.
    :param csvList:
    :param outPutName:
    :return: void
    """
    newCallList = []
    for call in csvList:
        newCallList.append(call.__dict__.values())
    with open(outPutName, 'w', newline="") as outPutFile:
        csvWriter = csv.writer(outPutFile)
        csvWriter.writerows(newCallList)
