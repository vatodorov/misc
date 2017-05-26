# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:06:50 2017

@author: bre49823
"""

import sys

def Hello(name):
    if name == 'Alice':
        name == name + '????'
    name = name + '!!!!'
    print('Hello ' + name)

# Print a little greeting
def main():
    Hello(sys.argv[1])

    
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    main()

