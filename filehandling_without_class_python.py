from datetime import date

class SaveDetails:
    print("Hello Program Started")
    mem_employee_details = {}
    mem_employee_office_details = {}

    def employee_details(emp_id: int, first_name: str, last_name: str, email_id: str, designation: str, department: str, joining_date: date) -> dict:
        return {"Id": emp_id, "Full Name": f"{first_name} {last_name}","email": email_id, "Role": designation,"Work": department,"Joined On": joining_date}

def employee_office_details(emp_id: int, salary: float, variable_pay: float, tax_deduction: float) -> dict:
    salary_structure = {
        "id": emp_id,
        "Salary": salary,
        "Bonus": variable_pay,
        "Taxation": tax_deduction
    }
    return salary_structure

master_employee_list = [] 

def add_employee():
    print("Add Employee Started")
    global mem_employee_details
    global mem_employee_office_details
    while True:
            emp_id = input("Enter Employee Id (for e.g. 01 0r 1 and not 1.0): ").zfill(2)
            if emp_id.isdigit():
                print(f"Ok!: {emp_id}" )
                break
            else:
                print(" Please Enter a Valid format: ")

    while True:     
        f_name = str(input("Enter the First name (Only STring values) : "))
        if not f_name.isalpha() or not f_name.istitle():
            print("Please enter first word Capital and all letters not number")
        else: 
            print("Correct")
            break

    while True:
        l_name = str(input("Enter Last name (Only String values) : "))
        if not l_name.isalpha() or not l_name.istitle():
            print("Please enter first word Capital and all letters not number")
        else:
            print("Correct")
            break
    email = str(input("Enter the Email Address (Only STring values) : "))
    role = str(input("Enter the Designation (Only STring values) : "))
    dept = str(input("Enter the Department (Only STring values) : "))
    joindate = (input("Enter the Joining Date (only in YYYY-MM-DD): "))
    j_date = date.fromisoformat(joindate)
    sal = float(input("Enter the Salary amount: "))
    var_pay = float(input("Enter the variable pay: "))
    tax_ded = float(input("Enter the amount for Tax: "))
    print("It is working ")

    if emp_id in mem_employee_details or emp_id in mem_employee_office_details:
        print("Employee already exists.")
        return
    try:
        mem_employee_details[emp_id] = employee_details(
            emp_id=emp_id,
            first_name=f_name,
            last_name=l_name, 
            email_id=email,
            designation=role,
            department=dept,
            joining_date=j_date
        )
        mem_employee_office_details[emp_id] = employee_office_details(
            emp_id = emp_id,
            salary=sal,
            variable_pay=var_pay,
            tax_deduction= tax_ded
        )
    except ValueError:
        print("Please check the Data type!")
        return 
    
    save_infile(emp_id, f_name, l_name, email, dept, j_date, sal, var_pay, tax_ded)
    print("Saved in emply")


def update_employee():
    global mem_employee_details
    global mem_employee_office_details
    print("Update Employee Started")

    emp_id_input = input("Enter Employee Id (e.g., 01): ").strip()
    if not emp_id_input.isdigit():
        print("Invalid ID format! Must be an integer number.")
        return
    emp_id = emp_id_input.zfill(2)

    if emp_id not in mem_employee_details or emp_id not in mem_employee_office_details:
        print("Employee Not found.")
        print("Sending to Add the Employee")
        add_employee()
        return 
    f_name = str(input("Enter the First name (Only STring values) : "))
    l_name = str(input("Enter Last name (Only String values) : "))
    email = str(input("Enter the Email Address (Only STring values) : "))
    role = str(input("Enter the Designation (Only STring values) : "))
    dept = str(input("Enter the Department (Only STring values) : "))
    while True:
        try:
            joindate = (input("Enter the Joining Date (only in YYYY-MM-DD): "))
            j_date = date.fromisoformat(joindate)
            break
        except ValueError as exp_info:
            print(f"Please Check Date {exp_info.value}")
    sal = float(input("Enter the Salary amount: "))
    var_pay = float(input("Enter the variable pay: "))
    tax_ded = float(input("Enter the amount for Tax: "))

    mem_employee_details[emp_id] = employee_details(
        emp_id=emp_id,
        first_name=f_name,
        last_name=l_name, 
        email_id=email,
        designation=role,
        department=dept,
        joining_date=j_date
    )
    mem_employee_office_details[emp_id] = employee_office_details(
            emp_id = emp_id,
            salary=sal,
            variable_pay=var_pay,
            tax_deduction= tax_ded
        )
    save_infile(emp_id, f_name, l_name, email, dept, j_date, sal, var_pay, tax_ded)
    print("Updated and Saved in emply")
    print("Update Success")


def save_infile(emp_id, f_name, l_name, email, dept, j_date, sal, var_pay, tax_ded):
    saveinfile = f"EmployeeId: {emp_id}, First Name: {f_name}, Last Name: {l_name}, Email Address:{email},Department: {dept}, Joining Date: {j_date},Salary: {sal},Variable Pay: {var_pay},Tax dedcution: {tax_ded}\n"
    with open('/home/jupyter-nikhilrokade/Learning/29062026/emply.txt', 'a') as dest:
        dest.write(saveinfile)
    print(f"Successfully saved: {saveinfile}")


mem_employee_details["01"] = employee_details(1, "Nikhil", "Rokade", "NikhilRokade@gmail.com", "Engineer Development", "DS", date(2022, 12, 5))

mem_employee_office_details["01"] = employee_office_details(1, 5000, 500, 0)
print("\n")

while True:
    print("\n Select from below:-")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Exit Program")
    
    select = input("Select an option (1-3): ")

    if select == "1":
        add_employee()
        
    elif select == "2":
        update_employee()
        
    elif select == "3":
        print("Exiting program!")
        break
        
    else:
        print("Invalid Selection! Please select 1, 2, or 3.")