import random


def allocate(callList, elevatorList):
    """
    we searched all over the internet for a way to make preference choices
    https://pynative.com/python-weighted-random-choices-with-probability/
    we found this link, and took the idea to work
    speed list:  contain all the data about the average of the elevators
    random.choices (
    population: list (of elevators) ,
    weights = list that stores the ratio between every element in the list,
    k = the amount of objects we want the function to return (the amount of throws the cube)
    return type is list containing elevators objects
    :param callList:
    :param elevatorList:
    :return void:
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
