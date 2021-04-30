#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    count = 0
    for i in my_list:
        count += i[1]
    if count is 0:
        return 0
    return (sum(map(lambda x: x[0] * x[1], my_list)) / count)
