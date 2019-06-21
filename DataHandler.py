"""
Created on Fri June 21
@author: martin_ayvazov
"""
class DataHandler:
    '''
    Handle one line from text document.
    Used as structure for faster data proccessing
    '''
    def __init__(self, employee_id, project_id, start_date, end_date):
        self.employee_id = employee_id
        self.project_id = project_id
        self.start_date = start_date
        self.end_date = end_date
        
    def __str__(self):
        return "EMP_ID {}\nPROJ_ID {}\nDATE_START {}\nDATE_END {}\n".format(self.employee_id,
        self.project_id,
        self.start_date,
        self.end_date)
