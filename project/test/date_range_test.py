import unittest
import sys
#step back one directory
sys.path.append("..")
#import all functions in functions.py
from packages.functions import (date_range_overlap,
                                find_longest_time_couple,
                                find_all_ranges,
                                read_file)

class TestLongestPair(unittest.TestCase):
    '''
    Automated test scripts for functions in functions.py
    '''
    def test_date(self):
        '''
        Unit testing date_range_overlap function used for detecting range in days between two date ranges
        '''
        self.assertEqual(date_range_overlap('2012-03-28', '2016-06-02', '2013-04-02', '2018-10-29'), 1158)
        self.assertEqual(date_range_overlap('not a date', 'not a date', 'not a date', 'not a date') , 'Wrong date format!')
        #excepting integer values given as arguments
        self.assertEqual(date_range_overlap(21, 23, 34, 45) , 'Wrong date format!')
    def test_longest_couple(self):
        '''
        To do
        '''
        pass
    def test_file_reading(self):
        '''
        To do
        '''
        pass
    def test_all_ranges(self):
        '''
        To do
        '''
        pass
if __name__ == '__main__':
    unittest.main()
