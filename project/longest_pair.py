'''
@author: martin_ayvazov
'''
import os
import sys
from packages.functions import find_all_ranges, find_longest_time_couple


if  __name__ == "__main__":

    try:
        RANGES = find_all_ranges(open(os.path.join(sys.path[0], "test.txt"), "r"))
        print(find_longest_time_couple(RANGES))

    except IOError:
        print("Cant open file test.txt")
    except IndexError:
        print("Wrong data format")
    except Exception:
        print("Unexpected error")
