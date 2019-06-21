"""
Created on Fri June 21
@author: martin_ayvazov
"""
import datetime
from collections import namedtuple
from CustomExceptions import*
from DataHandler import DataHandler


def validate_date(date_start, date_end):
    '''
    Validates two dates given as string parameters parameters 
    '''
    if date_end == 'NULL':
        date_end = datetime.date.today()
    
    try:
        date_start = datetime.datetime.strptime(
            date_start, '%Y-%m-%d').date()
        if isinstance(date_end, str):
            date_end = datetime.datetime.strptime(
                date_end, '%Y-%m-%d').date()

        if date_start > date_end:
            raise WrongDateFormatError()
        return (date_start, date_end)

    except:
        raise WrongDateFormatError()

def validate_ids(employee_id, project_id):
    '''
    Gets project id and employee id as string parameters.
    Casts each id to integer and validates them. If they are valid
    returns tuple of two ids (employee_id, project_id)
    '''
    employee_id = int(employee_id)
    project_id = int(project_id)
    if not isinstance(employee_id, int) or not isinstance(project_id, int):
        raise WrongIdFormat()
    elif  project_id < 0 or employee_id < 0:
        raise SmallerIdError()
    return (employee_id, project_id)

def date_range_overlap(first_start,
                       first_end,
                       second_start,
                       second_end):
    '''
    Detects range overlap
    '''
    time_spend = namedtuple('Range', ['start', 'end'])
    first_range = time_spend(first_start, first_end)
    second_range = time_spend(second_start, second_end)
    latest_start = (max(first_range.start, second_range.start))
    earliest_end = (min(first_range.end, second_range.end))
    delta = (earliest_end - latest_start).days + 1
    return max(0, delta)

def read_from_file():
    '''
    Reads Data from file and sorting the 
    employees by projects in dict
    '''
    try:
        
        orderd_by_projects = {}
        with open('test.txt') as text_file:
            lines = text_file.readlines()

            for line in lines:
                employee_data = line.split()

                start_date, end_date = validate_date(
                    employee_data[2],
                    employee_data[3])
               
                employee_id, project_id = validate_ids(
                    employee_data[0], employee_data[1])
                
                
                
                if project_id in orderd_by_projects:
                    orderd_by_projects[project_id].append(
                        DataHandler(employee_id,
                                 project_id,
                                 start_date,
                                 end_date))
                else:
                    orderd_by_projects[project_id] = [
                        DataHandler(employee_id,
                                 project_id,
                                 start_date,
                                 end_date)]

            return orderd_by_projects

    except EOFError:
        print("End of file")
    except IndexError:
        print("Wrong data input")
    except WrongDateFormatError:
        print("Wrong formated date in text file")
    except WrongDateIntervalError:
        print("start_date of project is larger than end_date")
    except WrongIdFormat:
        print("emp_id or proj_id are not instance of integer")
    except SmallerIdError:
        print("emp_id or proj_id are smaller")
    except LargerIdError:
        print("emp_id or proj_id are larger")

def find_longest_period(sorted_by_projects):
    '''
    This function takes dictionary as argument. The dictionary has
    project_id as key and list of all employees which has worked in
    that project as value of this dictionary.
    The algorithm 
    '''
    #handle project:(x1,x2)
    all_pairs = {}
    longest_period = 0
    longest_time_pair = tuple()
    for keys, values in sorted_by_projects.items():
        for first_employee in values:
            for second_employee in values[values.index(first_employee)+1:]:
                range_in_days = date_range_overlap(
                    first_employee.start_date,
                    first_employee.end_date,
                    second_employee.start_date,
                    second_employee.end_date)
                
                if range_in_days > longest_period:
                    longest_period = range_in_days
                    longest_time_pair = (first_employee, second_employee, range_in_days)
    return longest_time_pair
