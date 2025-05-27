class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self, name, age, student_number, course, year):
        super().__init__(name, age)
        
        self.student_number = student_number
        self.course = course
        self.year = year
        
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.student_number)
        print(self.course)
        print(self.year)
        
class Lecturer(Person):
    def __init__(self, name, age, employee_number, department):
        super().__init__(name, age)
        
        self.employee_number = employee_number
        self.department = department
        
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.employee_number)
        print(self.department)
        
class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age)
        
        self.staff_id = staff_id
        self.role = role
        
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.staff_id)
        print(self.role)
        
st1 = Student("Joyce", 22, "ST0034", "BSSE", 2023)
lect = Lecturer("Charity", 38, "E004", "Department of Networks")
s1 = Staff("Evelyn", 40, "E024", "Registrar")


st1.display_info()
print("-" * 30)

lect.display_info()
print("-" * 30)

s1.display_info()