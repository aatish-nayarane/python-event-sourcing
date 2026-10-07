from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Event:
    timestamp: datetime

@dataclass(frozen=True)
class AccountCreated(Event):
    account_id: str

@dataclass(frozen=True)
class MoneyDeposited(Event):
    amount: float

@dataclass(frozen=True)
class MoneyWithdrawn(Event):
    amount: float