#!/usr/bin/env python

import sys

def decide_if_palindrome(text):
    # using reverse
    #return text[::-1] == text

    # not using reverse
    for i in range(0, len(text) / 2):
        left = text[i]
        #right = text[len(text)-1 - i]
        right = text[-1 - i]
	if left != right:
	    return False
    return True


for line in sys.stdin:
    text = line[:-1]	# remove EOF
    if decide_if_palindrome(text): 
        print 'yes'
    else:
        print 'no'
