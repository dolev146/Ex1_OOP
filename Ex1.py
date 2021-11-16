import sys
from convertFiles import jsonBuildingToObj, csvToList, writeOutPutFile
from allocate import allocate
# B5.json calls_d.csv output.csv

if __name__ == '__main__':
    # """
    # requiring all the data needed for the program from the files
    # python Ex1.py <Building.json> <Calls.csv> <output.csv> as specified to do.
    # requiring building from its json file callList from csv and the output name
    # and converting to something we can work with in python.
    # """

    # building = jsonBuildingToObj(sys.argv[1])
    # callsList = csvToList(sys.argv[2])
    # allocate(callsList, building.elevators)
    # writeOutPutFile(callsList, sys.argv[3])

    building = jsonBuildingToObj("./Buildings/B1.json")
    callsList = csvToList("./Calls/Calls_a.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B1_a.csv") 

    building = jsonBuildingToObj("./Buildings/B2.json")
    callsList = csvToList("./Calls/Calls_a.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B2_a.csv") 

    # B3 with calls b , c ,d
    building = jsonBuildingToObj("./Buildings/B3.json")
    callsList = csvToList("./Calls/Calls_b.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B3_b.csv") 

    building = jsonBuildingToObj("./Buildings/B3.json")
    callsList = csvToList("./Calls/Calls_c.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B3_c.csv") 

    building = jsonBuildingToObj("./Buildings/B3.json")
    callsList = csvToList("./Calls/Calls_d.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B3_d.csv") 

    # B4 with calls b , c ,d
    building = jsonBuildingToObj("./Buildings/B4.json")
    callsList = csvToList("./Calls/Calls_b.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B4_b.csv") 

    building = jsonBuildingToObj("./Buildings/B4.json")
    callsList = csvToList("./Calls/Calls_c.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B4_c.csv") 

    building = jsonBuildingToObj("./Buildings/B4.json")
    callsList = csvToList("./Calls/Calls_d.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B4_d.csv") 

    # B5 with calls b , c ,d
    building = jsonBuildingToObj("./Buildings/B5.json")
    callsList = csvToList("./Calls/Calls_b.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B5_b.csv") 

    building = jsonBuildingToObj("./Buildings/B5.json")
    callsList = csvToList("./Calls/Calls_c.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B5_c.csv") 

    building = jsonBuildingToObj("./Buildings/B5.json")
    callsList = csvToList("./Calls/Calls_d.csv")
    allocate(callsList, building.elevators)
    writeOutPutFile(callsList, "output_B5_d.csv") 
