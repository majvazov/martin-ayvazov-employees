"""
Created on Fri June 21
@author: martin_ayvazov
"""
# pylint: disable=wildcard-import
import datetime
from collections import namedtuple
from CustomExceptions import*
from functions import *
from DataHandler import DataHandler


if  __name__ == "__main__":
    EMPLOYEES = read_from_file()

    LONGEST_TIME_PAIR = find_longest_period(EMPLOYEES)
    for items in LONGEST_TIME_PAIR:
        print(items)

