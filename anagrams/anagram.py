#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    # Check if string length is odd. If so, it cannot be an anagram.
    if len(s) % 2 != 0:
        return -1

    # Split the string into two halves
    half_1 = s[0: len(s) // 2]
    half_2 = s[len(s) // 2: len(s)]

    # Initialize a counter for characters that need removal
    num_characters_to_remove = 0

    # Iterate through characters in the first half
    for char in half_1:
        # Check if the character exists in the second half
        if char in half_2:
            # Remove the first occurrence of the character from the second half
            half_2 = half_2.replace(char, '', 1)
        else:
            # If the character is not found, increment the counter
            num_characters_to_remove += 1

    # Return the number of characters that need removal
    return num_characters_to_remove

  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
