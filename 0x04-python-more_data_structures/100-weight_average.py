#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    tot_score = 0
    tot_weight = 0

    for tups in my_list:
        tot_score += tups[0] * tups[1]
        tot_weight += tups[1]

    return (tot_score / tot_weight)
