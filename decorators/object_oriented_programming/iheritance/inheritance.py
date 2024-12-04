
class GrandParent:
     
     def m(self):
          print("grand parent class m1 method")


class Parent:
     def m(self):
          print("parent class m2 method")

class Child(Parent,GrandParent):#first work parent in method|class child(Grandparent,Parent):work GP methode
     def m3(self):
          print("chilfd class m3 mthod")
chiid_instance=Child()
chiid_instance.m()
chiid_instance.m()
chiid_instance.m3()