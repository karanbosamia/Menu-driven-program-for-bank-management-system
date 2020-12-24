class Account:

    def __init__(self, acc_no, name, balance):
        if len(acc_no) == 12 or len(acc_no) == 14:
            self._acc_no = acc_no
        else:
            print("Account can't be created as your account no. isn't a 12 digit or a 14 digit number")
            break
        self._name = name
        self._balance = balance
        print("Account created for " + self._name)
        self.display_account()
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.display_account()
    
    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
        else:
            print("The amount must be greater than zero and should not be higher than your account balance")
        self.display_account()
        
     
