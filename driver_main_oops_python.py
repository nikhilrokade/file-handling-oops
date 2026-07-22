from classoop import Organisation, Employee, FinanceManagement
from employeesdetail import SaveDetails
import csv, os

def main():
    print("Driver function of this Program! \n")

    path_of_csv = '/home/Learning/07072026OOPS/save_details.csv'
    os.makedirs(os.path.dirname(path_of_csv), exist_ok=True)
    with open(path_of_csv, 'w', newline='', encoding='utf-8') as dest:
        writer = csv.writer(dest)
        writer.writerow(['Employee ID', 'First Name', 'Last Name', 'Age', 'Salary'])
    save_object = SaveDetails(employee_id=1, f_name="Nikhil" , l_name="Rokade", age=30, salary=6000)
    save_obj_1 = SaveDetails(employee_id=2, f_name= "Test", l_name="set", age=25, salary=3000)
    save_obj_2 = SaveDetails(employee_id=3, f_name="Durgesh" , l_name="Singh", age=25, salary=4000)

    save_object.save_infile()
    save_obj_1.save_infile()
    save_obj_2.save_infile()
    
    print("\n==================================== Above Printed and Exited CSV class ================================================")
    #calling Organisation class
    emp_det = Employee(101,'Nikhil', 'Rokade', 30, 'B', 6000, 2000, 'ReBIT') #reduces the code by inheritance
    org_type = emp_det.show_industry_details()
    org_size = emp_det.industry_size()
    org_hea = emp_det.headquater()

    print(org_type)
    print(org_size)
    print(org_hea)

    print("\n===================================== Above Printed and Exiting Organisation class =============================================== \n")

    #calling Employee class below

    basic_employee_info = emp_det.employee_basic_details()
    desg_sal = emp_det.salary
    emp_add = emp_det.add_employee()
    emp_asset_details = emp_det.employee_assets("Mouse ", "Headphone","Id Card", made = "Lenovo", delivered = True)
    dept_div = emp_det.departments
    sal_grad = emp_det.employee_grade_and_salary_structure
    emp_age = emp_det.employee_age(1996, 8, 9)
    addres = [emp_det.headquater()]
    print(emp_add)
    print(basic_employee_info)
    print(f"Get Employee Salary: {desg_sal}")
    print(dept_div)
    print(emp_asset_details)
    print(addres)

    print("\n===================================== Above Printed and Exiting Employee class =============================================== \n")

    #calling FianceManagement
    finance_details = FinanceManagement(1234567890, 10, 10000)
    bal_check = finance_details.check_current_balance()
    print(f"{bal_check}")
    dep = finance_details.deposit(emp_det, 5000)
    check_withdraw = finance_details.withdraw(emp_det, 1100.50)
    check_sal_raise = finance_details.apply_raise(emp_det)
    print(check_sal_raise)
    print("\n===================================== Above Printed and Exiting Finance Management class =============================================== \n")

if __name__=="__main__":
    main()