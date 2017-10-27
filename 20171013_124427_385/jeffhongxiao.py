#!/usr/bin/env python

import sys


def initialize_table(col, row):
    table = [[False for j in range(col)] for i in range(row)]
    return table


def calculate_negative_sum(list):
    sum = 0
    for num in list:
        if num < 0:
            sum = sum + num
    return sum


def calculate_positive_sum(list):
    sum = 0
    for num in list:
        if num > 0:
            sum = sum + num
    return sum


def myprint(table):
    for row in table:
        string = ''
        for val in row:
            if (val):
                string += 'T '
            else:
                string += 'F '
        print string
    print '-----------------------------'


def decide_if_sum_subset_exists(list, S):
    N = calculate_negative_sum(list)
    P = calculate_positive_sum(list)

    # if (S == N or S == P):
    #    return True

    table = initialize_table(-N + P + 1, len(list))
    # row of x1
    for s in range(0, -N + P + 1):
        if list[0] == +N + s:
            table[0][s] = True

    # rows of x2, x3, ... xi
    for i in range(1, len(list)):
        # cols of N, N+1, ..., P
        myprint(table)		# TODO: debug output
        for j in range(0, -N + P + 1):
            if ((list[i] == +N + j or
                 table[i - 1][j])):
                table[i][j] = True
            if ((-N + (j + N) - list[i] >= 0 and    # Q: out of bound?
                 table[i - 1][j - list[i]])):
                table[i][j] = True

    myprint(table)

    return table[len(list) - 1][-N + S]


def parse_list(text):
    list = text.split(',')
    return [int(s) for s in list]


for line in sys.stdin:
    text = line[:-1]    # remove EOF
    list = parse_list(text)
    sum = 0

    if decide_if_sum_subset_exists(list, sum):
        print 'yes'
    else:
        print 'no'
