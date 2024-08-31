# Leo Dahlen
#CBIS 4210
#assignment 2.2
#8/31/2024

#payroll with user input name, hoursly rate, and hours worked
class Employee:
    def __init__(self, name, hourly_rate):
        """
        Initializes an Employee object with name and hourly rate.
        Hours worked, gross pay, deductions, and net pay will be calculated later.
        """
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0  # Will be input by the user
        self.gross_pay = 0  # Will be calculated later
        self.deductions = 0  # Will be calculated later
        self.net_pay = 0  # Will be calculated later

    def set_hours_worked(self, hours_worked):
        """
        Sets the hours worked for the employee. This will be provided by the user.
        """
        self.hours_worked = hours_worked

    def calculate_gross_pay(self):
        """
        Calculates gross pay as hourly rate multiplied by hours worked.
        Returns the calculated gross pay.
        """
        self.gross_pay = self.hourly_rate * self.hours_worked
        return self.gross_pay

    def calculate_deductions(self, tax_rate=0.2, insurance_rate=0.05):
        """
        Calculates total deductions as the sum of tax and insurance.
        Tax is calculated as a percentage of gross pay.
        Insurance is also a percentage of gross pay.
        Returns the total deductions.
        """
        self.deductions = (self.gross_pay * tax_rate) + (self.gross_pay * insurance_rate)
        return self.deductions

    def calculate_net_pay(self):
        """
        Calculates net pay by subtracting deductions from gross pay.
        Returns the net pay.
        """
        self.net_pay = self.gross_pay - self.deductions
        return self.net_pay

    def generate_pay_slip(self):
        """
        Prints a simple pay slip for the employee showing gross pay, deductions, and net pay.
        """
        print(f"Pay Slip for {self.name}")
        print(f"Gross Pay: ${self.gross_pay:.2f}")
        print(f"Deductions: ${self.deductions:.2f}")
        print(f"Net Pay: ${self.net_pay:.2f}")
        print("-" * 30)  # Separates pay slips for different employees


class Payroll:
    def __init__(self):
        """
        Initializes the Payroll system with an empty list to store Employee objects.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Adds an Employee object to the payroll system.
        """
        self.employees.append(employee)

    def process_payroll(self):
        """
        Loops through all employees, gets the user input for hours worked,
        calculates their pay (gross, deductions, net), and generates their pay slip.
        """
        for employee in self.employees:
            # Get hours worked from user input
            hours_worked = float(input(f"Enter hours worked for {employee.name}: "))
            employee.set_hours_worked(hours_worked)

            # Calculate payroll details
            employee.calculate_gross_pay()  # Calculate the employee's gross pay
            employee.calculate_deductions()  # Calculate the deductions
            employee.calculate_net_pay()  # Calculate the net pay
            employee.generate_pay_slip()  # Print the pay slip for the employee


def main():
    payroll = Payroll()

    # Get the number of employees
    num_employees = int(input("Enter the number of employees: "))

    # Loop to get input for each employee
    for _ in range(num_employees):
        name = input("Enter employee name: ")
        hourly_rate = float(input(f"Enter hourly rate for {name}: "))

        # Create employee object
        employee = Employee(name, hourly_rate)

        # Add employee to payroll
        payroll.add_employee(employee)

    # Process payroll for all employees with user input for hours worked
    payroll.process_payroll()


# Example usage of the payroll system
if __name__ == "__main__":
    main()
