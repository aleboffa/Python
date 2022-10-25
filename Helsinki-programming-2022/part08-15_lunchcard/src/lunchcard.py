# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = 0
        self.balance = balance

    def eat_lunch(self):
        amount = 2.6
        if self.balance > amount:
            self.balance -= amount

    def eat_special(self):
        amount = 4.6
        if self.balance > amount:
            self.balance -= amount

    def deposit_money(self, balance: float):
        if balance < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

peters_card = LunchCard(20)
graces_card = LunchCard(30)
# the rest of your main function
peters_card.eat_special()
graces_card.eat_lunch()

print(f"Peter: The balance is {peters_card.balance:.1f} euros")
print(f"Grace: The balance is {graces_card.balance:.1f} euros")

peters_card.deposit_money(20)
graces_card.eat_special()
#graces_card.deposit_money(50)

print(f"Peter: The balance is {peters_card.balance:.1f} euros")
print(f"Grace: The balance is {graces_card.balance:.1f} euros")

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)

print(f"Peter: The balance is {peters_card.balance:.1f} euros")
print(f"Grace: The balance is {graces_card.balance:.1f} euros")

