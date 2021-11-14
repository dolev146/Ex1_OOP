import csv
import sys
import classes


def Ex1(Building_json, Calls_csv, output_csv):  # --> input: <Building.json> <Calls.csv> <output.csv>

    all_calls = []

    with open(Calls_csv) as f:  # getting the sum of lines in Calls_csv
        lines = sum(1 for line in f)
    f.close()

    for row in lines[1:]:  # loop that start from 1
        a = classes.Call(Calls_csv, row)  # put the csv and the num of the call
        all_calls.append(a)

    b = classes.Building(Building_json)
    num_of_elev = elev_in_list(b)  # ->  function that return the sum of the elev in b

    if num_of_elev == 1:  # if there us only one elev in this case
        insert_zero(output_csv)

    all_elev = []
    for _ in num_of_elev:  # create a list of lists for each of elevators:
        all_elev.append([])

    for index in all_calls:  # loop that send to "allocate" calls by over the list of calls.
        allocate(all_calls[index], all_elev)


# for insert in all_elev:   --> the loop that insert the final allocation to the output
# insert_ans_to_csv(index, i, output_csv)
'''
 this function allocate the call to specific elevator
    call: the call that we need to allocate (contains: src,dest and time stamp)
    all_elev: list of lists: each list represent elevator
'''


def allocate(call: classes.Call, all_elev) -> int:
    # direction = direction_call(call)
    ans = []
    our_time = call.time
    for each_list in all_elev:  # iter the elev list and find the best elev to allocate

        if each_list.__len__() == 0:
            all_elev[each_list].append(call)

        # if each_list.__len__() > 0 && each_list[-1].dest - each_list[-1].src  :

        our_el = {}
        if each_list.__len__() > 0:
            time_for_floor = calc_time(each_list.index(), all_elev[each_list])
            last_call = each_list[-1]
            other_time = last_call.time
            fin_time = our_time - other_time



'''
this method insert the chosen elev to the csv file that we need to return  
index: the index of the call in the csv file
choose_elev
output_csv: the csv that we need to return at the end..
 '''


def calc_time(index: int):
    return 1


def direction_call(call):
    if (call.dest - call.src) > 0:
        return 1  # up
    else:
        return -1


def insert_ans_to_csv(index, choose_elev, output_csv):
    with open(output_csv) as file:
        writer = csv.writer(file, delimiter=',')
        cur_line = 1
        for row in writer:
            if cur_line == index:
                row[5] = choose_elev
            break
        else:
            cur_line += 1
        file.close()


def insert_zero(output_csv):  # used when we have only one elev
    with open(output_csv) as file:
        writer = csv.writer(file, delimiter=',')
        cur_line = 1
        for row in writer:
            row[5] = 0
        file.close()


# iter the list and count how much dict we have
def elev_in_list(test_list):
    res = len([ele for ele in test_list if isinstance(ele, dict)])
    return str(res)

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
'''
this function decide.. 
'''
# def priority(index, floor):

if __name__ == '__main__':
    bui = classes.Building(r'ex1/data/Ex1_input/Ex1_Calls/Calls.csv')
