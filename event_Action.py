from datetime import datetime
from  define_events import  *

def create_account(event_store, account_id):
    event = AccountCreated(timestamp=datetime.now(), account_id=account_id)
    event_store.append(event)

def deposit(event_store, amount):
    event = MoneyDeposited(timestamp=datetime.now(), amount=amount)
    event_store.append(event)

def withdraw(event_store, amount, current_balance):
    if amount > current_balance:
        raise Exception("Insufficient funds")

    event = MoneyWithdrawn(timestamp=datetime.now(), amount=amount)
    event_store.append(event)