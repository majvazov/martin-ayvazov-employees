"""
Created on Fri June 21 
@author: martin_ayvazov
"""
class WrongIdFormat(Exception):
    '''
    Raised when emp_id or proj_id are not instance of integer
    '''
class SmallerIdError(Exception):
    '''
    Raised when emp_id or proj_id are smaller
    '''
    pass

class LargerIdError(Exception):
    '''
    Raised when emp_id or proj_id are larger
    '''
    pass

class WrongDateFormatError(Exception):
    '''
    Raised when submitted date is not formated correctly
    '''
    pass

class WrongDateIntervalError(Exception):
    '''
    Raised when start_date of project is larger than end_date
    '''
    pass

