import json
import os
from account import Account
# save and load account from a json file

class AccountStorage:
    def __init__(self):
        self.account = {}

    def add_account(self, name, amount):
        self.account[name] = Account(name, amount)

    def save_account(self, name, filename="data.json"):
        if name not in self.account:
            print(f"No account with name {name} was found")
            return
        
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try: 
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}
        
        data[name] = self.account[name].to_dict()

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        #print(f"Account '{name}' saved successfully.")
   
    def load_account(self, target_name, filename="data.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        acc_data = data.get(target_name)
        if acc_data is None:
           return None
           #raise ValueError("Account not found")

        return Account(acc_data["name"], acc_data["amount"])
            
      

