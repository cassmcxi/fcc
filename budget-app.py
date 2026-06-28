
#python certification project

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.amount = amount
        self.description = description=''

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

        print(self.deposit(12.89))

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass

    def create_spend_chart(categories):
        pass