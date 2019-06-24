'''
@author: martin_ayvazov
'''
import os
import sys
from packages.functions import find_all_ranges, find_longest_time_couple


if  __name__ == "__main__":

    try:
        RANGES = find_all_ranges(open(os.path.join(sys.path[0], "test.txt"), "r"))
        LONGEST_TIME_PAIR = find_longest_time_couple(RANGES)

        #output
        print("projects: {}".format(LONGEST_TIME_PAIR[0]))
        print("first employee: {}".format(LONGEST_TIME_PAIR[1]))
        print("second employee: {}".format(LONGEST_TIME_PAIR[2]))
        print("ranges in days: {}".format(LONGEST_TIME_PAIR[3]))


    except IOError:
        print("Cant open file test.txt")
    except IndexError:
        print("Wrong data format")
    except Exception:
        print("Unexpected error")
