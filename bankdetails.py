from  define_events import  *

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_id = None

    def apply(self, event):
        if isinstance(event, AccountCreated):
            self.account_id = event.account_id

        elif isinstance(event, MoneyDeposited):
            self.balance += event.amount

        elif isinstance(event, MoneyWithdrawn):
            self.balance -= event.amount

    def load_from_events(self, events):
        for event in events:
            self.apply(event)