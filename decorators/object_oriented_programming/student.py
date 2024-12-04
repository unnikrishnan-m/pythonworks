class student:

    rollnumber:int

    age:int

    course:str


    def set_student(self,name,rollnumber,age,course):

        self.rollnumber=rollnumber

        self.name=name

        self.age=age

        self.course=course
    def display(self):
        print(self.rollnumber,self.name,self.age,self.course)

        student_instance1=student()

        student_instance1.set_student(11,"amal",23,"django")

        student_instance1.display()  