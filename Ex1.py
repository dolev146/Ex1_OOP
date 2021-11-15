import sys
import json
import csv
import operator
import random
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
                indexOfChosenElevatorToThisCall=int(row[5])
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



# : classes.Call


def allocate(call: ElevatorCall, all_elev: list) -> int:
    # direction = direction_call(call)
    ans = []
    # for index, item in enumerate(items):
    # print(index, item)
    for index, each_elev in enumerate(all_elev):  # iter the elev list and find the best elev to allocate
        if len(each_elev.callList) == 0:
            each_elev.callList.append(call)
            return index

        # if each_elev.len() > 0 && each_elev[-1].dest - each_elev[-1].src  :
    for index, each_elev in enumerate(all_elev):
        if len(each_elev.callList) > 0:
            time_for_dest = each_elev.floorTime * abs(call.destinationOfCall - call.sourceOfCall)
            last_call_time_stamp = each_elev.callList[-1].timeStamp
            fin_time = call.timeStamp - last_call_time_stamp
            if fin_time < time_for_dest:
                ans.append((index, time_for_dest))
    # min([], default="EMPTY")

    rand_index = 0
    if len(ans) == 0:
        elev_indexes_range = len(all_elev) - 1
        rand_index = random.randint(0, elev_indexes_range)
        elev_ = (rand_index , 0)
    else:
        elev_ = min(ans, key=operator.itemgetter(1))
    all_elev[elev_[0]].callList.append(call)
    return elev_[0]


if __name__ == '__main__':
    # requiring all the data needed for the program from the files
    # python Ex1.py <Building.json> <Calls.csv> <output.csv> as specified to do.

    # requiring building from its json file
    building = jsonBuildingToObj(sys.argv[1])
    # requiring calls from its json file
    callsList = csvToList(sys.argv[2])
    # apply algorithm
    for call in callsList:
        chosen_elev = allocate(call, building.elevators)
        call.indexOfChosenElevatorToThisCall = chosen_elev
    # writing the output file
    writeOutPutFile(callsList, sys.argv[3])

# """
# :param manufacturer: The manufacturer of the vehicle.
# :param model: The model of the vehicle .
# :param registration_plate: The registration_plate of the vehicle.
# :param weight: The manufacturer of the vehicle .
# :param max_speed: The max speed  that the vehicle can get.
# """

# self.manufacturer = manufacturer
# self.model = model
# self.registration_plate = registration_plate
# self.weight = weight
# self.max_speed = max_speed
# self.author = "Simon Pikalov"
