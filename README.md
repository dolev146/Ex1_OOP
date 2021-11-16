# Ex1_OOP
 ## This project deals with the design of a smart elevator, which receives all the required input in advance, and should incorporate elevators for call in the most optimal way, so that the average waiting time will be minimal. 
 

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
  check how much elevator is in the json file.\
  make number of list that represent the number of the elevators that in the json file.\
  id (method that every elev have) = the place of the elev in the list.\
  insert all the calls that in the csv file to list that represent the calls by over every row in the csv file.\
  insert dict (to each of the list) that contain the finish time of the last call in the current list.\
  if there is only one elevator - put 0 in all the collum that in the csv file.\
  else -( iter the list of the calls by compute the start time of the call and the by the dict of the list- insert the call to the shortest )
  by that iter all the calls that in the list
  when finish -insert the assignees of the calls to the csv file.\
  at the end return the csv file.
  

  
  [//]:#
  [studylib]: https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...
  [thinksoftware]:  https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c
