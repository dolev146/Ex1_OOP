
# Ex1 OOP Ariel University Elevators System Design With Python
## by [Dvir Borochov](https://github.com/dvirbo) and [Dolev Dublon](https://github.com/dolev146)

**Files**

- Ex1.py
- Building.py
- Elevator.py
- ElevatorCall.py
- allocate.py
- convertFiles.py
- .gitignore
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
 - [UML chart](https://lucid.app/lucidchart/445effd6-f902-4f9e-96e1-666f7d6a955b/edit?view_items=nGpmtm1QpyO3&invitationId=inv_f7e0b4b2-6c3e-4bd0-ab49-4eb8e0be02b5)


## UML && Google Collab
the uml from out first assignment helped understanding how to build our code.
![Uml](https://user-images.githubusercontent.com/62290677/142245926-8ac89962-1e82-462f-84ef-4c57f816919d.png)


| ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)     |  ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)|  ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) |
| :---        |    :----:   |          ---: |


 

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




## Content of Files

- Building: contain info about minFloor & maxFloor, and a list of elevators.
- Elevator: info about the parameters of the building. contain- speed, minFloor, close & open Time, start & stop Time, status: up/down or level.
- ElevatorCall: info about each call that will help us to assign the call. contain: index of the Chosen Elev,timeStamp of the call,source & destination of the Call and the direction of the call- up/down.
- convertFiles: contain 3 functions: jsonBuildingToObj: convert json file that contain the data about the elevator and the building to objects of building & elevator. csvToList: convert csv file that contain the info about the calls that we get and make list of calls from the data. writeOutPutFile: write the elevators that we allocate To the right column un the csv file.


## Screenshots
this is how we tried to understand the method of random un python
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



## Unit test
 We checked that indeed the amount of shows of the high-speed elevator appears more:
![image](https://user-images.githubusercontent.com/73783656/142267727-b0f2238c-dfa4-4bfc-9810-510b07d3ef21.png)



