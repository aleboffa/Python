class BankAccount:
    def __init__(self, customer: str, account_number: str, saldo: float, credit: float):
        self.customer = customer
        self.account_number = account_number
        self.saldo = saldo
        self.credit = credit

    def __str__(self):
        return (f"BankAccount(customer={self.customer}, " + 
            f"account_number={self.account_number}, " +  
            f"saldo={self.saldo}, credit={self.credit})")

    def __eq__(self, another):
        return self.account_number == another.account_number

    def __gt__(self, another):
        return (self.saldo + self.credit) > (another.saldo + another.credit)

    def __add__(self, another):
        client = BankAccount(self.customer, self.account_number, (self.saldo + another.saldo), (self.credit + another.credit))
        return client


####################################################################
if __name__=="__main__":
    account1 = BankAccount("Peter Python", "12345", 200.0, 300.0)
    account2 = BankAccount("Paula Python", "12345", 100.0, 500.0)
    print(account1 == account2)
    print(account1 > account2)
    print(account2 > account1)

    pt3 = account1 + account2
    print(pt3)

#########################################
# output

# True
# False
# True
# BankAccount(customer=Peter Python, account_number=12345, saldo=300.0, credit=800.0)