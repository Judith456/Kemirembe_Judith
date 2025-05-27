#Example 1. Printer Device
class Device:
    def start(self):
        print("The device turned on")
        
class Printer(Device):
    def start(self):
        print("The printer connects to the computer")
        
p = Printer()
p.start()

print("-" * 50)
#Example 2.Payment
class Payment:
    def make_payment(self):
        print("Choose payment options")
        
class PayPal(Payment):
    def make_payment(self):
        print("Redirects to paypal gateway")
        
class CreditCard(Payment):
    def make_payment(self):
        print("Requeting card number")
        
p1 = PayPal()
c1 = CreditCard()

p1.make_payment()
c1.make_payment()

print("-" * 50)
class EmployeeSalary:
    def calculate_salary(self, salary):
        self.salary = salary
        print(f"Employee salary is {salary}")
        
class ManagerSalary(EmployeeSalary):
    def calculate_salary(self, salary, bonus):
        super().calculate_salary(salary)
        self.bonus = bonus
        total_salary = self.salary + self.bonus
        print(f"Manager salary is {total_salary}")
 
emp1 = EmployeeSalary()      
manager = ManagerSalary()

manager.calculate_salary(34000, 1000)
