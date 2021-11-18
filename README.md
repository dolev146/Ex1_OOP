
# Ex1 OOP Ariel University Elevators System Design With Python
## by [Dvir Borochov](https://github.com/dvirbo) and [Dolev Dublon](https://github.com/dolev146)


| ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)     |  ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)|  ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) |
| :---        |    :----:   |          ---: |


**Files**

- Ex1.py
- Building.py
- Elevator.py
- ElevatorCall.py
- allocate.py
- convertFiles.py
- B1.json - B4.json
- Call_a.csv - Calls_d.csv

This project deals with a design of a smart elevator System,
 which receives all the required input calls in advance,
 and should allocate an elevator for a call in the most
 optimal way, so that the average waiting time will be minimal.
 the input that we get is:

- json file that contain data about the building and the elevators.
- csv file that contain data about the calls that the elevators going to recived.




## Planning && Execution (work process)

We were asked in this task, to write a program in Python that
 processes information and emits a new csv file where each call
  is acllocated to an elevator,
 so that the total wait time will be the lowest.
The software gets a file with information about the building in
 json format and a file with information about the calls in csv
  format(**Off-Line Algorithm**) and emits a csv file,
   at the beginning of the task Dvir and I were not partners 
   and after a week we decided to become partners.
    That is why our literary review is different. At
     first we did a brainstorm, and came up with a lot 
     of good ideas, we tried to implement an algorithm based
      on the shortest time of an elevator to get to the call
       received, but we quickly found it very complex, 
       we feel that maybe with a little more knowledge in Python
        we would succeed to calculate the timestamp and to take
         the exact elevator location,but after many attempts,
          writing and deleting, which can be seen in commits and
           in our branches, the code became very cumbersome and
            impossible Understand , we decided to Keep It Simple, 
Finally, we decided to produce a preference-based algorithm,
 meaning it prioritizes the fast elevators over the slower ones
  so that relatively fast elevators get more calls.

things to take to consideration
Each building has a minimum and maximum floor and the number of elevators is known
 Each elevator has characteristics of stop time, movement start time, and speed (how many seconds does it take to move to the floor).
The user has to tap the destination floor outside the elevators and then the system has to insert (assign) a specific elevator that is set for it and stop at the destination floor.
The system will want to install the elevator that will reduce the arrival time to a minimum (the arrival time is set to be the time in seconds between the call to the elevator and the arrival to the destination floor)
Given a collection of calls for lifts in time we would like to define an elevator placement strategy for calls that will minimize the total arrival time for all calls.
Residential floors is 1 and up
Entrance or exit floors to this building are 0 and below
And there is no limit to the amount of people per elevator.
## Bibliography

We used the links below to understand the problem in depth and formulate an algorithm that will lead to optimal performance.
 - [studylib](https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...)
 - [thinksoftware](https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c)



## UML 
the uml from out first assignment helped understanding how to build our code.
![UML](https://user-images.githubusercontent.com/62290677/142478335-138fa53b-ea16-418f-b1d8-1177a92a08a3.png)926-8ac89962-1e82-462f-84ef-4c57f816919d.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/dvirbo/Ex1_OOP.git  
```

Go to the project directory

```bash
  cd Ex1_OOP
```

Run

```bash
  python Ex1.py B1.json Calls_a.csv output.csv
```
or on linux / mac

```bash
python3 Ex1.py B1.json Calls_a.csv output.csv
```





## Content of Files

- Building: contain info about minFloor & maxFloor, and a list of elevators.
- Elevator: info about the parameters of the building. contain- speed, minFloor, close & open Time, start & stop Time, status: up/down or level.
- ElevatorCall: info about each call that will help us to assign the call. contain: index of the Chosen Elev,timeStamp of the call,source & destination of the Call and the direction of the call- up/down.
- convertFiles: contain 3 functions: jsonBuildingToObj: convert json file that contain the data about the elevator and the building to objects of building & elevator. csvToList: convert csv file that contain the info about the calls that we get and make list of calls from the data. writeOutPutFile: write the elevators that we allocate To the right column un the csv file.


## Screenshots
this is how we tried to understand how to choose with prefered answer in python by using 
[Google Collab](https://colab.research.google.com/drive/1dkSnW-NIoo4lqPexWkW0YivdMyRu777n?usp=sharing)
![image](https://user-images.githubusercontent.com/73783656/142256429-9cf944d9-35ff-4a83-adb4-d0c1b01cf454.png)

## Screenshots of our tests

![image](https://user-images.githubusercontent.com/73783656/142257606-1ff49e09-6958-464a-8aa1-b4a7619452c7.png)
![image](https://user-images.githubusercontent.com/73783656/142257377-a79d6ab2-73cc-4b7a-ac7a-eaba452323a4.png)
In the Screenshots above we tried to change the algorithm based on the average time of floor transition for each elevator.

 ![image](https://user-images.githubusercontent.com/62290677/142257395-ef2f77ce-8f80-451d-bf66-ecc619fad5d4.png)
 ![image](https://user-images.githubusercontent.com/62290677/142257562-40a00e03-f9fb-404c-b1aa-2f0ab0c4c412.png)
finally, we decided to use an algorithm that favors speed.
 ![image](https://user-images.githubusercontent.com/62290677/142257788-c5ca8601-89b5-4b1f-a635-8f1962c97417.png)
 this table shows the different between the two methods that we examine

[link to the java simulator repo](https://github.com/dolev146/JavaSimulatorPythonElevatorOOP)


## Unit test
 We checked that indeed the amount of shows of the high-speed elevator appears more:
![image](https://user-images.githubusercontent.com/73783656/142267727-b0f2238c-dfa4-4bfc-9810-510b07d3ef21.png)



# Files

### Ex1.py

``` import sys
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
    writeOutPutFile(callsList, sys.argv[3])
```

## Elevator.py

```
class Elevator:
    def __init__(self, id: int,
                 speed: float,
                 minFloor: int,
                 maxFloor: int,
                 closeTime: float,
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

```

## ElevatorCall.py

```
class ElevatorCall:
    def __init__(self,
                 strElevatorCall: str,
                 timeStamp: float,
                 sourceOfCall: int,
                 destinationOfCall: int,
                 stateOfElevator: int,
                 idChosenElev: int) -> None:
        self.strElevatorCall = strElevatorCall
        self.timeStamp = timeStamp
        self.sourceOfCall = sourceOfCall
        self.destinationOfCall = destinationOfCall
        self.stateOfElevator = stateOfElevator
        self.idChosenElev = idChosenElev

```

## convertFiles.py

```
import json
import csv
from Building import Building
from ElevatorCall import ElevatorCall
# from pathlib import Path
# data_folder = Path("./Outputs")


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
    # file_to_open = data_folder / outPutName
    newCallList = []
    for call in csvList:
        newCallList.append(call.__dict__.values())
    with open(outPutName, 'w', newline="") as outPutFile:
        csvWriter = csv.writer(outPutFile)
        csvWriter.writerows(newCallList)

```
### Building.py 

```
from Elevator import Elevator


class Building:
    def __init__(self, minFloor: int, maxFloor: int, elevators: list) -> None:
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = []
        for elevator in elevators:
            elv = Elevator(elevator['_id'],
                           elevator['_speed'],
                           elevator['_minFloor'],
                           elevator['_maxFloor'],
                           elevator['_closeTime'],
                           elevator['_openTime'],
                           elevator['_startTime'],
                           elevator['_stopTime']
                           )
            self.elevators.append(elv)


```