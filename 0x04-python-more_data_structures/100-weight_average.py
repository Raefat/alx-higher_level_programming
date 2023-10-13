#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        avg = 0
        weights = 0
        for i in range(len(my_list)):
            weights += my_list[i][1]
            avg += my_list[i][0] * my_list[i][1]
        return (avg / weights)
