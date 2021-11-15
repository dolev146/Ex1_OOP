import sys
from allocate import allocate
from convertFiles import jsonBuildingToObj,csvToList,writeOutPutFile
from allocate import allocate

if __name__ == '__main__':
    # requiring all the data needed for the program from the files
    # python Ex1.py <Building.json> <Calls.csv> <output.csv> as specified to do.
    # requiring building from its json file
    building = jsonBuildingToObj(sys.argv[1])
    # requiring calls from its json file
    callsList = csvToList(sys.argv[2])
    # apply algorithm
    for call in callsList:
        chosen_elev = allocate(call, building)
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
