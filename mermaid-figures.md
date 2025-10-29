### DRY Principle
```mermaid
mindmap
  root((DRY - Don't Repeat Yourself))
    - Single source of truth
    - Avoid duplicate code & logic
    - Use functions, classes, modules
    - Easier maintenance & fewer bugs
```

### Zen of Python
```mermaid
mindmap
The Zen of Python (PEP 20)
  - Beautiful > Ugly
  - Explicit > Implicit
  - Simple > Complex
  - Complex > Complicated
  - Readability counts
  - One obvious way to do it
  - Now > Never
```




### Separation of Concerns Hierarchy in Python

```mermaid
graph TD
    A[Function Level] --> B[Class Level]
    B --> C[Module Level]
    C --> D[Package Level]
    D --> E[Layer Level]
    E --> F[System Level]

    subgraph "Separation of Concerns Hierarchy in Python"
        A
        B
        C
        D
        E
        F
    end

    A:::level1
    B:::level2
    C:::level3
    D:::level4
    E:::level5
    F:::level6

    classDef level1 fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px;
    classDef level2 fill:#E8F5E9,stroke:#43A047,stroke-width:2px;
    classDef level3 fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px;
    classDef level4 fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px;
    classDef level5 fill:#FBE9E7,stroke:#E53935,stroke-width:2px;
    classDef level6 fill:#ECEFF1,stroke:#37474F,stroke-width:2px;


```

### Creational Design Patterns 1

```mermaid
mindmap
  root((Creational Design Patterns))
    description(Deals with object creation mechanisms)
    Factory Method
      note(Lets subclasses decide which class to instantiate)
    Abstract Factory
      note(Creates families of related objects)
    Builder
      note(Constructs complex objects step by step)
    Prototype
      note(Creates new objects by cloning existing ones)
    Singleton
      note(Ensures only one instance of a class)
    Object Pool
      note(Reuses limited resources instead of recreating)


```
### Creational Design Patterns 2

```mermaid
mindmap
  root((Creational Design Patterns))
    description(Deals with object creation mechanisms)
    Factory Method
      note(Lets subclasses decide which class to instantiate)
    Abstract Factory
      note(Creates families of related objects)
    Builder
      note(Constructs complex objects step by step)
    Prototype
      note(Creates new objects by cloning existing ones)
    Singleton
      note(Ensures only one instance of a class)
    Object Pool
      note(Reuses limited resources instead of recreating)


```

### Structural Design Patterns 1

```mermaid
mindmap
  root((Structural Design Patterns))
    description(Simplifies relationships between classes and objects)
    Adapter
      note(Converts one interface into another)
    Decorator
      note(Adds new behavior dynamically)
    Bridge
      note(Separates abstraction from implementation)
    Facade
      note(Provides simple interface to complex system)
    Flyweight
      note(Shares common data to save memory)
    Proxy
      note(Controls access to another object)


```
### Structural Design Patterns 2

```mermaid
mindmap
  root((Structural Design Patterns))
    description(Simplifies relationships between classes and objects)
    Adapter
      note(Converts one interface into another)
    Decorator
      note(Adds new behavior dynamically)
    Bridge
      note(Separates abstraction from implementation)
    Facade
      note(Provides simple interface to complex system)
    Flyweight
      note(Shares common data to save memory)
    Proxy
      note(Controls access to another object)


```
### Behavioral Design Patterns 1

```mermaid
mindmap
  root((Behavioral Design Patterns))
    description(Manages communication and control flow among objects)
    Chain of Responsibility
      note(Passes requests along handlers)
    Command
      note(Encapsulates requests as objects)
    Observer
      note(Notifies dependents of state changes)
    State
      note(Changes behavior when internal state changes)
    Interpreter
      note(Defines grammar and interprets sentences)
    Strategy
      note(Selects algorithm at runtime)
    Memento
      note(Saves and restores object state)
    Iterator
      note(Sequentially accesses collection elements)
    Template Method
      note(Defines algorithm skeleton, defers details)


```
### Behavioral Design Patterns 2

```mermaid
mindmap
  root((Behavioral Design Patterns))
    description(Manages communication and control flow among objects)
    Chain of Responsibility
      note(Passes requests along handlers)
    Command
      note(Encapsulates requests as objects)
    Observer
      note(Notifies dependents of state changes)
    State
      note(Changes behavior when internal state changes)
    Interpreter
      note(Defines grammar and interprets sentences)
    Strategy
      note(Selects algorithm at runtime)
    Memento
      note(Saves and restores object state)
    Iterator
      note(Sequentially accesses collection elements)
    Template Method
      note(Defines algorithm skeleton, defers details)


```

### Architectural Patterns 1

```mermaid
mindmap
  root((Architectural Patterns))
    description(High-level templates for structuring software systems)
    Model-View-Controller (MVC)
      note(Separates data, logic, and presentation)
    Microservices
      note(Independent, loosely coupled services)
    Serverless
      note(Executes code in cloud-managed environments)
    Event Sourcing
      note(Stores state changes as events)


```
### Architectural Patterns 2

```mermaid
mindmap
  root((Architectural Patterns))
    description(High-level templates for structuring software systems)
    Model-View-Controller (MVC)
      note(Separates data, logic, and presentation)
    Microservices
      note(Independent, loosely coupled services)
    Serverless
      note(Executes code in cloud-managed environments)
    Event Sourcing
      note(Stores state changes as events)


```



### Concurrency & Asynchronous Patterns 1

```mermaid
mindmap
  root((Concurrency & Asynchronous Patterns))
    description(Manages multiple operations simultaneously)
    Thread Pool
      note(Reuses threads for multiple tasks)
    Worker Model
      note(Producers send tasks to worker consumers)
    Future & Promise
      note(Represents results of async operations)
    Reactive Observer
      note(Handles continuous data streams asynchronously)


```

### Concurrency & Asynchronous Patterns 2

```mermaid
mindmap
  root((Concurrency & Asynchronous Patterns))
    description(Manages multiple operations simultaneously)
    Thread Pool
      note(Reuses threads for multiple tasks)
    Worker Model
      note(Producers send tasks to worker consumers)
    Future & Promise
      note(Represents results of async operations)
    Reactive Observer
      note(Handles continuous data streams asynchronously)


```

### Performance Patterns

```mermaid
mindmap
  root((Performance Patterns))
    description(Improves speed, efficiency, and memory use)
    Cache-Aside
      note(Loads and stores data in cache on demand)
    Memoization
      note(Caches function results for reuse)
    Lazy Loading
      note(Delays initialization until needed)


```
### Distributed Systems Patterns

```mermaid
mindmap
  root((Distributed Systems Patterns))
    description(Makes distributed systems reliable and scalable)
    Throttling
      note(Limits requests to prevent overload)
    Retry
      note(Automatically retries failed operations)
    Circuit Breaker
      note(Stops repeated failures to protect system)


```
### Testing Patterns

```mermaid
mindmap
  root((Testing Patterns))
    description(Simplifies and isolates testing)
    Mock Object
      note(Simulates real objects during tests)
    Dependency Injection
      note(Provides dependencies externally for flexibility)


```


```mermaid


```
