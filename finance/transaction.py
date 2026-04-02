from datetime import date

class Transaction:
    def __init__(self, amount, date, t_type, category=None):
        self.amount = amount
        self.date = date
        self.type = t_type
        self.category = category

    def __str__(self):
        return f"[{self.date}] {self.type.capitalize()}: {self.amount:.2f} DKK"