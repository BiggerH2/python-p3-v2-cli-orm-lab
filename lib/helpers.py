from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# Employee functions

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'Employee {name} not found')


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title: ")
            employee.job_title = job_title
            department_id = input("Enter the employee's new department id: ")
            employee.department_id = department_id

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f'Department {department_id} not found')


# Main CLI loop

def main():
    while True:
        print("\nPlease select an option:")
        print("0. Exit the program")
        print("1. List all departments")
        print("2. Find department by name")
        print("3. Find department by id")
        print("4. Create department")
        print("5. Update department")
        print("6. Delete department")
        print("7. List all employees")
        print("8. Find employee by name")
        print("9. Find employee by id")
        print("10. Create employee")
        print("11. Update employee")
        print("12. Delete employee")
        print("13. List all employees in a department")

        try:
            choice = int(input("> "))
            if choice == 0:
                exit_program()
            elif choice == 1:
                list_departments()
            elif choice == 2:
                find_department_by_name()
            elif choice == 3:
                find_department_by_id()
            elif choice == 4:
                create_department()
            elif choice == 5:
                update_department()
            elif choice == 6:
                delete_department()
            elif choice == 7:
                list_employees()
            elif choice == 8:
                find_employee_by_name()
            elif choice == 9:
                find_employee_by_id()
            elif choice == 10:
                create_employee()
            elif choice == 11:
                update_employee()
            elif choice == 12:
                delete_employee()
            elif choice == 13:
                list_department_employees()
            else:
                print("Invalid choice. Please enter a number from 0 to 13.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
        except Exception as exc:
            print(f"Error: {exc}")

if __name__ == "__main__":
    main()
