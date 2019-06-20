"""
Created on Thur June 20 03:53 2019
@author: martin_ayvazov
"""

import random
import datetime


employees = 200
projects = 9
def random_date(start, end):
    """
    """
    delta_days = (end - start).days
    while True:
        random_date = start + datetime.timedelta(days = random.randrange(delta_days+1))
        if holiday_check(random_date) == True:
            return random_date
       

def holiday_check(random_date):
    """
    """
    holidays = {1:1, 3:3, 1:5, 6:9, 22:9,24:12, 25:12, 26:12}
    if(random_date.weekday() == 5 and random_date.weekday() == 6):
        return False
    elif random_date.day in holidays:
        if random_date.month == holidays.get(random_date.day):
            return False
    return True
    

def simulate_data():
    """
    """
    d1 = datetime.date(2012,1,1)
    d2 = datetime.date.today()
    text_file = open("test.txt", "w")

    for i in range(1, employees+1):
        project_id = random.randrange(1,projects+1)
        start_date = random_date(d1,d2)
        end_date = random_date(start_date, d2)
        if end_date == d2:
            end_date = "NULL"
            data_to_string = "{} {} {} {}\n".format(
                i, project_id, start_date.isoformat(), end_date)
        else:
            data_to_string = "{} {} {} {}\n".format(
                i, project_id, start_date.isoformat(), end_date.isoformat())
        print(data_to_string)
        text_file.write(data_to_string)
        
    
    
simulate_data()
