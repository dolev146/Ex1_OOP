import random

def allocate(callList, elevatorList):
    """
    we searched all over the internet for a way to make probabilty choicse
    https://pynative.com/python-weighted-random-choices-with-probability/
    we found this link, and took the idea to work
    random.choices (
    population: list (of elevators) ,
    weights = list that stores the ratio between every element in the list,
    k = the amount of objects we want the function to return (the amount of throws the cube)
    return type is list containing elevators objects
    :param callList:
    :param elevatorList:
    :return:
    """
    speed_list = []
    for i in elevatorList:
        speed_list.append(i.speed)
        result = random.choices(
            population=elevatorList,
            weights=speed_list,
            k=len(callList)
        )
    for index, call in enumerate(callList):
        call.idChosenElev = result[index].id
