from typing import Any


class bank:

    accno:int

    balance:int

    acc_type:int

    customer_name:str

    def __init__(self,accno,balance,acc_type,customer_name):

        self.accno=accno

        self.balance=balance

        self.ac_type=acc_type

        self.customer_name=customer_name

    def deposit(self,acmount):

        self.balance+=acmount

        print(f"your account{self.accno}.0"has been credited {amount}avl balanceP{self})


        def withdraw(self,amount):

            if self.balnce<amount:

                self.balance-=amount

                print(f"your account{self.accno} has been debited with amount {amount}avl bal(self.balance)")


        def get_balance(self):

            print("your available blance is",self.balance)    

                


