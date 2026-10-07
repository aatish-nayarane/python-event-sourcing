from  event_store import   EventStore
from  bankdetails import *
from  event_Action  import  *

store = EventStore()

# Commands
create_account(store, "acc-123")
deposit(store, 1000)
deposit(store, 500)

# Rebuild state
account = BankAccount()
account.load_from_events(store.get_all())

# Withdraw safely
withdraw(store, 300, account.balance)

# Rebuild again after new event
account = BankAccount()
account.load_from_events(store.get_all())

print("Final Balance:", account.balance)