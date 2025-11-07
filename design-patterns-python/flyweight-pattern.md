


## Flyweight pattern implementation example

```python
class Connection:
    """Flyweight: Represents a reusable shared connection (simulated)."""
    def __init__(self, server_name):
        self.server_name = server_name
        print(f"🔌 Creating new connection to '{server_name}'")

    def send(self, message):
        print(f"[{self.server_name}] Sending message → {message}")


class ConnectionPool:
    """Flyweight Factory: Creates & reuses 
    shared Connection objects."""
    _connections = {}

    @classmethod
    def get_connection(cls, server_name):
        if server_name not in cls._connections:
            cls._connections[server_name] = Connection(server_name)
        else:
            print(f"Reusing existing connection to-> '{server_name}'")
        return cls._connections[server_name]


# --- Client Code ---
pool = ConnectionPool()

# Multiple clients requesting connections
conn1 = pool.get_connection("Server-A")
conn2 = pool.get_connection("Server-B")
conn3 = pool.get_connection("Server-A")  # Reuses conn1

# Use connections to send messages
conn1.send("Ping 1")
conn2.send("Ping 2")
conn3.send("Ping 3 (same connection as Ping 1)")

# Verify shared flyweight
print("\nIs conn1 same as conn3?", conn1 is conn3)

```

#### Flowchart showing the execution of above script

```mermaid

flowchart TD
    A[Client Request] --> B["ConnectionPool.get_connection(server_name)"]
    B --> C{"Connection exists?"}
    C -- No --> D["Create new Connection(server_name)"]
    C -- Yes --> E["Return existing Connection"]
    D --> F["Store in _connections dict"]
    E --> F
    F --> G["Connection.send(message)"]


```

#### Sequence Diagram — Flyweight (Connection Pool)

```mermaid
sequenceDiagram
    autonumber
    participant Client
    participant Pool as ConnectionPool
    participant Conn as Connection

    Note over Client,Pool: Client requests connection to "Server-A"
    Client->>Pool: get_connection("Server-A")
    alt Connection not in _connections
        Pool->>Conn: Create new Connection("Server-A")
        Conn-->>Pool: Return new Connection instance
        Pool->>Pool: Store instance in _connections["Server-A"]
    else Connection already exists
        Pool-->>Client: Return existing Connection
    end
    Pool-->>Client: Return Connection object

    Note over Client,Conn: Client sends a message using the connection
    Client->>Conn: send("Ping 1")

    Note over Client,Pool: Later, another request for "Server-A"
    Client->>Pool: get_connection("Server-A")
    Pool-->>Client: Reuse same Connection instance

    Client->>Conn: send("Ping 2")

    Note over Client: Both calls used the same shared object

```

#### Python code diagram (with arrows showing calls like get_connection → Connection() → send() flow

```mermaid
flowchart TD
    A["Client Code"] -->|"requests connection"| B["ConnectionPool (Flyweight Factory)"]

    B -->|"checks cache"| C{"_connections cache"}
    C -->|"miss"| D["Connection object (new Flyweight)"]
    C -->|"hit"| D["Existing shared Connection"]

    D -->|"use connection"| E["Shared state: db_name (intrinsic data)"]

    A -->|"uses shared connection"| D

    subgraph Note["Flyweight Pattern Summary"]
        direction TB
        N1["Client asks factory for an object"]
        N2["Factory returns existing one if available"]
        N3["Otherwise creates, caches, and returns new one"]
        N4["Result → fewer objects, shared memory"]
    end

    Note -.-> A



```





