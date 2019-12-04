class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self) -> str:
        return "Customer[{0},{1}]".format(self.first_name, self.last_name)

class Account:
    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

c = Customer('Anne', 'Smith', 'anne@smith.com')
print(c)

