import csv

import classes


# c = classes.Building('ex1/data/Ex1_input/Ex1_Buildings/B1.json')
# print(c.speed)


def elev_in_list(test_list):
    res = len([ele for ele in test_list if isinstance(ele, dict)])
    return str(res)


my_list = [[], ['a2', 'b2'], ['a3', 'b3', 'c3'], ['a4', 'b4', 'c4', 'd4', 'e4']]
for _ in my_list:
    print(_)


