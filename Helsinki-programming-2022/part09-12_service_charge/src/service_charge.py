# WRITE YOUR SOLUTION HERE:
class BankAccount():
    def __init__(self, owner: str, account_number: str, balance: float):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance


    def deposit(self, amount: float):
        self.__amount = amount


    def withdraw(self, amount: float):
        self.__amount = amount


    def balance(self):
        pass


    def __service_charge(self):
        pass



if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)


