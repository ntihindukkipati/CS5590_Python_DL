class Employee():  #parent class
    employee_count=0    #class variable
    salary=0   #class variable

    # n=name, f=family, s=salary, d= department
    def __init__(self,n,f,s,d):
        self.name =n
        self.family =f
        Employee.salary +=int(s)
        self.department =d
        Employee.employee_count+=1

    def Average_Salary(self):
        self.avgsalary=Employee.salary/Employee.employee_count     #averaging the employee salary

class FullTimeEmployee(Employee):   #defining parent class
    def __init__(self):
        Employee.Average_Salary(self)          #calling the parent class method
        print("Average Salary Of total employees =",self.avgsalary)

c=Employee('Nsd','safj',1000,'cse')  #initiating an object for Employee class
c=Employee('Ns','saj',2000,'cse')
k=FullTimeEmployee()               #iniitiating an object for FulltimeEmployee





