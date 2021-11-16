import sys
from convertFiles import jsonBuildingToObj, csvToList, writeOutPutFile
from allocate import allocate


if __name__ == '__main__':
    # """
    # requiring all the data needed for the program from the files
    # python Ex1.py <Building.json> <Calls.csv> <output.csv> as specified to do.
    # requiring building from its json file callList from csv and the output name
    # and converting to something we can work with in python.
    # """

    building = jsonBuildingToObj(sys.argv[1])
    callsList = csvToList(sys.argv[2])
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, sys.argv[3])   # writing the output file
