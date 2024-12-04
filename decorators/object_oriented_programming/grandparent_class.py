class GrandParent:
     
     def m1(self):
          print("grand parent class m1 method")


class Parent:
     def m2(self):
          print("parent class m2 method")

class Child(Parent,GrandParent):
     def m3(self):
          print("chilfd class m3 mthod")
chiid_instance=Child()
chiid_instance.m3()
chiid_instance.m2()
chiid_instance.m1()