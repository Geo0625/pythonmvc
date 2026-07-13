class Employee:
    def __init__(self, employee_id, department, base_salary):
        self.employee_id = employee_id
        self._department = department
        self.__base_salary = base_salary
        
    def get_salary(self):
        return self.__base_salary
    
    def set_salary(self, amount):
        print("--------------------------------------------")
        print(f"Updating base salary from: {self.get_salary():,.2f}\nTo: {amount:,.2f}\n....")
        if amount < 0 or amount > 150000:
            print(f"Updating salary failed!\nBase salary: {self.get_salary():,.2f}")
        else:
            self.__base_salary = amount
            print(f"Salary updated successfully!\nNew base salary: {self.get_salary():,.2f}")
        print("--------------------------------------------")
        print()
    
    def display_employee(self):
        print(f"=== Employee Details ===\nEmployee ID: {self.employee_id}\nDepartment: {self._department}\nBase Salary: {self.get_salary():,.2f}\n--------------------------------------------")
        print()
      
emp = Employee("001", "IT Department", 80000)
#Getting using attributes
print("Getting using attributes")
print(emp.employee_id)
print(emp._department)

'''
FOR PRIVATE ATTRIBUTE
print(emp.__base_salary) - will return an error
'''
print(emp.get_salary()) # public method to access the private attribute
print()

#Getting using display_employee method
emp.display_employee()

emp.set_salary(-10)

emp.set_salary(1500000)

emp.set_salary(120000)
emp.display_employee()