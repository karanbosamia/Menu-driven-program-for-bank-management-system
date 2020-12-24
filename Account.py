class Account:

    def __init__(self, acc_no, name, balance):
        self._acc_no = acc_no
        self._name = name
        self._balance = balance
        print("Account created for " + self._name)
        self.display_account()
        print("*" * 40)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("The amount deposited in your account is {} Rs.".format(amount))
            self.display_account()
            print("*" * 40)
    
    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
            print("The amount withdrawn from your account is {} Rs.".format(amount))
        else:
            print("The amount must be greater than zero or it should not be higher than your account balance")
        self.display_account()
        print("*" * 40)
        
    def display_account(self):
        print("Account name: {}\nAccount number: {}\nBalance: {}".format(self._name, self._acc_no, self._balance))

        
if __name__ == '__main__':
    karan = Account(121412111241, "Karan", 2522)
    karan.deposit(200)
    karan.withdraw(2000)
    karan.withdraw(723)
