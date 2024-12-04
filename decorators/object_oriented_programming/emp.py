class employee:

    id:int

    age:int

    dept:str


    def set_employee(self,name,id,age,dept):

        self.id=id

        self.name=name

        self.age=age

        self.dept=dept

    def employee_instance(self):
        print(self.name,self.age)    