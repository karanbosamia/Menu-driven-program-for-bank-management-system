class Account:

    def __init__(self, acc_no, name, balance):
        self._acc_no = acc_no
        self._name = name
        self._balance = balance
        print("Account created for " + self._name)
        self.display_account()
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.display_account()
