import sys
import classes


def Ex1(Building_json, Calls_csv, output_csv):  # --> input: <Building.json> <Calls.csv> <output.csv>

    all_calls = []
    i = 1  # need to start from the first place
    for _ in all_calls:
        a = classes.Call(Calls_csv, i)  # put the csv and the num of the call
        all_calls.append(a)

    b = classes.Building(Building_json)
    num_of_elev = elev_in_list(b)  # ->  function that return the sum of the elev in b

    all_elev = []
    for num_of_elev in all_elev:  # create a list of lists for each of elevators:
        all_elev.append([])
       #{'done_last_call': 0.0} ??
    # done_last_call: when the elev finish her duty and ready to the next call, will be at -1 pos (end of the list..)

    for index in all_calls:
       allocate(all_calls[index], all_elev, output_csv)


'''
 this function allocate the call to specific elevator
 index: the index of the elev in the call list
 all_calls: all the calls that we need to allocate (contains: src,dest and time stamp)
 all_elev: list of list: each list represent elevator
'''

def allocate(call, all_elev, output_csv)-> int:

    for i in all_elev:
        if:
            insert_ans_to_csv(i, output_csv)










'''
this method insert the chosen elev to the csv file that we need to return 
'''
def insert_ans_to_csv(choose_elev, output_csv):



#def dest(b):


# iter the list and count how much dict we have
def elev_in_list(test_list):
    res = len([ele for ele in test_list if isinstance(ele, dict)])
    return str(res)


'''
this function decide.. 
'''
# def priority(index, floor):

if __name__ == '__main__':
    bui = classes.Building(r'ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv')


