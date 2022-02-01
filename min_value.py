#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Feb 1 2022
# This program generates 10 random numbers
# and finds the smallest.
import constant
import random


# function to find the samllest number
def find_min_value(rand_list):
    smallest = constant.MAX_NUM
    for current_num in rand_list:
        if current_num < smallest:
            smallest = current_num
    return smallest


def main():
    # declare list
    main_list = []
    # generate random numbers
    for counter in range(constant.MAX_SIZE):
        rand = random.randint(constant.MIN_NUM, constant.MAX_NUM)
        main_list.append(rand)
    # display random numbers
    print("The list is: {}". format(main_list))
    # call function to find min value
    smallest_num = find_min_value(main_list)
    # display min value
    print("The smallest number is: {}". format(smallest_num))


if __name__ == "__main__":
    main()
