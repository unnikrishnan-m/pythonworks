class Person:


    def __init__(self,name,age):

        self.name=name

        self.age=age

    def display_person(self):

      print(self.name,self.age)       
       

class Employee:

    def __init__(self,eid,salary):

        self.eid=eid


        self.salary=salary

    def display_employee(self):

      print(self.eid,self.salary)

class Manager(Person,Employee):

    def __init__(self,age,name,eid,salary,department):
        Person.__init__(self,age,name) 
        Employee.__init__(self,eid,salary)  

        self.department=department

    def display_manager_info(self):

        self.display_person()

        self.display_employee()

        print(self.department)


manage_instance=Manager(32,"hari","e34",23456,"hr")
manage_instance.display_manager_info()     




