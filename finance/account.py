from transaction import Transaction

class Account: 
    def __init__(self, name, amount=0):
        self.amount = amount
        self.name = name
        self.transactions = []
    
    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount
        }
    
    def add_transaction(self, amount, data, t_type):
        if t_type == "withdraw" and amount > self.amount:
            print("Not enough funds.")
            return
        
        if t_type == "withdraw":
            self.amount -= amount
        else:
            self.amount += amount

        t = Transaction(amount, data, t_type)
        self.transactions.append(t)

        print(f"{t_type.capitalize()}: {amount:.2f} DKK")
        print(f"New balance: {self.amount:.2f} DKK")

    def deposit(self, amount, date):
        self.add_transaction(amount, date, "deposit")

    def withdraw(self, amount, date):
        self.add_transaction(amount, date, "withdraw")

    def view_transaction(self):
        if not self.transactions:
            print("No transactions yet")
            return
        
        for t in self.transactions:
            print(t)

    def filter_by_category(self, category):
        filtered = [t for t in self.transactions if t.category == category]

        if not filtered:
            print(f"No transactions found for '{category}'")
            return
        
        for t in filtered:
            print(t)



