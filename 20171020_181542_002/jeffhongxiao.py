#!/usr/bin/env python

import sys


def parse_list(text):
    splitted = text.split(',')
    listA = [int(s) for s in splitted[0].split(' ')]
    listB = [int(s) for s in splitted[1].split(' ')]
    return listA, listB


def decide_if_sublist(A, B):
    lenB = len(B)
    lenA = len(A)

    index = []
    for i in range(lenB):
        if A[0] == B[i]:
            index.append(i)

    flag = True
    for i in index:
        for k in range(0, lenA):
            if i + k >= lenB:
                return False
            if A[k] != B[i + k]:
                flag = False
    return flag


for line in sys.stdin:
    text = line[:-1]    # remove EOF
    listA, listB = parse_list(text)
    # print listA
    #print listB

    if decide_if_sublist(listA, listB):
        print 'yes'
    else:
        print 'no'
