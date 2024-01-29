import random

class Account:
    print("Write your name")
    owner = input()
    balance = random.choice(range(1000,100001))
    print(f"Your balance is {balance}")
    print()
    def withdraw(self):
        print("Write sum that you want to withdraw")
        x = int(input())
        if self.balance >= x:
            print(f"You withdrawed {x} tenghe!")
        else:
            print("insufficient funds!")
    def deposit(self):
        print("Write sum that you want to deposit")
        x = int(input())
        print(f"You deposited {x} tenghe!")

x = Account()
#x.withdraw()
x.deposit()


