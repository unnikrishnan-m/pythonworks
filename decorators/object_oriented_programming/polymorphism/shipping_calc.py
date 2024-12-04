class shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping(shipping):
    
    def calculate_shipping_cost(self,weight):

        print(weight*20)

class StandardShipping(shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*10)

express_instance=ExpressShipping()

express_instance.calculate_shipping_cost(10)

Standard_instance=StandardShipping()

Standard_instance.calculate_shipping_cost(20)
