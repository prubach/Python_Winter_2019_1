class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        Customer.last_id += 1
        self.customer_id = Customer.last_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def __str__(self) -> str:
        return "Customer[{0},{1},{2}]".format(self.customer_id, self.first_name, self.last_name)

class Account:
    last_id = 0
    interest_rate = 0.02
    def __init__(self, customer):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.customer = customer
        self._balance = 0
    def deposit(self, amount):
        self._balance = self._balance + amount
    def charge(self, amount):
        if amount<0:
            raise NegativeAmountException('Amount: ' + str(amount))
        if amount > self._balance:
            raise NotEnoughMoneyException('Not enough money')
            #return -1
        self._balance = self._balance - amount
        return 0
    def calc_interest(self):
        self._balance = self._balance + self.calc_interest_value(self._balance)
    @classmethod
    def calc_interest_value(cls, amount):
        return cls.interest_rate*amount
    def get_balance(self):
        return self._balance
    def __str__(self) -> str:
        return "{3}[{0},{1},{2}]".format(self.account_id, self._balance, self.customer.last_name, self.__class__.__name__)

class SavingsAccount(Account):
    interest_rate = 0.03

class DebitAccount(Account):
    interest_rate = 0.001

class BankException(Exception):
    pass

class NotEnoughMoneyException(BankException):
    pass

class NegativeAmountException(BankException):
    pass

c1 = Customer('Anne', 'Smith', 'anne@smith.com')
c2 = Customer('John', 'Brown', 'john@smith.com')
print(c1)
#a1 = SavingsAccount(c1)
a1 = DebitAccount(c1)
print(a1)
a1.deposit(300)
s = str(a1)
print(a1.get_balance())
try:
    res = a1.charge(400)
    print("Result of charge: " + str(res))
except NegativeAmountException as ne:
    print(ne)
    print("continuing...")
except BankException as e:
    print(e)
    #quit(0)
    exit(0)
    #raise(e)
a1.calc_interest()
print(a1)

#print("res=" + res)
#print(c2)
