class Employee():
    def __init__(self, emp_name, emp_age, salary):
        self.__emp_name = emp_name          
        self.__emp_age = emp_age      
        self.__salary = salary 

    def get_emp_name(self):
        return self.__emp_name
    def get_emp_age(self):
        return self.__emp_age
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
    def annual_income(self):
        pass
class fulltime(Employee):
    def annual_income(self):
        return self.get_salary() * 12
class parttime(Employee):
    def __init__(self, emp_name, emp_age, amt_per_hour, total_hours_worked):
        super().__init__(emp_name, emp_age, amt_per_hour * total_hours_worked )
        self.__amt_per_hour = amt_per_hour  
        self.__total_hours_worked = total_hours_worked  

    def annual_income(self):
        return self.__amt_per_hour * self.__total_hours_worked * 12
def employee_details(employee):
    print(f"Employee Name: {employee.get_emp_name()}")
    print(f"Employee age: {employee.get_emp_age()}")
    print(f"Monthly Salary: {employee.get_salary()}")
    print(f"Annual income: {employee.annual_income()}")

if __name__ == "__main__":
 emp1 = fulltime("kiru", 21, 15000)
 emp2 = parttime("deepi", 21, 50, 100)
 print("Fulltime Employee Details:")
 employee_details(emp1)
 print("\nPartime Employee Details:")
 employee_details(emp2)
