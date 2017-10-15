#!/usr/bin/env python

import sys

def initialize_table(col, row):
    table = [[True for j in range(col)] for i in range(row)]
    return table

def calculate_negative_sum(list):
    sum = 0
    for i in list:
        if i < 0:
            sum = sum + i
    return sum
  
def calculate_positive_sum(list):
    sum = 0
    for i in list:
        if i > 0:
            sum = sum + i
    return sum

def decide_if_sum_subset_exists(list, S):
    N = calculate_negative_sum(list)
    P = calculate_positive_sum(list)

    table = initialize_table(-N+P+1, len(list))
    # row of x1
    for i in range(0, len(list)):
	if list[0] == S:
            table[0][S-N] = True

    # rows of x2, x3, ... xi
    for i in range(1, len(list)):
        for j in range(0, N+P):
            if (list[i] == j+N or 
		table[i-1][j] or 
		table[i-1][j - list[i]]):

                table[i][j] = True
        
    return table[len(list) - 1][S-N]


def parse_list(text):
    list = text.split(',')
    return [int(s) for s in list]

for line in sys.stdin:
    text = line[:-1]	# remove EOF
    list = parse_list(text)
    sum = 0  # 7 --> no

    if decide_if_sum_subset_exists(list, sum): 
        print 'yes'
    else:
        print 'no'


