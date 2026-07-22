from datetime import date 
from abc import ABC, abstractmethod #abstarct method used from here
import re #regex imported from here

class Organisation(ABC):
    def __init__(self, unique_id: int, organisation_names: str, humans: int):
        self.unique_id = unique_id
        self.organisation_names = organisation_names #encapsulation implemnted with attribute
        self.humans = humans 

    def show_industry_details(self):
        print(f"\nOrganisation Name: {self.organisation_names}")
        public_organisation_id = range(1, 2000)        
        private_organisation_id = range(2000, 10001)
        if self.unique_id in public_organisation_id:
            sector_type = "Public Sector"
            governance = "Government of India"
        elif self.unique_id in private_organisation_id:
            sector_type = "Private / Corporate Sector"
            governance = "Supervised by Government Laws"
        else:
            print(f"Error: The ID {self.unique_id} does not match any sector.")
            return
        print(f"Sector Type : {sector_type}")
        print(f"Governed By : {governance}")
        print(f"Registered ID: {self.unique_id}")
        return

    def industry_size(self):
        count = self.humans
        if count <= 50:
            return("Start up or Small Scale Industry")
        elif 50 < count <= 500:
            return("Growing  but small scale industry")
        elif 500 < count <= 5000:
            return("Medium Scale Industry \n")
        elif count > 5000:
            return("It is a MNC or Large Scale Industry")
        
    @property     
    @abstractmethod
    def departments(self):
        #abstraction
        return
 
    def headquater(self):
        """Location of Organisation""" #polymorphism
        address = "RBI, E-Block, BKC, Mumbai"
        return (f"Address of Organisation governance: {address}")

#inheritance from Organisation
class Employee(Organisation):
    employee_count = 0
    def __init__(self, employee_id: int, f_name: str, l_name: str, age: int, grade, salary: float, unique_id: int, organisation_names: str = "rebit"):
        super().__init__(unique_id, organisation_names, humans=0)
        self.employee_id = employee_id
        self.first_name = f_name
        self.last_name = l_name
        self._age = age
        self.grade = grade
        self.__salary = salary #encapsulation
        self.employees = []

    def employee_basic_details(self):
        return f'Basic Details of Employees:\nEmployee Id: {self.employee_id}, Employee Full Name: {self.first_name} {self.last_name} Age: {self._age}'

    def employee_age(self, year, month, day):
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))        
        return f'Age of Employee: {age}'
    
    def employee_grade_and_salary_structure(self):
        basic_salary = 0
        grade = ['A', 'B', 'C']
        self.__salary = [15000, 14500, 14000] #removed grade[0] by default 
        if self.grade == grade[0]:
            basic_salary = self.__salary[0]
        elif self.grade == grade[1]:
            basic_salary = self.__salary[1]
        elif self.grade == grade[2]:
            basic_salary = self.__salary[2]

        hra = 0.2 * basic_salary
        da = 0.5 * basic_salary
        pf = 0.11 * basic_salary
        if self.grade == grade[0]:
            allowance = 1700
        elif self.grade == grade[1]: 
            allowance = 1500
        else:
            allowance = 1300
        self.gross_salary = round(basic_salary + hra + da + allowance - pf)
        return f"Basic Salary: {self.__salary[0]} for Grade: {grade[0]}\nBasic Salary: {self.__salary[1]} for Grade: {grade[1]}\nBasic Salary: {self.__salary[2]} for Grade: {grade[2]}"

    @property
    def salary(self):
        """salary is private""" #private __salary also encapsulation method
        return self.__salary 
 
    def add_employee(self):
        if self.employee_id in self.employees:
            return f'Employee present: {self.first_name} {self.last_name}'
        self.employees.append(self.employee_id)
        return f'Employee added with Id: {self.employee_id}'
    
    @property
    def departments(self):
        deparment_divisons = ['Cyber Security', 'Software Development and Testing', 'Admin']
        if self.grade == 'A':
            i = deparment_divisons[0]
        elif self.grade == 'B':
            i = deparment_divisons[1]
        elif self.grade == 'C':
            i = deparment_divisons[2]
        else:
            return "No Department Assigned"
        return f"\nDepartment and Division: {i} \n"

    def employee_assets(self, *args, **wfh):
        if self.employee_id in self.employees:
            welcome_kit = True
            work_station = True
            laptop_issued = True
            laptop_charger_number = True
            work_dekstop = True
        else:
            return (f"Employee is not a part of Organisation{self.employee_id}")
        return f"Assets Provided to Employees: \nLaptop : {laptop_issued},\nLaptop Charger: {laptop_charger_number},\nReceived Welcome kit: {welcome_kit},\nDesk Allocation: {work_station},\nDesktop Screen Provided: {work_dekstop} \n{args} \n{wfh}"
    
    #method overriding runtime Polymorphism 
    def headquater(self):
        address = "501, floor 5th, Mindspace, Jui Nagar, Navi Mumbai"
        return (f"Address of Headquater: {address}")
    

class FinanceManagement:
    bank_accounts_number_validation = r'^\d{9,18}$'

    def __init__(self, account_number: int, pay_raise: float, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.pay_raise = pay_raise
        
    def check_current_balance(self):
        return f"Current Balance is: {self.balance}"
    
    def organisation_emp_account_number_details(self):
        self.organisation_employee_accounts = []
        count = 1
        while True:
            self.account_number = 4877074215
            user_input = input(f"Enter organisation_emp_account: {count} (or type 'exit'): ").strip()
            if user_input.lower() == 'exit':
                print("\nExiting account entry, accounts collected:")
                break
            if not re.match(self.bank_accounts_number_validation, user_input):
                print("Invalid input! Account number must be strictly between 9 and 18 digits. Try again.")
                continue
            self.organisation_employee_accounts.append(user_input)
            print(f"Successfully added employee Bank account_{count}: {user_input}")
            count += 1
            return

    #method injection and Type hinting
    def deposit(self, employee: Employee, amount):
        print(f"Depositing Amount to Employee ID {employee.employee_id} ---")
        print(f"Printing Deposit Amount: {amount}")
        self.balance += amount
        return f"Successfully deposited: {amount} Current Balance is: {self.balance}"
    
    #method injection and Type hinting
    def withdraw(self, employee: Employee, amount):
        print(f"Requesting Withdrawal for Employee ID {employee.employee_id} ---")
        if self.balance < amount:
            print(f"Withdraw fail Insufficient balance{self.balance}")
        else:
            self.balance -= amount
            print(self.balance)
            print(f"Amount withdrawn: {amount}")
        return
    
    def apply_raise(self,employee: Employee):
        employee_current_salary = employee.salary
        self.pay_raise = float(employee_current_salary * 10)
        return f"Appraisal Calculated! New Pay Scale: ₹{self.pay_raise}"