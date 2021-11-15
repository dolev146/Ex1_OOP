from Elevator import Elevator
from ElevatorCall import ElevatorCall
from Building import Building
import random


# In [1]: import random

# In [2]: random.choices(
# ...:     population=[{'id': 1, 'speed': 7 }, {'id': 2, 'speed': 3 }],
# ...:     weights=[0.7, 0.3],
# ...:     k=1
# ...: )


def allocate(call: ElevatorCall, building: Building,
             building_size: int,
             fastest_elv: Elevator,
             fast_elev_list: list,
             all_elev
             ) -> int:
    return 1


#  random.choices(
#     population=[{'id': 1, 'speed': 7}, {'id': 2, 'speed': 3}],
#     weights=[0.7, 0.3],
#     k=1
# )

# # direction = direction_call(call)
# ans = []
# # for index, item in enumerate(items):
# # print(index, item)
# # iter the elev list and find the best elev to allocate
# for index, each_elev in enumerate(all_elev):
#     if len(each_elev.callList) == 0:
#         random.choices(
#             population=[{'id': 1, 'speed': 7}, {'id': 2, 'speed': 3}],
#             weights=[0.7, 0.3],
#             k=1
#         )

#     # if each_elev.len() > 0 && each_elev[-1].dest - each_elev[-1].src  :
# for index, each_elev in enumerate(all_elev):
#     if len(each_elev.callList) > 0:
#         time_for_dest = each_elev.floorTime * \
#             abs(call.destinationOfCall - call.sourceOfCall)
#         last_call_time_stamp = each_elev.callList[-1].timeStamp
#         fin_time = call.timeStamp - last_call_time_stamp
#         if fin_time < time_for_dest:
#             ans.append((index, time_for_dest))
# # min([], default="EMPTY")

# rand_index = 0
# if len(ans) == 0:
#     elev_indexes_range = len(all_elev) - 1
#     rand_index = random.randint(0, elev_indexes_range)
#     elev_ = (rand_index, 0)
# else:
#     elev_ = min(ans, key=operator.itemgetter(1))
# all_elev[elev_[0]].callList.append(call)
# return elev_[0]

def random_allocate(callList, elevatorList):
    speed_list = []
    for i in elevatorList:
        speed_list.append(i.speed)
    result = random.choices(
        population=elevatorList,
        weights=speed_list,
        k=len(callList)
    )
    for index , call in enumerate(callList):
        call.idChosenElev = result[index].id
    
    
    # for index, each_elev in enumerate(all_elev):
    #     if len(each_elev.callList) > 0:
    #         time_for_dest = each_elev.floorTime * abs(call.destinationOfCall - call.sourceOfCall)
    #         last_call_time_stamp = each_elev.callList[-1].timeStamp
    #         fin_time = call.timeStamp - last_call_time_stamp
    #         if fin_time < time_for_dest:
    #             ans.append((index, time_for_dest))
    # # min([], default="EMPTY")
