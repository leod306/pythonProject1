# Leo Dahlen
#CBIS 4210
#assignment 2.2
# 9/3/2024

#payroll with user input name, hoursly rate, and hours worked
# Global list to store employee data
employees = []


def add_employee():
    """
    Adds an employee to the global employee list.
    Asks for employee's name and hourly rate, then stores them.
    """
    name = input("Enter employee name: ")
    hourly_rate = float(input(f"Enter hourly rate for {name}: "))

    # Creating a dictionary to represent the employee and storing the name and hourly rate
    employee = {
        "name": name,
        "hourly_rate": hourly_rate,
        "hours_worked": 0,
        "gross_pay": 0,
        "deductions": 0,
        "net_pay": 0
    }

    # Adding the employee dictionary to the employees list
    employees.append(employee)


def set_hours_worked(employee):
    """
    Sets the hours worked for an employee.
    Asks the user to input the number of hours worked for the employee.
    """
    hours_worked = float(input(f"Enter hours worked for {employee['name']}: "))
    employee['hours_worked'] = hours_worked


def calculate_gross_pay(employee):
    """
    Calculates the gross pay for the employee.
    Formula: hourly rate * hours worked.
    """
    employee['gross_pay'] = employee['hourly_rate'] * employee['hours_worked']


def calculate_deductions(employee, tax_rate=0.2, insurance_rate=0.05):
    """
    Calculates total deductions as a sum of tax and insurance.
    Tax and insurance are percentages of the employee's gross pay.
    """
    employee['deductions'] = (employee['gross_pay'] * tax_rate) + (employee['gross_pay'] * insurance_rate)


def calculate_net_pay(employee):
    """
    Calculates net pay for the employee.
    Formula: gross pay - deductions.
    """
    employee['net_pay'] = employee['gross_pay'] - employee['deductions']


def generate_pay_slip(employee):
    """
    Prints a simple pay slip for the employee showing gross pay, deductions, and net pay.
    """
    print(f"\nPay Slip for {employee['name']}")
    print(f"Gross Pay: ${employee['gross_pay']:.2f}")
    print(f"Deductions: ${employee['deductions']:.2f}")
    print(f"Net Pay: ${employee['net_pay']:.2f}")
    print("-" * 30)


def process_payroll():
    """
    Processes payroll for all employees by setting hours worked, calculating gross pay,
    deductions, and net pay, and then printing a pay slip for each employee.
    """
    for employee in employees:
        # Set hours worked and calculate the pay details
        set_hours_worked(employee)
        calculate_gross_pay(employee)
        calculate_deductions(employee)
        calculate_net_pay(employee)
        generate_pay_slip(employee)


def main():
    """
    Main function to manage the payroll system.
    Asks the user for the number of employees, adds them to the system, and processes payroll.
    """
    # Get the number of employees
    num_employees = int(input("Enter the number of employees: "))

    # Loop to add each employee to the system
    for _ in range(num_employees):
        add_employee()  # Add each employee to the global employee list

    # Process payroll for all employees
    process_payroll()


# Entry point for the program
if __name__ == "__main__":
    main()

