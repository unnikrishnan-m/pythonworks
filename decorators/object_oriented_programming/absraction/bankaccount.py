class Bankaccount:

    def __init__(self,custumer_name,mpin,account_ype,balance):
        self.custumer_name=custumer_name

        self.__mpin=mpin

        self.account_type=account_ype

        self.__balance=balance


    def get_balance(self):

        print(self.__balance)

    def __str__(self):

        return self.custumer_name

bank_account_instance=Bankaccount("hari",23,"savings",3459)

bank_account_instance.get_balance()