'''
@author: martin_ayvazov
'''
from collections import namedtuple
from itertools import combinations
import datetime
import pandas

def date_range_overlap(first_start,
                       first_end,
                       second_start,
                       second_end):
    '''
    Detects overlap between 2 date ranges
    Returns overlap in days
    '''
    time_spend = namedtuple('Range', ['start', 'end'])

    #convert dates given as parameters from string to datetime
    first_start = datetime.datetime.strptime(first_start, '%Y-%m-%d').date()
    first_end = datetime.datetime.strptime(first_end, '%Y-%m-%d').date()
    second_start = datetime.datetime.strptime(second_start, '%Y-%m-%d').date()
    second_end = datetime.datetime.strptime(second_end, '%Y-%m-%d').date()

    #store ranges in the namedtuple time_spend
    first_range = time_spend(first_start, first_end)
    second_range = time_spend(second_start, second_end)

    latest_start = (max(first_range.start, second_range.start))
    earliest_end = (min(first_range.end, second_range.end))

    delta = (earliest_end - latest_start).days + 1

    #overlaped days
    return max(0, delta)

def read_file(opened_text_file):
    '''
    Convert the readed data from text file to dictionary
    '''
    list_to_dict = {}
    mask = ["emp_id", "proj_id", "start", "end"]


    readed_lines = opened_text_file.readlines()
    emp_id_list = [x.split()[0] for x in readed_lines]
    proj_id_list = [x.split()[1] for x in readed_lines]
    date_start_list = [x.split()[2] for x in readed_lines]
    date_end_list = [x.split()[3] for x in readed_lines]
    list_from_row = [emp_id_list, proj_id_list, date_start_list, date_end_list]

    for each_column in range(0, 4):
        if each_column == 3:
            for j in range(len(list_from_row[each_column])):
                if list_from_row[each_column][j] == "NULL":
                    list_from_row[each_column][j] = datetime.date.today().strftime('%Y-%m-%d')
        list_to_dict[mask[each_column]] = list_from_row[each_column]
    return list_to_dict

def find_all_ranges(opened_text_file):
    '''
    This function return dataframe with every posible combination
    of employees worked on the same project
    '''
    raw_dataframe = pandas.DataFrame(
        read_file(opened_text_file),
        columns=["emp_id", "proj_id", "start", "end"])
    all_ranges = pandas.DataFrame(columns=['proj_id', 'emp1', 'emp2', 'worktime'])
    projects = raw_dataframe.proj_id.unique()

    for project in projects:
        worked_on_project = raw_dataframe.loc[raw_dataframe['proj_id'] == project]
        for index in list(combinations(worked_on_project.index, 2)):
            combinated = worked_on_project.loc[index, :]
            rangee = date_range_overlap(combinated.iloc[0]['start'],
                                        combinated.iloc[0]['end'],
                                        combinated.iloc[1]['start'],
                                        combinated.iloc[1]['end'])
            if rangee > 0:
                all_ranges = all_ranges.append({'proj_id' : combinated.iloc[0]['proj_id'],
                                                'emp1' : combinated.iloc[0]['emp_id'],
                                                'emp2' : combinated.iloc[1]['emp_id'],
                                                'worktime' : rangee}, ignore_index=True)
    return all_ranges

def find_longest_time_couple(all_ranges):
    '''
    This function returns tuple of
    (list of projects, emp1, emp2, time in days that they worked together)
    '''
    longest_time = all_ranges.loc[all_ranges.worktime == all_ranges.worktime.max()]
    max_range = (longest_time.proj_id.values[0],
                 longest_time.emp1.values[0],
                 longest_time.emp2.values[0],
                 longest_time.worktime.values[0])


    for i, row in all_ranges.iterrows():
        del i
        max_range_of_all_projects = all_ranges.loc[
            ((all_ranges['emp1'] == row['emp1']) |
             (all_ranges['emp1'] == row['emp2'])) &
            ((all_ranges['emp2'] == row['emp1']) |
             (all_ranges['emp2'] == row['emp2']))]

        if all_ranges.worktime.max() < max_range_of_all_projects.worktime.sum():
            max_range = ([x.proj_id for i, x  in max_range_of_all_projects.iterrows()],
                         max_range_of_all_projects.emp1.values[0],
                         max_range_of_all_projects.emp2.values[0],
                         max_range_of_all_projects.worktime.sum())
    return max_range
