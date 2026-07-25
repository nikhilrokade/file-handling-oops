import csv
import os
from org_emp_oops_python import Employee

class SaveDetails:
    def __init__(self, employee_id, f_name, l_name, age, salary):
        self.employee_id = employee_id
        self.f_name = f_name          
        self.l_name = l_name
        self.age = age
        self.salary = salary

    def save_infile(self):
        path_of_csv = '/home/jupyter-nikhilrokade/Learning/07072026OOPS/save_details.csv'
        os.makedirs(os.path.dirname(path_of_csv), exist_ok=True)
        
        with open(path_of_csv, 'a', newline='', encoding='utf-8') as dest:
            writer = csv.writer(dest)
            writer.writerow([self.employee_id, self.f_name, self.l_name, self.age, self.salary])