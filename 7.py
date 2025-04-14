class Student:
    def __init__(self, student_id="", name="", address="", admission_year=0, level="", section=""):
       
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section
    
    def input_details(self):
       
        print("\nEnter Student Details:")
        print("-" * 25)
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Full Name: ")
        self.address = input("Enter Address: ")
        
        
        while True:
            try:
                self.admission_year = int(input("Enter Admission Year: "))
                
                if 1900 <= self.admission_year <= 2100:
                    break
                else:
                    print("Please enter a valid year between 1900 and 2100.")
            except ValueError:
                print("Please enter a valid year (numeric value).")
        
        self.level = input("Enter Level: ")
        self.section = input("Enter Section: ")
    
    def display_details(self):
       
        print("\nStudent Information:")
        print("-" * 25)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

def main(): 
    student = Student()
    student.input_details()
    student.display_details()
if __name__ == "__main__":
    main()