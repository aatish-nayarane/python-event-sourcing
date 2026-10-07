# Python Event Sourcing

A Python project demonstrating the **Event Sourcing design pattern** using a simple banking domain.

Instead of storing only the current state of an entity, the application stores a sequence of events that represent every state-changing action. The current state can then be reconstructed by replaying those events.

## Project Structure

```text
.
├── bankdetails.py
├── define_events.py
├── event_Action.py
├── event_store.py
├── test_event.py
├── docs/
├── __init__.py
└── README.md
```

## Event Sourcing

Event Sourcing is a design pattern where changes to application state are stored as a sequence of immutable events.

Instead of storing:

```text
Account Balance = 5000
```

the system stores events such as:

```text
AccountCreated
MoneyDeposited
MoneyWithdrawn
MoneyDeposited
```

The current state can be reconstructed by replaying these events in order.

```text
                Events
                   |
                   v
        +---------------------+
        |     Event Store      |
        +---------------------+
                   |
                   v
        Event Replay / Apply
                   |
                   v
        +---------------------+
        |   Current State     |
        +---------------------+
```

## Key Components

### Event Definitions

`define_events.py`

Contains the events used by the application.

Events represent something that has already happened in the system.

Examples:

```text
AccountCreated
MoneyDeposited
MoneyWithdrawn
```

### Event Store

`event_store.py`

Responsible for storing and retrieving events.

The event store acts as the source of truth for the application's state.

Basic flow:

```text
Command
   |
   v
Generate Event
   |
   v
Store Event
   |
   v
Replay Events
   |
   v
Current State
```

### Event Actions

`event_Action.py`

Contains operations/actions that generate domain events.

For example:

```text
Deposit
Withdraw
Create Account
```

An action does not simply modify the current state. Instead, it produces an event that represents the state change.

### Bank Details

`bankdetails.py`

Contains the banking domain logic and state representation used by the example.

The state can be rebuilt by applying previously stored events.

### Tests

`test_event.py`

Contains tests for the event sourcing implementation.

Run the tests with:

```bash
python -m pytest
```

## Event Replay

One of the important concepts demonstrated by this project is **event replay**.

Suppose an account has the following events:

```text
1. AccountCreated
2. MoneyDeposited(1000)
3. MoneyDeposited(500)
4. MoneyWithdrawn(200)
```

The state can be reconstructed as:

```text
Initial Balance = 0

+ 1000
+  500
-  200
---------
  1300
```

The current state is therefore:

```text
Balance = 1300
```

The important point is that the state is derived from the events rather than being the primary source of truth.

## Advantages of Event Sourcing

### Complete History

Every state-changing operation is preserved as an event.

### Auditability

The complete history of changes can be inspected.

### State Reconstruction

The current state can be rebuilt by replaying events.

### Debugging

Historical events can help identify how a particular state was reached.

### Temporal Queries

The system can potentially reconstruct the state of an entity at an earlier point in time.

## Important Concepts

This project demonstrates the following concepts:

- Event Sourcing
- Domain Events
- Event Store
- Event Replay
- State Reconstruction
- Immutable Events
- Command and Event separation
- Domain-driven design concepts
- Event-driven architecture
- Unit testing

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd python-event-sourcing
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies if a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

Run the application/example:

```bash
python <entry-point>.py
```

Run tests:

```bash
python -m pytest
```

## Learning Goals

The purpose of this project is to understand how Event Sourcing works internally and how application state can be derived from a sequence of events.

Key learning areas:

1. Event Sourcing pattern
2. Domain events
3. Event storage
4. Event replay
5. State reconstruction
6. Event-driven design
7. Separation of actions and state changes
8. Testing event-based systems

## Future Improvements

Possible improvements include:

- Persistent event storage
- Event versioning
- Event serialization
- Event schema validation
- Snapshots
- Event replay from a specific version
- Optimistic concurrency control
- REST API integration
- PostgreSQL-based event store
- Message broker integration
- Better domain boundaries

## License

This project is licensed under the terms specified in the `LICENSE` file.