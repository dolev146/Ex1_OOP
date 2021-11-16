# Ex1_OOP - offline algorithem
## This is the second task in OOP course (Object Oriented Programming & Design. - Ariel University)
  This project deals with a design of a smart elevator, which receives all the required input in advance, and should incorporate elevators for call in the most optimal way,       so that the average waiting time will be minimal.
  the input that we get is:
- json file that contain data about the building and the Features of elevator.
- csv file that contain data about the calls that the elevators going to recived.

 

  ## bibliography:
  We used the links below to understand the problem in depth and formulate an algorithm that will lead to optimal performance.
  - [studylib] - On-line Algorithms versus Off-line Algorithms for the Elevator Scheduling Problem
  - [thinksoftware] - Elevator System Design 

# python files:
- Building: contain info about minFloor & maxFloor, and a list of elevators.
- Elevator: info about the parameters of the building. contain- speed, minFloor, close & open Time, start & stop Time, status: up/down or level.
- ElevatorCall: info about each call that will help us to assign the call. 
  contain: index of the Chosen Elev,timeStamp of the call,source & destination of the Call and the direction of the call- up/down.
- convertFiles: contain 3 functions:
 jsonBuildingToObj: convert json file that contain the data about the elevator and the building to objects of building & elevator.
 csvToList: convert csv file that contain the info about the calls that we get and make list of calls from the data.
 writeOutPutFile: write the elevators that we allocate To the right column un the csv file.



# algo description:
  first, convert the data from the json to objects.\
  insert all the calls that in the csv file to list that represent the calls by over every row in the csv file.\
  check how much elevator is in the json file.\
  make number of list that represent the number of the elevators that in the json file .\
  if there is only one elevator - put 0 in all the collum that in the csv file.\
  else -
  we allocate the calls by the fastest elevator per floor,e.i we calculate the data abour all the elevators that we have and Assigned by the weights of them.
  So an elevator that is faster than the other elevators will handle the more calls and bring us a low average waiting time.\
  by that iter all the calls that in the list and allocate the calls by te above description.
  when finish -insert the assignees of the calls to the csv file.\
  at the end return the csv file.
  

  
  [//]:#
  [studylib]: https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...
  [thinksoftware]:  https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c
