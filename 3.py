import csv
import os
class Employee:
    def __init__(self, empid="", name="", address="", contact_number="", 
                 spouse_name="", number_of_child=0, salary=0.0):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary
    def input_details(self):
        try:
            print("\nEnter Employee Details:")
            print("-" * 25)
            self.empid = input("Enter Employee ID: ")
            self.name = input("Enter Full Name: ")
            self.address = input("Enter Address: ")
            while True:
                self.contact_number = input("Enter Contact Number: ")
                if self.contact_number.isdigit() or self.contact_number == "":
                    break
                else:
                    print("Contact number should contain only digits.")
            self.spouse_name = input("Enter Spouse Name (leave blank if not applicable): ")
            while True:
                try:
                    child_input = input("Enter Number of Children: ")
                    self.number_of_child = int(child_input) if child_input else 0
                    if self.number_of_child >= 0:
                        break
                    else:
                        print("Number of children cannot be negative.")
                except ValueError:
                    print("Please enter a valid number.")
            while True:
                try:
                    salary_input = input("Enter Salary: ")
                    self.salary = float(salary_input) if salary_input else 0.0
                    if self.salary >= 0:
                        break
                    else:
                        print("Salary cannot be negative.")
                except ValueError:
                    print("Please enter a valid amount.")
            return True   
        except Exception as e:
            print(f"An error occurred while inputting employee details: {e}")
            return False
    def to_dict(self):
        return {
            'Employee ID': self.empid,
            'Name': self.name,
            'Address': self.address,
            'Contact Number': self.contact_number,
            'Spouse Name': self.spouse_name,
            'Number of Children': self.number_of_child,
            'Salary': self.salary
        }
    def display(self):
       
        print(f"ID: {self.empid}, Name: {self.name}, Address: {self.address}")
        print(f"Contact: {self.contact_number}, Spouse: {self.spouse_name}")
        print(f"Children: {self.number_of_child}, Salary: ${self.salary:.2f}")
class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = []
        self.fieldnames = ['Employee ID', 'Name', 'Address', 'Contact Number', 
                          'Spouse Name', 'Number of Children', 'Salary']
        self.load_employees()
    def load_employees(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        emp = Employee(
                            row['Employee ID'],
                            row['Name'],
                            row['Address'],
                            row['Contact Number'],
                            row['Spouse Name'],
                            int(row['Number of Children']),
                            float(row['Salary'])
                        )
                        self.employees.append(emp)
                print(f"Loaded {len(self.employees)} employees from file.")
            else:
                print("No existing employee data found. Starting with empty database.")
        except Exception as e:
            print(f"Error loading employees: {e}")
    
    def add_employee(self):
       
        try:
            emp = Employee()
            if emp.input_details():
                self.employees.append(emp)
                print("Employee added successfully!")
                return True
            return False
        except Exception as e:
            print(f"Error adding employee: {e}")
            return False
    
    def save_to_csv(self):
       
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                for emp in self.employees:
                    writer.writerow(emp.to_dict())
            print(f"Successfully saved {len(self.employees)} employees to {self.filename}")
            return True
        except PermissionError:
            print(f"Permission denied. Cannot write to {self.filename}")
            return False
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return False
    
    def display_all_employees(self):
        
        if not self.employees:
            print("No employees to display.")
            return
        
        print("\nEmployee List:")
        print("-" * 50)
        for i, emp in enumerate(self.employees, 1):
            print(f"\nEmployee #{i}:")
            emp.display()
            print("-" * 50)
    
    def search_employee(self, empid):
        
        for emp in self.employees:
            if emp.empid == empid:
                return emp
        return None


def main():
   
    manager = EmployeeManager()
    
    while True:
        try:
            print("\nEmployee Management System")
            print("=" * 25)
            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee by ID")
            print("4. Save and Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == '1':
                manager.add_employee()
                # Save after each addition
                manager.save_to_csv()
                
            elif choice == '2':
                manager.display_all_employees()
                
            elif choice == '3':
                emp_id = input("Enter Employee ID to search: ")
                employee = manager.search_employee(emp_id)
                
                if employee:
                    print("\nEmployee Found:")
                    print("-" * 25)
                    employee.display()
                else:
                    print(f"No employee found with ID: {emp_id}")
                    
            elif choice == '4':
                manager.save_to_csv()
                print("Exiting program. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Saving data...")
            manager.save_to_csv()
            break
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()